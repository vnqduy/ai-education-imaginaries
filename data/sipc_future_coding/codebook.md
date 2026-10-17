# SIPC codebook v3.2 — five future roles

Updated 17 October 2026. Five future roles retained; speaker, responsibility and affected_entities now share ten non-exclusive actor categories.

## AI as a Learning Partner

`FR_LEARNING_PARTNER`

AI will transform learning into a more personalized and collaborative process.

AI changes the learning process, learner development, and relationships among learners, teachers and AI.

**Include:** Tutoring, personalization, collaborative learning, teacher instructional support, and development or erosion of understanding, creativity, autonomy and practical learning. Includes explicit loss of learning-by-doing through AI automation.

**Exclude:** Formal assessment/recognition alone; institutional administration; learning about AI alone; job displacement without an articulated learning consequence.

**Boundary:** Lesson preparation and learning feedback belong here; assessment validity, grades, integrity and recognized competence belong to educational judgment. A feared loss of thinking can belong here without endorsing AI as a good partner.

## AI as a Force Reshaping Educational Judgment

`FR_EDUCATIONAL_JUDGMENT`

AI will change how educational achievement, integrity, and competence are assessed and recognized.

AI changes assessment, academic integrity, authenticity, and recognition of educational achievement or competence.

**Include:** Grading, examination and assessment redesign, cheating/authorship, credential recognition and the validity or fairness of educational judgments.

**Exclude:** Routine administration, behaviour monitoring without competence/achievement judgment, and formative learning help without assessment/recognition stakes.

**Boundary:** Generating or evaluating assessed work is different from supporting learning. An AI-subject competition alone is not a change in educational judgment.

## AI as an Educational Management Tool

`FR_EDUCATIONAL_MANAGEMENT`

AI will make educational institutions more efficient, data-driven, and responsive.

AI changes educational operations, administration, institutional services, monitoring and resource allocation.

**Include:** Administrative workload, attendance, institutional data use, admissions information services, resource planning and school safety/monitoring. Include dysfunctions or contested control within these arrangements.

**Exclude:** Learner competence assessment; pedagogical preparation alone; policies governing AI adoption without a specified AI-enabled operational function.

**Boundary:** Distinguish AI used for educational management from management of AI implementation. A school or ministry as actor does not by itself establish this role.

## AI Literacy as an Educational Imperative

`FR_AI_LITERACY`

Education must prepare people to live, learn, and work responsibly in an AI-driven world.

Education prepares people to understand, develop, critically use and live or work with AI.

**Include:** AI knowledge and curricula; ethical/critical AI use; educator AI competence; specialist AI formation and professional preparation explicitly oriented to an AI-driven world.

**Exclude:** Using AI merely to improve an existing learning process; automation/job loss without an educational preparation response; collective development inferred only from an institution or country name.

**Boundary:** The object of formation is people’s AI-related understanding/capacity. Individual AI study can fit; a national-development motive is not assumed. If training is only the mechanism of a stated collective goal, do not automatically add this code.

## AI as a Driver of National Development

`FR_NATIONAL_DEVELOPMENT`

AI education will strengthen the workforce, technological capabilities, and national development.

AI-related education or university research serves an explicitly articulated collective, sectoral or national development purpose.

**Include:** Collective workforce formation, sectoral technological capacity, national innovation/competitiveness, technological sovereignty, and explicit wider societal development. Retain the actual country/sector and any feared consequence.

**Exclude:** Individual employability or study aspirations alone; institutional prestige/ranking alone; national location, state affiliation, policy name, or cultural subject matter without an articulated collective development purpose.

**Boundary:** Require the collective/sectoral/national end in the account and source. Workforce demand may justify a sectoral workforce goal; it does not turn every individual career aspiration into national development.

## Context and desirability

Interpret future_role from the future being evaluated, not from whether the account endorses it. Use inherited open extraction and attributed account statements first. A warning, safeguard, implementation condition or evaluation may receive the role of its clearly identified target in the same source. Require a demonstrable shared referent (the same programme, tool, arrangement or continuing attributed argument). Record the contextual link and exact source anchors in the account. Do not transfer another speaker’s evaluation, certainty or intention, or assign all roles in the article. Generic policy, risk or market claims without an identifiable role remain MISSING. The contextual role revision preserved the five definitions; the subsequent v3.2 actor harmonisation is documented below. Desirability records positive, negative, mixed and undecided evaluation. No sixth role or separate positive/negative role subcodes are used.

The current corpus contains the decisions, source anchors and reasons. Git manages file history; there is no separate pilot, backup corpus or decision-ledger directory. Earlier descriptive literal_details are preserved; current future_role codes and missing_notes supersede historical classification comments.

