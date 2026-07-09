#!/usr/bin/env python3
"""Fetch missing DOIs/eprints for bib entries using CrossRef + Semantic Scholar."""

import re, time, json, urllib.request, urllib.parse, sys

BIB_FILE = "references.bib"

def crossref_doi(title, author_family):
    """Query CrossRef for a DOI by title and first author."""
    query = urllib.parse.urlencode({
        "query.title": title,
        "query.author": author_family,
        "rows": 1,
        "select": "DOI,title,author"
    })
    url = f"https://api.crossref.org/works?{query}"
    req = urllib.request.Request(url, headers={"User-Agent": "DOI-fetcher/1.0 (grant-proposal)"})
    try:
        with urllib.request.urlopen(req, timeout=8) as r:
            data = json.loads(r.read())
        items = data.get("message", {}).get("items", [])
        if items:
            return items[0].get("DOI", "")
    except Exception as e:
        print(f"  CrossRef error: {e}", file=sys.stderr)
    return ""

def semantic_doi(title):
    """Query Semantic Scholar for DOI."""
    query = urllib.parse.urlencode({"query": title, "fields": "doi,externalIds", "limit": 1})
    url = f"https://api.semanticscholar.org/graph/v1/paper/search?{query}"
    req = urllib.request.Request(url, headers={"User-Agent": "DOI-fetcher/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=8) as r:
            data = json.loads(r.read())
        papers = data.get("data", [])
        if papers:
            p = papers[0]
            doi = p.get("doi", "") or p.get("externalIds", {}).get("DOI", "")
            arxiv = p.get("externalIds", {}).get("ArXiv", "")
            return doi, arxiv
    except Exception as e:
        print(f"  S2 error: {e}", file=sys.stderr)
    return "", ""

def extract_entries(content):
    """Extract (key, full_entry_text) pairs."""
    pattern = r'(@\w+\{(\w+),.*?)(?=@\w+\{|\Z)'
    return [(m.group(2), m.group(1)) for m in re.finditer(pattern, content, re.DOTALL)]

def get_field(entry, field):
    """Extract a field value from a bib entry."""
    m = re.search(rf'{field}\s*=\s*\{{([^}}]*)\}}', entry, re.IGNORECASE)
    if m:
        return m.group(1).strip()
    m = re.search(rf'{field}\s*=\s*"([^"]*)"', entry, re.IGNORECASE)
    if m:
        return m.group(1).strip()
    return ""

def extract_arxiv_id(entry):
    """Try to find an arXiv ID in the journal or note field."""
    for field in ["journal", "note", "howpublished", "url"]:
        val = get_field(entry, field)
        m = re.search(r'(\d{4}\.\d{4,5})', val)
        if m:
            return m.group(1)
    return ""

def add_doi_to_entry(entry, doi):
    """Add doi field to entry if not present."""
    if re.search(r'\bdoi\s*=', entry, re.IGNORECASE):
        return entry  # already has doi
    # Insert before closing brace
    return entry.rstrip().rstrip('}') + f'  doi={{{doi}}}\n}}'

def add_eprint_to_entry(entry, arxiv_id):
    """Add eprint field to entry if not present."""
    if re.search(r'\beprint\s*=', entry, re.IGNORECASE):
        return entry
    return entry.rstrip().rstrip('}') + f'  eprint={{{arxiv_id}}},\n  eprinttype={{arXiv}}\n}}'

with open(BIB_FILE) as f:
    content = f.read()

entries = extract_entries(content)
results = {}  # key -> (doi, arxiv_id)

for key, entry_text in entries:
    has_doi = bool(re.search(r'\bdoi\s*=', entry_text, re.IGNORECASE))
    has_eprint = bool(re.search(r'\beprint\s*=', entry_text, re.IGNORECASE))
    if has_doi and has_eprint:
        continue

    title = get_field(entry_text, "title")
    author_raw = get_field(entry_text, "author")
    author_family = author_raw.split(",")[0].split("and")[0].strip().split()[-1] if author_raw else ""
    arxiv_id = extract_arxiv_id(entry_text)

    doi = ""
    if not has_doi:
        if title and author_family:
            print(f"[{key}] CrossRef lookup: {author_family}, {title[:50]}...")
            doi = crossref_doi(title, author_family)
            time.sleep(0.3)
            if not doi:
                print(f"  -> CrossRef miss, trying S2...")
                doi, arxiv_id2 = semantic_doi(title)
                if not arxiv_id:
                    arxiv_id = arxiv_id2
                time.sleep(0.5)

        if doi:
            print(f"  -> DOI: {doi}")
        elif arxiv_id:
            print(f"  -> arXiv: {arxiv_id}")
        else:
            print(f"  -> NOT FOUND")

    results[key] = (doi, arxiv_id)

# Apply updates
new_content = content
for key, (doi, arxiv_id) in results.items():
    m = re.search(r'(@\w+\{' + key + r',.*?)(?=@\w+\{|\Z)', new_content, re.DOTALL)
    if not m:
        continue
    old_entry = m.group(1)
    new_entry = old_entry

    has_doi = bool(re.search(r'\bdoi\s*=', old_entry, re.IGNORECASE))
    has_eprint = bool(re.search(r'\beprint\s*=', old_entry, re.IGNORECASE))

    if doi and not has_doi:
        new_entry = add_doi_to_entry(new_entry, doi)
    elif arxiv_id and not has_eprint and not doi:
        new_entry = add_eprint_to_entry(new_entry, arxiv_id)

    if new_entry != old_entry:
        new_content = new_content.replace(old_entry, new_entry, 1)

with open(BIB_FILE + ".updated", "w") as f:
    f.write(new_content)

print(f"\nDone. Written to {BIB_FILE}.updated")
print(f"Found DOI: {sum(1 for d,a in results.values() if d)}")
print(f"Found arXiv only: {sum(1 for d,a in results.values() if not d and a)}")
print(f"Not found: {sum(1 for d,a in results.values() if not d and not a)}")
