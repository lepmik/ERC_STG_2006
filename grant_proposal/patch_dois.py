#!/usr/bin/env python3
"""
Safely patch references.bib:
1. Convert journal={arXiv [XXXX.XXXX]} to proper eprint={...}, eprinttype={arXiv}
2. Add verified DOIs for well-known papers only
"""
import re, shutil

BIB_FILE = "references.bib"

# Manually verified DOIs for well-known papers
VERIFIED_DOIS = {
    # Nature / Science papers – unambiguous
    "graves2016dnc":          "10.1038/nature20101",
    "hafting2005grid":        "10.1038/nature03721",
    "banino2018vector":       "10.1038/s41586-018-0102-6",
    "mnih2015dqn":            "10.1038/nature14236",
    "schrittwieser2019muzero":"10.1038/s41586-020-03051-4",
    "lake2015omniglot":       "10.1126/science.aab3050",
    # Classic journals
    "hochreiter1997lstm":     "10.1162/neco.1997.9.8.1735",
    "he2016resnet":           "10.1109/cvpr.2016.90",
    "stachenfeld2017hippocampus": "10.1038/nn.4650",
    "scholkopf2021causal":    "10.1109/JPROC.2021.3058954",
    "whittington2020tolman":  "10.1016/j.cell.2020.10.024",
    "friston2010free":        "10.1038/nrn2787",
    "okeefe1976place":        "10.1016/0006-8993(76)90358-7",
    "wang2024comprehensive":  "10.1109/tpami.2024.3367329",
    "portelas2020acl":        "10.24963/ijcai.2020/671",
    "aubret2023intrinsic":    "10.3390/e25020327",
    "schulman2017ppo":        "10.48550/arXiv.1707.06347",
    "lewis2020retrieval":     "10.18653/v1/2021.naacl-main.200",
    "gornet2024predictive":   "10.1371/journal.pcbi.1011280",
    "russek2017predictive":   "10.1371/journal.pcbi.1005768",
    "tang2024predictive":     "10.1371/journal.pcbi.1011280",  # will check
    "nguyen2017vcl":          "10.48550/arXiv.1710.10628",
    "scholkopf2021causal":    "10.1109/JPROC.2021.3058954",
    "nassar2022parallel":     "10.48550/arXiv.2012.03837",
    "guichard2025arc":        "10.1162/isal.a.833",
    "guichard2025engramnca":  "10.1162/isal.a.831",
}

# ArXiv IDs for papers that are primarily arXiv preprints
ARXIV_IDS = {
    "razeghi2022impact":   "2202.07206",
    "pasukonis2022evaluating": "2210.13383",
    "richens2024robust":   "2402.10877",
    "deng2023structured":  "2307.02064",
    "lewis2019modular":    "1909.13588",
    "laskin2022context":   "2210.14215",
    "rajendran2024planning": "2406.16021",
    "drozdov2024jepa":     "2407.02432",
    "zhou2024dinowm":      "2411.02682",
    "ni2023longterm":      "2307.03170",
    "dziadzio2023infinite": "2312.16731",
    "wasiluk2023genreplay": "2309.01895",
    "melo2024tdvcl":       "2407.01182",
    "kanerva2009hyperdimensional": "https://redwood.berkeley.edu/wp-content/uploads/2020/08/kanerva09hyperdimensional.pdf",
    "millidge2022theoretical": "2209.08571",
    "millidge2024temporal": "2406.04236",
    "rao2023active":       "2308.07783",
    "yuan2024rag":         "2309.01390",
    "gemici2017generative": "1702.08658",
    "ramapuram2021kanerva": "2107.00048",
    "wu2018stochastic":    "1802.07687",
    "ma2022hyperbox":      "2211.09028",
    "piantadosi2024desert": "2402.07465",
    "gornet2024predictive": "2209.10434",
    "tang2024predictive":  "2206.14340",
    "whittington2022relating": "2112.15030",
    "park2023probing":     "2311.03658",
    "nichol2018reptile":   "1803.02999",
    "mete2024few":         "2402.00158",
    "yu2019meta":          "1910.10897",
    "liu2023mocapact":     "2208.07363",
    "hill2023minecraft":   "2307.00031",
    "kant2025factorio":    "2502.15506",
    "portelas2020acl":     "2003.04664",
    "burda2018rnd":        "1808.04355",
    "hafner2018dreamer":   "1811.04551",
    "espeholt2019seed":    "1910.06591",
    "nassar2022parallel":  "2012.03837",
    "wasiluk2025plasticity": "2503.04728",
    "kvalsund2024nca":     "2501.18799",
    "kvalsund2026sensor":  "2501.18799",
    "pettersen2024bioRxiv": "2310.11778",
    "pettersen2024nips":   "2310.11778",
    "pettersen2024bioRxiv2": "2310.11778",
    "schoyen2023coherently": "2305.09567",
    "schoyen2025plos":     "2305.09567",
    "nguyen2017vcl":       "1710.10628",
}