## Other fields

### certainty

How firmly does the speaker claim that the specified future will or can occur?

- `CERT_CONFIDENT` — Confident prediction: The speaker presents the future outcome as a firm expectation.
- `CERT_POSSIBLE` — Possible outcome: The speaker presents an outcome or capability as possible, probable or potential without assuring its occurrence.
- `CERT_DENIED` — Denied outcome or capability: The speaker explicitly rules out a specified future outcome or capability.
- `CERT_UNRESOLVED` — Explicitly unresolved outcome: The speaker explicitly withholds a prediction or states that an outcome cannot yet be determined.

### desirability

How does this speaker evaluate this particular future arrangement?

- `DES_POSITIVE` — Desirable: The speaker positively values the specified future.
- `DES_NEGATIVE` — Undesirable: The speaker negatively values the specified future.
- `DES_MIXED` — Explicitly mixed: One speaker explicitly weighs desirable and undesirable effects of the same future arrangement.
- `DES_UNDECIDED` — Value explicitly undecided: The speaker explicitly leaves the educational desirability of the future open.

### rationale

What explicit reason, need or value explains why this goal or arrangement is desirable or undesirable?

- `RATION_PEDAGOGY` — Learning quality: A learning mechanism or pedagogical principle warrants the future.
- `RATION_CAPACITY` — Operational feasibility and efficiency: Educational provision is justified or constrained by staffing, time, infrastructure, cost or implementation capacity.
- `RATION_ECONOMY` — Employment and economic returns: Expected employment, occupational demand, income or commercial returns warrant the future.
- `RATION_EQUITY` — Equality of opportunity: Fair distribution of educational opportunity warrants the future.
- `RATION_RIGHTS_INTEGRITY` — Rights, reliability and academic integrity: Protecting rights, trustworthy information, authentic achievement or fair adjudication warrants the future.
- `RATION_HUMAN_VALUES` — Human, civic and cultural values: Human flourishing, dignity, empathy, democratic life, civic responsibility or cultural expression warrants the future.
- `RATION_NATIONAL` — National development and strategic autonomy: The future is warranted by an explicit collective national-development, competitive-position or sovereignty objective.
- `RATION_POLICY` — Policy or standards compliance: Alignment with a named policy, formal standard or official requirement itself warrants the future.

### technology_object

What technical form of AI is explicitly implicated in the future?

- `OBJ_GENERATIVE` — Generative AI: AI is explicitly identified as a generative model/system producing new text, images, audio, video, code or other content.
- `OBJ_PREDICTIVE` — Predictive or discriminative AI: AI is explicitly identified as a non-generative system that classifies, scores, predicts, detects or recognises patterns in supplied data.
- `OBJ_UNSPECIFIED` — AI form unspecified: The source identifies AI but provides insufficient information to distinguish its model/system family.

### education_context

In what educational sector or setting is the future located?

- `CTX_SCHOOL` — School education: The future is located in early-childhood, primary or secondary education.
- `CTX_HIGHER` — Higher education: The future is located in university or other explicitly tertiary education and its academic institutions.
- `CTX_VOCATIONAL` — Vocational education: The future is located in an explicitly vocational education or training programme/institution.
- `CTX_PROFESSIONAL` — Professional and workplace development: The future is located in continuing preparation or development of people acting in occupational roles.
- `CTX_COMMUNITY` — Community and informal education: The future is located in non-occupational community education or explicitly informal self-education.

### timespan

How does the source characterise the proximity or continuity of the educational future, and what exact horizon does it supply?

- `TIME_IMMEDIATE` — Immediate / being realised: The future arrangement is explicitly being implemented or realised at the source’s reference time.
- `TIME_NEAR` — Near-term: The source explicitly characterises the future as near, soon or short-term.
- `TIME_DISTANT` — Distant / long-term: The source explicitly characterises the future as distant or long-term.
- `TIME_ONGOING` — Ongoing / continuous: The future is framed as a continuing or recurrent educational process rather than a target completed at a horizon.
- `TIME_ANCHORED_UNCLASSIFIED` — Explicit horizon; proximity unstated: A date, quantified interval or stage anchors the future, but the source does not characterise its proximity or continuity.

### space

Which country or cross-border arena is explicitly the intended reach of the educational future?

- `SPACE_VIETNAM` — Vietnam: The future explicitly applies within Vietnam.
- `SPACE_FOREIGN_DOMESTIC` — Specific foreign country: The future explicitly applies within a named country other than Vietnam.
- `SPACE_TRANSNATIONAL` — Cross-national or global: The future explicitly spans countries or is intended for a regional/worldwide educational arena.

