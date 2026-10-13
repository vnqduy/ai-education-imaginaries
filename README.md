# Educational AI futures in Vietnamese news

Final coding checkpoint: **14 October 2026**. The active codebook is **v2.3**, with SIPC’s six dimensions and twelve fields. The final corpus contains **1,081 original article IDs** and **3,004 attributed future arrangements**: 864 clear futures, 93 borderline cases, 107 adequate sources without an educational future, and 17 unresolved sources.

## IDs and corpus correction

`DOC_0001` etc. were sequential extraction-row identifiers, not the original article IDs. The historical linkage table at commit `bad2614` preserves original IDs such as `TTO17_000`. Those IDs are restored as the primary key throughout source, extraction, review, coding, account references and final CSV exports. The old extraction identifier remains in `legacy_extraction_id` for traceability.

The researcher instructed exclusion of **17 storage/linkage exceptions** from the 1,098-record working corpus: 15 without a supported original ID and two duplicate extractions pointing to `KEN26_021`. Both duplicate records were excluded. This is a **researcher-error exclusion**, not an assessment of educational futurity. It precedes substantive eligibility. The local crosswalk documents every retained and excluded row. Counts and outlet denominators were regenerated after exclusion; no retained source text, code or evidence locator changed.

## Current directory

| Path | Purpose | GitHub |
|---|---|---|
| `data/source_corpus.jsonl` | Retained full texts and metadata | Local only |
| `data/open_extraction.jsonl` | Uncategorised twelve-field extraction | Local only |
| `data/source_review.jsonl` | Source adequacy and interpretive limits | Local only |
| `data/hosted_publisher_flags.jsonl` | Producing-publisher uncertainty | Local only |
| `data/id_crosswalk.csv`, `provenance.json` | Original-ID linkage, exclusions and consolidated audit | Local only |
| `data/outlet_classification.csv` | Supplied exploratory outlet groups | Published |
| `data/sipc_future_coding/codebook.json`, `.md` | Frozen v2.3 definitions | Published |
| `data/sipc_future_coding/record_specification.json` | Coding schema | Published |
| `data/sipc_future_coding/coded_corpus.jsonl` | Authoritative linked coding and source evidence | Local only |
| `data/sipc_future_coding/coded_articles.csv`, `coded_accounts.csv` | Final inspectable coding exports | Local only |
| `data/sipc_future_coding/manifest.json` | Frozen input hashes and population | Local only |
| `methods/` | Extraction, coding and comparison protocols | Published |
| `results/` | Current aggregates, validation and checkpoint report | Published |
| `results/figures/` | Process figure | Published |
| `scripts/` | Validation, export, aggregation and process figure generation | Published |
| `manuscript/`, `ref/` | Authoring sources, deliverables and literature | Local only |

## Reproduction

From the repository root, with Python 3 and the private inputs restored:

```sh
python3 scripts/reproduce_results.py
```

The numerical pipeline uses the Python standard library. It validates complete ID coverage, frozen source/codebook hashes, code membership, account structure and evidence locators; exports private article/account CSVs; and regenerates public distributions and outlet comparisons. It does not rerun extraction or recreate semantic coding. `scripts/plot_process.py` separately requires ReportLab.

The **article is the unit of analysis**. Main counts use codes present in any linked arrangement, once per code per article; primary-account counts are a prominence sensitivity. Article-level MISSING means no linked arrangement assigns a substantive code in that field. Multiple codes can occur, so percentages need not sum to 100%. Relations among speakers, evaluations, roles and responsibilities are interpreted within linked arrangements, not manufactured from article-level unions.

The main outlet comparison uses clear futures without producing-publisher flags. Sensitivities include borderline cases, all supplied host groups, complete sources, individual-outlet concentration, leave-one-outlet-out ranges and common-year standardisation. The two outlet groups are exploratory labels, not causal measures of state or market control. Constituent frequencies do not measure imaginary prevalence or public acceptance.

## Cleanup and limitations

The active folder contains one codebook, one authoritative coding corpus and one set of current aggregates. Superseded coding, batch parts, worker scripts, drafts, old result snapshots and build caches were removed after preserving the final records and compact audit trail. Authoring sources and reference originals remain. The manuscript has not been substantively revised at this checkpoint.

Assistant source review and automated checks establish traceability and structural consistency, not independent human intercoder reliability. Excluding storage errors does not remove all incomplete sources: 17 retained original-ID articles remain unresolved on source adequacy.

Full texts and coded research records are excluded from new Git commits. Previously published history is not rewritten by this cleanup.
