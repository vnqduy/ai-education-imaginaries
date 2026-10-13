# Educational AI futures in Vietnamese news

Final checkpoint: **14 October 2026**, frozen **v2.3**. The corpus contains **1,081 unique original article IDs** and **3,004 attributed future arrangements**: 864 clear futures, 93 borderline cases, 107 adequate sources without an educational future, and 17 unresolved sources.

## IDs and population

`DOC_…` was an extraction-row identifier. Original article IDs such as `TTO17_000` were restored from matched entries in the historical linkage table at commit `bad2614`; `legacy_extraction_id` preserves the former row key. The researcher instructed removal of 17 storage/linkage errors: 15 unlinked records and both duplicate extractions of `KEN26_021`. This researcher-error exclusion precedes substantive eligibility. Retained text, codes and evidence were unchanged. The private crosswalk and compact provenance preserve the correction and recovery history.

## Minimal working directory

- `data/`: private source, extraction, adequacy review, publisher flags, original-ID crosswalk and compact provenance; public outlet classification.
- `data/sipc_future_coding/`: one authoritative private `coded_corpus.jsonl`, private hash manifest, frozen codebook in human/machine-readable forms and record specification.
- `methods/`: extraction prompt and consolidated coding/interpretation protocol.
- `results/`: **only** `corpus_summary.json`, `outlet_comparison.json` and the final vector process figure `figures/process.svg`.
- `scripts/`: **only** `reproduce_results.py` and `validate_future_coding.py`.
- `manuscript/`: editable manuscript sources and bibliography/style dependencies, local only. The existing manuscript has not yet been rewritten for this checkpoint.
- `ref/originals/`: original literature files, local only.

No batch directories, worker scripts, old coding snapshots, CSV copies of the coded corpus, validation/progress reports, separate checkpoint reports, redundant figure exports, old presentation products or extracted reference-text copies are retained. They are not recreated by the pipeline.

## Reproduction

With Python 3 and the private inputs restored, run from the repository root:

```sh
python3 -B scripts/reproduce_results.py
```

The pipeline uses only the standard library. It checks complete coverage, frozen source/codebook hashes, code membership, linked account structure and source locators, then regenerates the two aggregate JSON files. Validation is reported to the console rather than saved as a secondary artifact. It does not rerun extraction or semantic coding.

The **article is the unit of analysis**. Main counts use code presence in any linked arrangement, once per code per article. Primary-arrangement counts and pooled arrangement counts remain supplementary measures inside the same aggregate files, not separate products. Multiple codes are allowed. Article MISSING means no arrangement assigns a substantive code in that field. Relational interpretation returns to linked arrangements, never joining unrelated voices from article-level unions.

The primary outlet comparison uses clear futures without producing-publisher flags. The comparison file also retains borderline, source-quality, host-group, outlet-concentration and common-year sensitivities needed to assess descriptive contrasts. Groups do not measure causal state/market effects; constituent frequencies do not measure imaginary prevalence or public acceptance. Assistant review and automatic checks do not establish independent human intercoder reliability.

GitHub contains only definitions, methods, scripts, outlet classification, aggregate results and the process figure. Full texts, coded records, crosswalk/provenance, authoring files and literature remain local and ignored. Previously published Git history has not been rewritten.
