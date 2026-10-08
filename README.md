# AI education imaginaries in Vietnamese news

Checkpoint: **8 October 2026**. This is the current full-corpus, future-centred SIPC analysis. It supersedes the earlier 917-article analysis and six-imaginary classification.

## Current findings and scope

All **1,098 articles** have been coded with the user-approved **v1.1 codebook**: 845 clear educational futures, 103 borderline cases, 122 without a supported educational future and 28 unresolved because of inadequate sources. There are **1,850 attributed future accounts**; account identity is `(ID, account_id)`.

Applying the SIPC framework is already analysis of imaginaries in public communication. Further interpretation examines the relations between educational futures, evaluations, speakers, justifications and proposed actions. A separate named typology is optional. Code frequencies are constituent measures, not estimates of imaginary prevalence or public acceptance.

The primary outlet comparison includes 421 public/central and 387 commercial/general clear-future articles, excluding producing-publisher uncertainty. Public/central coverage more often foregrounds capabilities, institutional organisation, public-authority voices, curriculum and collaboration. Commercial/general coverage more often foregrounds cognition/agency, learner voices and negative evaluations. Both groups predominantly articulate positively evaluated futures. The supplied groups support exploratory comparison; they do not directly measure ownership or political/market control.

See [checkpoint report](results/checkpoint_report.md) for findings, methodological clarification, sensitivities and limitations. Source-based comparative interpretation remains ongoing; the current checkpoint does not claim a final typology or causal explanation.

## Working set and publication scope

Full-text sources, raw extraction, source review, publisher flags, consolidated provenance and coded article/account records are **local only** and excluded from GitHub. GitHub publishes the codebook, methods, scripts, outlet mapping and aggregate results. The table below documents both local inputs and published materials.

| Location | Purpose |
|---|---|
| `data/source_corpus.jsonl` | Effective retained texts and metadata for all original IDs, including eight recovered-source replacements |
| `data/open_extraction.jsonl` | Final effective, uncategorised extraction of the twelve SIPC fields |
| `data/source_review.jsonl` | Source adequacy, review reasons and interpretive limits for each ID |
| `data/provenance.json` | Local consolidated recovery, semantic amendment and audit history |
| `data/outlet_classification.csv` | Supplied exploratory outlet-group mapping |
| `data/hosted_publisher_flags.jsonl` | Fifty records with producing-publisher uncertainty; 37 are clear-future articles |
| `data/sipc_future_coding/codebook.json` and `.md` | Frozen v1.1 definitions and readable documentation; introductory clarification does not alter codes |
| `data/sipc_future_coding/record_specification.json` | Article/account structure |
| `data/sipc_future_coding/coded_corpus.jsonl` | Authoritative coding, attributed accounts, evidence, mechanisms and qualifications |
| `data/sipc_future_coding/coded_articles.csv` and `coded_accounts.csv` | Final tabular exports; article codes describe the primary account |
| `methods/` | Extraction prompt, coding protocol, interpretation guidance and publisher-attribution note |
| `results/` | Consolidated report, corpus distributions, outlet comparisons/sensitivity, validation and checkpoint hashes |
| `scripts/` | Validation and reproduction from final inputs |

## Reproduction

Run from the repository root with Python 3; no third-party packages are required. A GitHub clone requires the local research inputs listed above to be restored at their documented paths before reproduction can run:

```sh
python3 scripts/reproduce_results.py
```

This validates the corpus, verifies the approved codebook hash, regenerates CSV exports and produces `results/validation.json`, `results/corpus_summary.json` and `results/outlet_comparison.json`. It does not rerun model extraction, recreate qualitative coding or rewrite the interpretive report. The checkpoint manifest records hashes of the final artifacts at this checkpoint.

Primary comparisons use clear futures without hosted-publisher flags. Other scenarios include borderline futures, all supplied host groups, and complete sources. Outlet comparisons also record individual-outlet concentration, year composition and leave-one-outlet-out ranges. Selected contrasts have any-account article-presence and pooled-year standardisation sensitivities for 2023–2026. These are descriptive checks, not confidence intervals or causal estimates. Multi-coded proportions need not sum to 100%.

Structural checks do not measure independent intercoder agreement. Targeted source/semantic audits and recovery history are consolidated in local `data/provenance.json`. Positivity concerns each account's specified future, including protective restrictions, rather than general approval of AI.

## Cleanup and local materials

The obsolete archive has been deleted after consolidating 28 audit/recovery records into local `data/provenance.json` and retaining 27 original literature files in `ref/originals/`. Batch outputs, duplicate datasets, worker scripts, old manuscripts, old figures and caches are removed. The current manuscript and reference texts remain intact.

The cleanup removed 606 archive files (165,675,824 bytes before retaining literature/audit essentials). Pipeline reproduction passed afterward with 1,098 articles, 1,850 accounts and zero structural errors; authoritative coding, CSV exports and aggregate results retain their checkpoint hashes. Historical paths inside provenance records describe the earlier workflow and do not indicate current dependencies.

`manuscript/`, `ref/`, source records, extraction, coded research data and provenance remain local and excluded from GitHub. GitHub contains documentation and aggregate outputs. Full-data commit `5530233` is retained only on local branch `codex/local-data-checkpoint-2026-10-08`. Data removed from the current GitHub tree remain in already-published Git history; this cleanup does not rewrite that history. The manuscript has not been revised.

## Framework references

- Brause et al. (2025), [Sociotechnical imaginaries and public communication](https://doi.org/10.1177/13548565251338192).
- Richter et al. (2025), [Negotiating AI(s) futures](https://jcom.sissa.it/article/pubid/JCOM_2402_2025_A08/).
