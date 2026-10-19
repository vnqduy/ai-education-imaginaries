# Educational AI futures in Vietnamese news

**Work in progress.** This repository is a working space for exploring the data and refining the method. The codebook, coding decisions, sample definitions, analyses and manuscript are provisional and may change.

## Working files

- `data/`: source articles, extraction, source review and metadata.
- `data/sipc_future_coding/`: current coding, codebook and validation specifications.
- `results/article_coding.csv`: article-level data for analysis in R.
- `scripts/`: CSV reproduction, validation and plotting.
- `methods/`: working extraction and coding protocols.
- `manuscript/`: draft manuscript and supporting files.
- `ref/`: local reference literature.

## Using the data

The current CSV has 1,081 articles and 99 columns; `main_sample == 1` selects 828 articles. Code columns use 1/0 for observed presence/absence and blanks for missing coding. The current taxonomy has eight rationale domains and ten actor categories shared by speaker, affected entities and responsibility. Categories can overlap. Article-level co-occurrence does not establish a relationship within the same account; consult `coded_corpus.jsonl` for linked evidence.

Rebuild the CSV from the current coding:

```sh
python3 -B scripts/reproduce_results.py
```

For figures, run `scripts/plot_future_roles.R` in R with tidyverse, jsonlite and patchwork installed. Validation checks structure and evidence references, not interpretive validity.

Replace current working files in place. Delete intermediate outputs, superseded exports and unused derivatives; do not keep dated copies, parallel old/new results or separate decision-proof files. Retain source materials, reproducible inputs and only the latest requested deliverables. Inherit existing coding and source evidence. Git history preserves tracked revisions; the local-only `manuscript/` and `ref/` directories are excluded from commits and pushes. Problematization uses linked role–rationale–action (see the coding protocol).

## Manuscript exports

The main manuscript and appendix support both PDF and editable Word from the same QMD source:

```sh
quarto render manuscript/manuscript.qmd --to all
quarto render manuscript/appendix.qmd --to all
```

See `manuscript/format/README.md` for LMT requirements, individual export commands, dependencies, and outstanding author declarations.
