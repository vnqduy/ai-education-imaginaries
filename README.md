# Educational AI futures in Vietnamese news

**Work in progress.** This repository is a working space for exploring the data and refining the method. The codebook, coding decisions, sample definitions, analyses and manuscript are provisional and may change.

## Working files

- `data/`: source articles, extraction, source review and metadata.
- `data/sipc_future_coding/`: current coding, codebook and validation specifications.
- `results/article_coding.csv`: article-level data for analysis in R.
- `scripts/`: CSV reproduction, validation and plotting.
- `methods/`: working extraction and coding protocols.
- `manuscript/`: current manuscript source, references, formatting and writing guidance.
- `supplementary/`: one supplementary document containing full profiles, sensitivity checks, screening details and AI documentation.
- `ref/`: local reference literature and original presentation/workbook inputs; excluded from Git.

## Using the data

The current CSV has 1,081 articles and 99 columns; `main_sample == 1` selects 828 articles. Code columns use 1/0 for observed presence/absence and blanks for missing coding. The current taxonomy has eight rationale domains and ten actor categories shared by speaker, affected entities and responsibility. Categories can overlap. Article-level co-occurrence does not establish a relationship within the same account; consult `coded_corpus.jsonl` for linked evidence.

Rebuild the CSV from the current coding:

```sh
python3 -B scripts/reproduce_results.py
```

For figures, run `scripts/plot_future_roles.R` in R with tidyverse, jsonlite and patchwork installed. Validation checks structure and evidence references, not interpretive validity.

Replace current working files in place. Delete intermediate outputs, superseded exports and unused derivatives; do not keep dated copies, parallel old/new results or separate decision-proof files. Retain source materials, reproducible inputs and only the latest requested deliverables. Inherit existing coding and source evidence. Git history preserves manuscript, supplementary and research-source revisions. Only `ref/` stays local. Problematisation uses linked role–rationale–action (see the coding protocol). Generated exports and intermediate files are excluded from Git; retain only current requested deliverables.

## Manuscript exports

The main manuscript and supplementary document support both PDF and editable Word from the same QMD source:

```sh
quarto render manuscript/manuscript.qmd --to all
quarto render supplementary/supplementary.qmd --to all
```

See `manuscript/format/README.md` for LMT requirements, individual export commands, dependencies, and outstanding author declarations.