### speaker

Who articulates this future, and in which evidenced capacities? Use the shared actor categories below; multiple codes are allowed.

### affected_entities

Who explicitly experiences the consequences of this future? Use the shared actor categories below; multiple codes are allowed.

### action

What concrete intervention or restraint is proposed to pursue or prevent the future?

- `ACT_CURRICULUM` — Change curriculum content or credentials: Actors change what is formally taught, required or recognised in a programme.
- `ACT_PRACTICE` — Change learning, teaching or assessment practice: Actors change how educational activities or learner evaluation are conducted.
- `ACT_RESOURCES` — Provide resources or implementation capacity: Actors obtain or supply the people, training, funding, equipment or services required for implementation.
- `ACT_RULES` — Set rules, safeguards or restrictions: Actors establish/enforce permissions, obligations, protections or prohibitions.
- `ACT_COORDINATE` — Establish coordination or partnerships: Actors create a specified joint arrangement for implementing or governing the future.
- `ACT_EVALUATE` — Evaluate the AI intervention: Actors produce or use evidence to decide whether an AI-related educational intervention should proceed or change.

### responsibility

Who is explicitly assigned action, intervention or accountability? Use the shared actor categories below; multiple codes are allowed.

## Shared actor categories

The same codes and definitions apply to speaker, responsibility and affected_entities. These are distinct concepts, not mutually exclusive groups. One actor or passage may receive multiple codes within a field when each is supported. Speaker, affected actor and responsible actor remain separate evidence judgments. MISSING remains exclusive. An unused category remains available in every field; zero frequency does not remove it.

### ACTOR_PUBLIC — Public authorities

Government, legislative, administrative, regulatory or security actors acting in that capacity. Ministries, public agencies, officials, military and police units. A country or society alone does not identify a public authority.

### ACTOR_ED_ORG — Educational organisations and leadership

Educational institutions, programmes, organisational units and actors exercising educational leadership. Schools, universities, training institutions, programme leaders and institutional management. An individual teacher is not automatically an institutional representative; a leader may also be an expert when supported.

### ACTOR_EXPERT — Educators, researchers and specialists

People acting through educational practice, research or specialist knowledge and advice. Teachers, educational staff, researchers and specialist advisers. Expertise can overlap with leadership, commercial or occupational capacity when each is demonstrated; a title alone does not establish every capacity.

### ACTOR_BUSINESS — Businesses and commercial actors

Companies, commercial providers, entrepreneurs, investors and actors representing business interests. Commercial employers, technology providers, business owners and startup ventures. Workers are not automatically business representatives; a firm and its workforce can both be coded when both are implicated.

### ACTOR_WORKFORCE — Workers and occupational communities

People or occupational groups in their employment, professional practice or future labour-market capacity. Employees, job entrants, engineers, lawyers, physicians, civil servants and future workers. Learners are not automatically future workers; require an explicit occupational consequence, voice or responsibility. May overlap with expert or learner capacity.

### ACTOR_LEARNER — Learners

People acting or experiencing consequences in their learning or educational formation. Pupils, students, trainees and adult learners. Age or student status alone does not establish the learner relationship in every field.

### ACTOR_FAMILY — Families and caregivers

Parents, relatives, families and caregivers in their care or educational support capacity. Family choices, supervision, support and family consequences. A parent speaking does not automatically establish family responsibility or consequences.

### ACTOR_COLLECTIVE — Civic, professional and international organisations

Organised civic, voluntary, professional, community or intergovernmental bodies and coordinating groups. Associations, charities, unions, international organisations, volunteer groups and identified organising committees. Unorganised public opinion or society as a whole uses SOCIETY; organisational and other capacities may coexist when supported.

### ACTOR_SOCIETY — Wider society and communities

The public, citizens, informal social groups, communities, countries or shared collective life. National or regional development, cultural communities, societal consequences and explicitly attributed public views or collective duties. Do not equate society with government or infer that every group speaks for society.

### ACTOR_AUTHOR — Article author or editorial voice

The identifiable article author, editorial voice or editorial producer in that capacity. Claims advanced in the article’s own narrative voice; explicit consequences or duties for authors/editorial producers. Reporting another actor’s claim alone does not make the author its speaker, beneficiary or responsible actor.

This revision preserves direct equivalents and reviews the linked evidence of the old employer/workforce, public/society and collective categories. It does not claim an independent new full-source recoding. Existing exact illustration spans and account evidence remain traceable; Git preserves the prior files.
