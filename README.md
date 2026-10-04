# AI education imaginaries in Vietnamese news

Current data, methods and supplementary results for the study of sociotechnical imaginaries of AI in education.

## Current materials

- `data/final_analysis_dataset.csv`: current 917-article dataset, incorporating the 31 approved coding corrections across 26 articles.
- `data/article_texts_and_open_extraction.csv`: original article texts and structured extraction (1,098 records).
- `data/final_article_coding.xlsx`: frozen original coding and extraction-to-article linkage, retained for provenance. It predates the correction ledger; use the CSV for current analysis.
- `data/original_article_register.csv` and `data/outlet_classification.csv`: source register and outlet mapping.
- `methods/`: codebook, extraction prompt, collection notebooks and project milestones.
- `evidence/coding_corrections.csv`: cell-level changes, source evidence and reasons.
- `evidence/reconstruction_and_sources.md`: relationships supporting the six-imaginary reconstruction and consolidated source-reading records.
- `results/results.xlsx`: complete descriptive tables, outlet comparisons, leave-one-outlet-out ranges, yes-only and January-cutoff sensitivity, and within-generative-AI comparisons.
- `results/outlet_comparison.json`: machine-readable comparisons used by the figures; `results/validation.json`: input hashes and verification results.
- `results/figures/`: current SIPC comparison and actor-position figures.

## Reproduction

```sh
python3 -m pip install -r requirements.txt
python3 scripts/reproduce_results.py
```

The default output directory is the system temporary directory's `sipc-reviewed-results`. To refresh the repository results and figures:

```sh
python3 scripts/reproduce_results.py --output-dir results
python3 scripts/plot_results.py
```

Reproduction verifies the 31 corrections against the frozen workbook and calculates all 89 indicators from the current CSV. It does not rerun LLM extraction or regenerate qualitative interpretations. Indicator percentages use coded-field denominators; codes are nonexclusive. Outlet differences are public/central minus commercial/general. Leave-one-outlet-out ranges are sensitivity ranges, not confidence intervals. The main comparison includes 871 articles from 30 November 2022 onward (433 public/central; 438 commercial/general).

The six imaginaries are differentiated learning at scale; capable participation in an AI society; education as infrastructure for technological development; the integrated AI educational institution; equitable educational access; and credible learning and accountable judgment. Article-level indicator frequencies do not estimate imaginary prevalence. Source-reading records document a reading pool rather than full-corpus manual validation.

## Local files and history

The manuscript and reference library remain local and are excluded from GitHub. Superseded analysis, evidence, figures and supplements are stored under `archive/superseded_2026-10-04/`, also excluded from GitHub. Earlier published versions remain recoverable through Git history. The manuscript is reserved for separate publication.
