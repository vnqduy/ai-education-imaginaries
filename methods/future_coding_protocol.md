# Future-centred SIPC coding protocol

Completed v2.3 checkpoint, 14 October 2026. Definitions: [codebook](../data/sipc_future_coding/codebook.md); twelve-field structure: [record specification](../data/sipc_future_coding/record_specification.json).

## Corpus and source preparation

The working set contained 1,098 extraction records. `DOC_…` identifiers indexed extraction rows. Original article IDs were restored using matched entries in the historical linkage table at Git commit `bad2614`. At the researcher's instruction, 15 unlinked records and two duplicate extractions pointing to one original ID were excluded as researcher storage/linkage errors. The final population is 1,081 unique original IDs. This correction is separate from educational-future eligibility; all aggregate denominators were regenerated. The compact provenance records storage exclusions by original article ID where available and source title/URL; former row identifiers and the crosswalk were removed at the author request.

Structured extraction preceded category development and recorded all twelve SIPC fields without applying the later categories. Source adequacy was assessed separately from educational futurity. Recovery replaced retained text only for the same article, with documented retrieval and fresh extraction. A tag page, missing body or absent video transcript is an unresolved source, not substantive absence. Scraped menus, related-story teasers and unrelated promotional material were excluded from interpretation.

## Codebook and semantic application

The codebook was developed after full-corpus extraction, considering negative and borderline cases. A 16-article assistant boundary pilot and coordinator review addressed goals versus applications, prescription versus certainty, delivery setting versus affiliation, explicit timing and geography, actor attribution and distinct evaluation targets. Version 2.3 consolidated future role into six goal/outcome families. The 230 records previously completed under v2.2 received source-based future-role-only revision; preservation checks confirmed their other eleven fields and account structure were unchanged. Remaining records received full-source v2.3 coding. Old thematic labels were not translated into new categories.

All 1,098 working records were read against full retained source, raw extraction and source-adequacy review in 55 disjoint batches, before the original-ID storage correction. A projected or normatively desired educational arrangement involving AI is eligible. A current example can embody such an arrangement when the source articulates its desired role or direction. General AI adoption, model performance, unrelated product futures or university affiliation alone do not establish an educational future.

The article is the unit of analysis; attributed future statements or arrangements are coding units within it. One prominent arrangement is marked primary, with materially distinct voices or alternatives retained separately. Each contains all twelve fields, a future statement, speaker, evaluation target, qualification, propositions, literal details and linked evidence. Multiple substantive codes per field are allowed when independently supported. Missing information remains MISSING; an unstated goal is not inferred from an application's ordinary benefits. Uncovered purposes remain literal rather than being forced into a family.

Future-role families accommodate sought, expected and feared outcomes. Desirability evaluates the specified arrangement, not AI in general. Protective restrictions may be desired while the harm they prevent is negative. Mixed evaluation requires benefits and harms of the same target; disagreement between separate speakers is not mixed evaluation. No artificial positive/negative balance was imposed. Timing, geography, confidence and responsibilities require source support rather than inference from dates, affiliations, intentions or identities.

## Evidence, validation and comparison

After the author checked evidence quality, new records stored retained-source character offsets instead of additional copied quotations. Earlier exact quotations were preserved. The coordinator performed targeted source checks and resolved attribution and boundary ambiguities. Automated validation checks hashes, unique complete IDs, code membership, twelve-field completeness, primary consistency, proposition links and exact quotes or valid nonempty source bounds. It establishes structural traceability, not interpretive accuracy or independent human agreement. Original-ID restoration preserved retained text, codes and evidence; final validation passed after cleanup.

Main distributions use the union of supported codes across linked arrangements, counting each code once per article. Article MISSING means no arrangement assigns a substantive code in that field. Primary-arrangement counts are a prominence sensitivity, and pooled arrangement counts are supplementary. Article-level unions describe presence only: relational interpretation returns to linked statements and never joins unrelated actors and evaluations into a synthetic future.

The primary outlet comparison uses clear futures without producing-publisher uncertainty. Sensitivities add borderline cases, all supplied host groups and complete sources, and examine outlet concentration, leave-one-outlet-out ranges and common-year standardisation. Groups describe exploratory institutional settings, not causal ownership/control effects or independence from state supervision. Applying SIPC analyses articulated imaginaries; marginal constituent counts alone do not reconstruct their relations or require a separate named typology.

On 14 October 2026, the author authorised publication of all research data, including full texts, extraction, coding, provenance and the rectangular dataframe, together with definitions, methods, scripts, outlet classification and the process figure.

## Relational interpretation and publication attribution

Reconstruct educational ordering through linked purposes, roles, speakers, evaluations, justifications, actions and responsibilities. Demonstrate those relations within sources and inspect contrary cases. A shared application can support competing educational futures; different applications can support a shared purpose. Distinguish recurrent syndicated or press-release narratives from independently articulated positions. Do not infer public acceptance, institutional stabilisation or material enactment solely from news recurrence.

Some supplied URL hosts carry pages naming another producing publication. Route flags do not by themselves establish political or market classification. Preserve source metadata; keep flagged articles in full-corpus analysis, but omit unresolved producing-publication cases from the primary institutional comparison. The all-host-groups scenario provides descriptive sensitivity. Differences by URL host must not be described automatically as editorial-origin effects.

## Rectangular dataframe for R

The sole analysis export is `results/article_coding.csv`: one row per retained article, with scalar metadata and binary columns named `field__CODE`. Codes are unioned across linked arrangements, once per article. When an eligible article has no substantive code assigned in a field, its code columns are NA and `field__missing` is 1. Observed fields have 0/1 code values and missing 0. Noneligible or unresolved articles have NA for all code and missing columns; eligibility preserves why. Positive and negative columns can both be 1 for distinct arrangements in one article. These unions do not imply account-level co-occurrence.

`main_sample=1` identifies clear-future articles without producing-publisher uncertainty. Dates use ISO YYYY-MM-DD; year is integer. UTF-8 CSV blanks represent NA. The standard-library exporter validates the source coding and serialization; the saved dataframe was also imported and checked in R. Counts, contrasts and sensitivity statistics are performed downstream in R rather than emitted as parallel JSON products.
