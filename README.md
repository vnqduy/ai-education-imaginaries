# Educational AI futures in Vietnamese news

Final checkpoint: **14 October 2026**, frozen **v2.3**. The corpus contains **1,081 unique original article IDs** and **3,004 attributed future arrangements**: 864 clear futures, 93 borderline cases, 107 adequate sources without an educational future, and 17 unresolved sources.

## IDs and population

`DOC_…` was an extraction-row identifier. Original article IDs such as `TTO17_000` were restored from matched entries in the historical linkage table at commit `bad2614`. The researcher instructed removal of 17 storage/linkage errors: 15 unlinked records and both duplicate extractions of `KEN26_021`. This researcher-error exclusion precedes substantive eligibility. Retained text, codes and evidence were unchanged. Compact provenance preserves the exclusions and source-recovery history. The former row-ID column and crosswalk have been removed.

## Minimal directory

- `data/`: published source, extraction, adequacy review, publisher flags, compact provenance and outlet classification.
- `data/sipc_future_coding/`: one authoritative `coded_corpus.jsonl`, hash manifest, frozen human/machine-readable codebook and record specification.
- `methods/`: extraction prompt and consolidated coding/interpretation protocol.
- `results/`: **one rectangular dataframe, `article_coding.csv`**, and the public vector process figure `figures/process.svg`.
- `scripts/`: `reproduce_results.py` and `validate_future_coding.py` only.
- `manuscript/`: editable manuscript sources and bibliography/style dependencies, local only. The existing manuscript has not yet been rewritten for this checkpoint.
- `ref/originals/`: original literature files, local only.

Old aggregate JSONs, per-account exports, worker logs, snapshots, progress/validation reports and redundant figure exports are absent and are not recreated by the pipeline.

## Rectangular dataframe for R

`results/article_coding.csv` has **1,081 rows and 91 columns**. Each row represents one article; every cell is a scalar, with no JSON/list columns or copied source passages.

| Columns | Meaning |
|---|---|
| `article_id` | Unique original article key |
| `title`, `date`, `year`, `url` | Source metadata; date is ISO YYYY-MM-DD |
| `outlet_domain`, `outlet_name`, `outlet_group` | Supplied publication-host metadata and exploratory group |
| `publisher_uncertain` | 1 if producing publication is flagged as uncertain |
| `eligibility`, `source_adequacy` | Educational-future eligibility and separate source-quality status |
| `account_count`, `codebook_version` | Number of linked arrangements and applied definitions |
| `main_sample` | 1 for clear futures without producing-publisher uncertainty; 828 articles |
| 65 `field__CODE` columns | Code presence in any linked arrangement, once per article |
| 12 `field__missing` columns | 1 when no substantive code is assigned in that field for an eligible article |

Code values are **1=present, 0=absent in an observed field**. If an eligible article has no substantive code in a field, all its code columns in that field are blank/NA and its missing indicator is 1. Noneligible and unresolved articles have NA in all coding and missing-indicator columns, rather than being represented as substantive zeros. The eligibility column preserves that distinction.

Multiple codes are allowed. Positive and negative can both equal 1 when different linked arrangements in an article receive different evaluations. Article-level unions do not establish that codes belong to the same speaker or future; relational interpretation returns to `coded_corpus.jsonl`. A field without an assigned code does not establish absence of all possible purposes in the text.

```r
d <- read.csv("results/article_coding.csv",
              fileEncoding = "UTF-8", na.strings = "",
              check.names = FALSE, stringsAsFactors = FALSE)
main <- d[d$main_sample == 1, ]
```

Choose denominators deliberately: excluding NA gives the observed-field denominator; filtering by eligibility or main_sample defines the analytic corpus. The primary outlet comparison excludes producing-publisher uncertainty. Borderline, source-quality, host-group, outlet-concentration and temporal sensitivities can be calculated in R from the same dataframe. The group labels do not establish causal state/market effects; constituent frequencies do not measure imaginary prevalence or public acceptance.

## Reproduction and publication

With Python 3, after cloning this repository, run from the repository root:

```sh
python3 -B scripts/reproduce_results.py
```

The pipeline uses only the standard library. It validates complete coding coverage, frozen source/codebook hashes, code membership, linked structures and evidence locators, then writes only the CSV. It checks CSV rectangularity, uniqueness and exact value round-trip. The exported file was also successfully imported and checked using R. It does not rerun extraction or semantic coding. Assistant review and automatic checks do not establish independent human intercoder reliability.

The author authorised publication of all research data on 14 October 2026. GitHub now includes full retained texts, extraction, source review, publisher flags, coded records, provenance/hash manifest and the R-ready dataframe, along with definitions, methods, scripts and process figure. Manuscript authoring files and external literature remain local. Previously published Git history has not been rewritten.
