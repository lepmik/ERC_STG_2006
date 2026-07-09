# ERC Starting Grant 2026 — FIND

Grant proposal project (LaTeX), not a software project. PI: Mikkel Elle Lepperød,
Simula Research Laboratory. Proposal: **FIND — Flexible Intelligence through
Neurocomputational Design** (PAM architecture: temporal predictive coding +
distributed Kanerva/HDC memory + active inference). Panel PE6, 60 months,
€1.5M base + additional compute funding.

## Layout

- `grant_proposal/` — LaTeX sources. Content lives in:
  - `00-coverpage.tex` — cover page + abstract
  - `01-part-I.tex` — B1 Part I of the Scientific Proposal (**max 5 pages**, references excluded)
  - `02-cv-trackrecord.tex` — B1 CV & track record (**max 4 pages**)
  - `03-part-II.tex` — B2 Part II: methodology, WPs, Gantt, risks, collaborations, Funding ID (**max 7 pages**, references + Funding ID excluded)
- Three build targets: `main_B1.tex` (submission PDF for B1), `main_B2.tex`
  (submission PDF for B2), `main.tex` (combined B1+B2 with per-part `refsection`s,
  for internal review only).
- `references.bib` is the canonical bibliography. `references_*.bib`,
  `*.bib.bak`, `*.bib.updated` are stale backups — do not edit or cite from them.
- `figures/` — TikZ figures each with own `.tex` (compiled to PDF and included);
  `graveyard/` — discarded material.
- `knowledge_base/` — call requirements. Start with
  `ERC_StG_2026_Requirements_Synthesis.md`; `md_converted/` holds markdown
  conversions of the official ERC PDFs in the repo root (work programme,
  information for applicants, evaluation rules, and the successful WoMBaM
  example proposal).
- `feedback/erc_stg_review_feedback.md` — simulated PE6 panel review of an
  earlier draft; most must-fix items have since been addressed.

## Build

```sh
cd grant_proposal
latexmk -pdf -interaction=nonstopmode main_B1   # B1 (cover + Part I + CV)
latexmk -pdf -interaction=nonstopmode main_B2   # B2 (Part II)
```

Uses biber (biblatex). Aux/log/bbl files are build products — never hand-edit.

## Rules that matter when editing

- ERC formatting is strict: ≥11pt font, single line spacing (`\setstretch` must
  stay at 1.0), 2 cm side margins, header "Lepperød — FIND — Part B1/B2".
  Page limits are hard; check page counts after any content change.
- B1 and B2 are submitted as **separate standalone PDFs**. `03-part-II.tex` must
  not `\ref` labels defined in Part I files (e.g. `fig:prelim`) — in the
  standalone B2 build they resolve to "??". Refer to Part I content textually
  ("Part I, Fig. 2") instead.
- Step 1 evaluators see only B1 (Part I + CV); Part I must stay self-contained.
- Do not report results from `predictive_active_modular_time` /
  `subspace_reasoning` repos beyond what is already in the text (PI marked them
  too preliminary); tPC-KM, CORe50, and PAMNCA/ARC results are approved.
- Terminology: the architecture is always "PAM" (never "PM"); the project is
  `\project` (FIND).