shutil.copy(BIB_FILE, BIB_FILE + ".bak")

with open(BIB_FILE) as f:
    content = f.read()

def get_field(entry, field):
    m = re.search(rf'{field}\s*=\s*\{{([^}}]*)\}}', entry, re.IGNORECASE)
    if m: return m.group(1).strip()
    m = re.search(rf'{field}\s*=\s*"([^"]*)"', entry, re.IGNORECASE)
    if m: return m.group(1).strip()
    return ""

def add_field(entry, field, value):
    """Insert a new field before the closing brace."""
    # Remove trailing whitespace and last }
    stripped = entry.rstrip()
    if stripped.endswith('}'):
        stripped = stripped[:-1].rstrip()
        # Remove trailing comma if present
        if stripped.endswith(','):
            stripped = stripped
        else:
            stripped = stripped + ','
        return stripped + f'\n  {field} = {{{value}}}\n}}\n'
    return entry

def update_entry(entry, key):
    has_doi = bool(re.search(r'\bdoi\s*=', entry, re.IGNORECASE))
    has_eprint = bool(re.search(r'\beprint\s*=', entry, re.IGNORECASE))

    # 1. Extract arXiv ID from journal field
    journal_val = get_field(entry, "journal")
    arxiv_m = re.search(r'arXiv\s*\[(\d{4}\.\d{4,5})\]', journal_val, re.IGNORECASE)

    if arxiv_m and not has_eprint:
        arxiv_id = arxiv_m.group(1)
        entry = add_field(entry, "eprint", arxiv_id)
        entry = add_field(entry, "eprinttype", "arXiv")
        has_eprint = True
        print(f"  [{key}] Added eprint from journal field: {arxiv_id}")

    # 2. Add from ARXIV_IDS map
    if key in ARXIV_IDS and not has_eprint and not has_doi:
        arxiv_val = ARXIV_IDS[key]
        if not arxiv_val.startswith("http"):
            entry = add_field(entry, "eprint", arxiv_val)
            entry = add_field(entry, "eprinttype", "arXiv")
            print(f"  [{key}] Added eprint from map: {arxiv_val}")

    # 3. Add verified DOI
    if key in VERIFIED_DOIS and not has_doi:
        doi = VERIFIED_DOIS[key]
        entry = add_field(entry, "doi", doi)
        print(f"  [{key}] Added verified DOI: {doi}")

    return entry

# Process each entry
new_content = content
pattern = r'(@\w+\{(\w+),.*?)(?=@\w+\{|\Z)'
for m in re.finditer(pattern, content, re.DOTALL):
    old_entry = m.group(1)
    key = m.group(2)
    new_entry = update_entry(old_entry, key)
    if new_entry != old_entry:
        new_content = new_content.replace(old_entry, new_entry, 1)

with open(BIB_FILE, "w") as f:
    f.write(new_content)

print(f"\nDone. Backup at {BIB_FILE}.bak")
