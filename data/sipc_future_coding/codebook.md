# SIPC educational-future codebook v1.1

Codebook v1.1 đã chốt để phân tích imaginaries trong truyền thông qua 12 fields SIPC. Phát triển từ extraction của 1.098 bài. Các mã là thành tố; không phải một bộ loại imaginaries bắt buộc. Chú thích này cập nhật cách diễn giải, không thay đổi định nghĩa hay mã đã chốt.

**Trạng thái:** frozen for full-corpus application; user confirmed codebook checked

## Nguyên tắc của bản sửa

- Future role mô tả quan hệ giáo dục thay đổi, không mặc định tích cực hay tiêu cực. Giữ cơ chế, hướng thay đổi, điều kiện và người phát biểu.
- Đánh giá gắn với một tương lai cụ thể. Hỗ trợ/thay thế, phát triển/suy giảm là hướng thay đổi; người phát biểu có thể đánh giá các hướng ấy khác nhau.
- Không ép số nhóm hoặc số ví dụ positive/negative bằng nhau; không kết luận corpus thiên positive trước khi coding.
- Qualifiers giữ chi tiết được nguồn nêu; không biến mọi facet thành category hoặc giả định các facet đồng nghĩa.
- MISSING là không được nêu. Unsettled phải có bằng chứng người nói chưa quyết định giá trị, không chỉ chưa biết kết quả.

## Ngưỡng phân tích

Chỉ mã hoá thay đổi, mục đích hoặc trật tự giáo dục được dự kiến, mong muốn, quy định, phản đối hoặc đang được hiện thực hoá. AI chung, benchmark, số liệu sử dụng và thông báo sản phẩm không tự đủ điều kiện. Không cần thì tương lai nếu một sự sắp xếp giáo dục được hướng tới đã rõ.

Phân biệt clear_future, borderline_future, no_educational_future và unresolved_source. Nguồn inadequate là unresolved_source; nguồn partial chỉ cho phép kết luận trong phần văn bản còn lại.

## Số mã theo trường

| Trường | Số mã |
|---|---:|
| future_role | 9 |
| certainty | 7 |
| desirability | 4 |
| rationale | 9 |
| technology_object | 8 |
| education_context | 6 |
| timespan | 4 |
| space | 4 |
| speaker | 9 |
| affected_entities | 6 |
| action | 6 |
| responsibility | 7 |

Các mã là lựa chọn ở 12 trường, không phải số loại tương lai. Không lấy tổng mã làm số imaginaries.

## Thông tin bắt buộc cho mỗi phát biểu tương lai

- **speaker_reference:** Attributed speaker or explicitly identifiable authorial voice; never pool rival voices.
- **future_statement:** Source-supported educational arrangement, with primary/secondary position retained.
- **role_details:** For each role code: mechanism/facet, direction, conditions and source anchor; use not specified where absent.
- **evaluation_target:** Precisely what arrangement or effect the evaluation concerns, not AI in general.
- **stance:** Source wording for endorsement/refusal/recommendation; not specified if absent. Refusal does not determine valence.
- **qualification:** Conditions/safeguards and mixed-effect explanation, or not specified.

Một bài có nhiều tiếng nói cần nhiều accounts. Giữ liên kết speaker → future role → rationale → action/responsibility của từng account; đồng xuất hiện chưa chứng minh cùng một cấu hình.

## future_role

### FR_CAPABILITY_PATHWAYS — AI-related capabilities and educational pathways

Education is reorganised to cultivate capabilities or pathways for participation in an AI-shaped society. This includes specialist formation, general literacy, professional adaptation and credential/pathway revaluation, without treating these ends as interchangeable.

**inclusion:** An explicit educational capability or pathway, with its intended learners, depth and purpose stated or left unspecified. Preserve whether the source anticipates preparation, exclusion, obsolescence or a contested route.

**exclusion:** AI adoption alone; salaries, medals or hiring preferences without an articulated educational direction. Do not infer institutional reform from an individual credential anecdote.

**neighbours:** Use the changed educational relation, not the technology or its overall reputation, to distinguish neighbouring roles.

**co_coding:** Code distinct supported relations within one attributed future account. Preserve facets, direction and evaluation separately; do not borrow another speaker’s rationale or stance.

**required_facets:** formation purpose: specialist expertise / general civic literacy / work-life adaptation / pathway-credential change / other source wording; target learners and depth; direction and conditions

**examples:** DOC_0043: Continuous training pipeline is proposed to form strong AI expertise.; DOC_0228: Expert-led training and projects form internationally competitive engineers.; DOC_0346: AI competence is framed as a general, inclusive civic capability.; DOC_0744: Progressive AI learning forms responsible creators and community-oriented learners.; DOC_0318: Continuous learning responds to rapid AI-related professional change.; DOC_0903: Communication students cultivate distinct human expertise while working with AI.; DOC_0540: Flexible degrees, skills and practice challenge fixed credential value.; DOC_0762: AI-supported self-learning is proposed as a route beyond university.

**boundary_examples:** DOC_0287: Medals/results alone do not establish a developmental educational purpose.; DOC_1057: Missing infographic caption cannot supply unstated literacy goals.; DOC_0310: Student business automation is not an educational preparation claim.; DOC_0027: Hiring without degrees is indirect/current; do not infer institutional schooling reform.; DOC_1040: Adjacent startup and shortened-degree remarks do not prove AI caused a redesign.

### FR_PERSONALISED_GUIDANCE — Individualised learning and pathway guidance

AI guides learning or educational routes around individual needs, pace, gaps, goals or choices. Preserve source-supported facets: instructional adaptation/feedback versus admission or study-pathway advice. These are functions of individual guidance, not separate future types.

**inclusion:** Require explicit tailored instructional or educational-choice support; retain who decides and whether the relation is tutoring, coaching or counselling.

**exclusion:** Benchmark success, admission-score forecasts, generic response speed or assumed personalisation.

**neighbours:** FR_ACCESS_DISTRIBUTION changes participation; FR_COGNITION_AGENCY changes intellectual control.

**co_coding:** Co-code independent supported core dimensions within the same account. Facets are qualifiers in the coding explanation, not additional category IDs. Preserve speaker, proposition, primary/secondary status and exact direction/conditions; do not borrow claims across accounts.

**required_facets:** source-stated mechanism; direction of educational change; conditions and affected relation

**examples:** DOC_0020: Learners follow differentiated paths rather than one common route.; DOC_0843: Individual pathways and unlimited feedback target distinct learner needs.; DOC_0008: AI fills personal counselling gaps without replacing empathy.; DOC_0970: AI expands comparison while applicants retain final choice.

**boundary_examples:** DOC_0258: Present exam-solving benchmark does not propose tutoring.; DOC_0953: Forecast admission scores are not a future educational AI role.

### FR_COGNITION_AGENCY — Learning, knowledge creation and intellectual agency

AI changes who performs intellectual work and how learners or scholars develop knowledge, independent judgment, authorship and agency. Supported inquiry and outsourced thinking are opposing configurations within this relation.

**inclusion:** An explicit prospect or prescription concerning understanding, inquiry, research, authorship, dependence, motivation or epistemic authority.

**exclusion:** Answer speed, benchmark accuracy or generic interactivity alone; errors without a learning/agency implication.

**neighbours:** Use the changed educational relation, not the technology or its overall reputation, to distinguish neighbouring roles.

**co_coding:** Code distinct supported relations within one attributed future account. Preserve facets, direction and evaluation separately; do not borrow another speaker’s rationale or stance.

**required_facets:** mechanism: supported inquiry / scholarly support / authorship / dialogic authority / outsourced thinking / dependence / other source wording; direction: development / erosion / redistribution / contested or unspecified

**examples:** DOC_0264: Learners form ideas and retain authorship before consulting AI.; DOC_0630: Questioning and staged guidance replace direct answers.; DOC_0056: Summarising is justified as support for scholars reading extensive material.; DOC_0936: An intellectual partner is intended to deepen research beyond quick answers.; DOC_0100: AI errors justify the right to be wrong and teachers learning alongside pupils.; DOC_0323: Quick solutions risk impairing later independent learning.; DOC_0824: Dependence erodes voice and capacity after graduation.

**boundary_examples:** DOC_0317: Technical help with an energy project does not itself specify learner agency as an educational arrangement.; DOC_0080: AI clinical diagnosis research does not itself express an educational/scholarly arrangement.; DOC_0126: Fast conversational answers alone do not establish dialogic educational authority.; DOC_0521: A wrong present answer alone does not establish a dependency future.

### FR_TEACHING_LABOUR — Teaching work and human pedagogic authority

AI reallocates teaching tasks, labour, employment or pedagogic authority between humans and systems. Assistance, retained judgment and substitution must remain distinguishable even when sharing this role family.

**inclusion:** A future division of instructional work, teacher capacity, care, judgment, authority or employment.

**exclusion:** Assuming workload reduction means replacement; assuming every automation retains meaningful human teaching; an unrelated employment dispute.

**neighbours:** Use the changed educational relation, not the technology or its overall reputation, to distinguish neighbouring roles.

**co_coding:** Code distinct supported relations within one attributed future account. Preserve facets, direction and evaluation separately; do not borrow another speaker’s rationale or stance.

**required_facets:** division of work: augmentation / substitution / retained human judgment-care / employment reduction / other source wording; which tasks and authority move, and to whom

**examples:** DOC_0114: Automated duties release teachers for inspiration and experience design.; DOC_1030: Personal assistance frees time for understanding and developing pupils.; DOC_0297: Virtual instruction is forecast with fewer highly capable teachers.; DOC_0307: AI replaces direct teaching in a planned personalised model.

**boundary_examples:** DOC_0285: AI delivering whole instruction is displacement even when people retain classroom discipline.; DOC_0309: Case-specific reinstatement after a dispute is not technological teacher replacement.

### FR_ACADEMIC_JUDGMENT — Assessment, academic recognition and legitimate judgment

AI changes how educational competence, contribution and authenticity are demonstrated or judged. Assessment redesign, misconduct control and due process are distinct mechanisms within this relation.

**inclusion:** An explicit projected or normative arrangement for demonstrating learning, certification, integrity, monitoring or fair human adjudication.

**exclusion:** A completed cheating incident alone; exam-solving performance; an AI topic in an exam without a changed assessment arrangement.

**neighbours:** Use the changed educational relation, not the technology or its overall reputation, to distinguish neighbouring roles.

**co_coding:** Code distinct supported relations within one attributed future account. Preserve facets, direction and evaluation separately; do not borrow another speaker’s rationale or stance.

**required_facets:** mechanism: assessment redesign / authenticity-compliance / certification / monitoring / due process / other source wording; what counts as achievement and who may judge it

**examples:** DOC_0293: Process and personal argument replace reliance on polished final output.; DOC_0784: University evaluation shifts toward judgment and responsibility.; DOC_0252: Conditional national AI proctoring is linked to fair examinations.; DOC_0587: Control of services is proposed to prevent cheating at its source.; DOC_0351: Detectors should assist rather than automatically convict.; DOC_0622: Human judgment and dialogue resist algorithmic punishment.

**boundary_examples:** DOC_0129: AI as an essay topic alone supplies no assessment-redesign future.; DOC_0600: Completed misconduct and prosecution alone do not articulate a future.; DOC_0827: Improved answer-choice reliability does not alone address false accusations or trust.

### FR_ACCESS_DISTRIBUTION — Access, participation and distribution of educational opportunity

AI changes who can participate in education and how learning opportunities or resources are distributed. Expanded access, exclusion and widened inequality are all eligible directions when explicitly supported.

**inclusion:** An explicit future or normative arrangement concerning opportunity across cost, location, disability, language, age or unequal capability/resource access.

**exclusion:** Availability or free promotion without educational participation implications; a generic social inequality claim with no educational future.

**neighbours:** FR_PERSONALISED_GUIDANCE changes fit; this changes participation distribution.

**co_coding:** Allowed only for distinct supported dimensions of the same educational-future account. Preserve account_id, speaker, proposition and primary/secondary status; do not combine another speaker’s reason or evaluation into this account.

**required_facets:** direction: widened access / reduced access / narrowed inequality / widened inequality / conditional or contested; barrier or distribution mechanism and affected learners

**examples:** DOC_0497: AI learning keeps older people included and connects generations.; DOC_1052: Voice-over opens independent reading to blind children.; DOC_0455: Secondary expert warning anticipates a widened digital divide alongside the principal promises; retain its separate attribution.; DOC_0940: Unequal tools, connectivity, literacy and language may widen educational inequality; the proposed safeguards belong to the preferred alternative.

**boundary_examples:** DOC_0340: Equitable clinical MRI access is not educational inclusion.

### FR_INSTITUTIONAL_REORGANISATION — Institutional organisation and educational mission

AI reorders educational governance, data, coordination, services or institution-level priorities, including explicit fears of mission loss through platforms, profit or metrics. Preserve source-supported facets: integrated data-informed organisation; ecosystem coordination; platform/commercial or metric-led mission hollowing. Preserve direction and who benefits, rather than a new core category for each organisational function.

**inclusion:** Whole-institution/sector architecture, connected governance or explicit institutional commercial/metric ordering.

**exclusion:** Isolated device/task, every corporate collaboration, coder-inferred ownership causation or metrics automatically treated as harmful.

**neighbours:** FR_HUMAN_PUBLIC_PURPOSE states educational ends; FR_TEACHING_LABOUR/DISPLACEMENT concern teaching labour.

**co_coding:** Co-code independent supported core dimensions within the same account. Facets are qualifiers in the coding explanation, not additional category IDs. Preserve speaker, proposition, primary/secondary status and exact direction/conditions; do not borrow claims across accounts.

**required_facets:** source-stated mechanism; direction of educational change; conditions and affected relation

**examples:** DOC_0274: An integrated university architecture links learning, prediction and administration.; DOC_0817: Sector governance shifts from dispersed management to connected data-informed decisions.; DOC_0135: Profit-led automation threatens academic labour and democratic educational ends.; DOC_0906: Platform spending and layoffs are opposed as a hollowing university future.

**boundary_examples:** DOC_0803: Smart equipment procurement without stated AI role is not an AI governance future.; DOC_0943: Measurement of actual impact is proposed accountability, not necessarily hollowing by metrics.

### FR_WELLBEING_RELATIONS — Learner wellbeing and school social relations

AI is positioned in future protection or deterioration of learner safety, care, emotional development and school social connection. Preserve source-supported facets: protection/early intervention versus abuse, emotional harm or loss of human connection. Direction and desirability must remain explicit; sharing a core category is not a shared educational future.

**inclusion:** Explicit safeguarding, counselling, health/safety or projected abuse/relational deprivation involving education.

**exclusion:** Clinical treatment outside education, general user risk or campus incidents without educational projection.

**neighbours:** FR_COGNITION_AGENCY concerns learning capacity; FR_ACADEMIC_JUDGMENT concerns fair academic recognition.

**co_coding:** Co-code independent supported core dimensions within the same account. Facets are qualifiers in the coding explanation, not additional category IDs. Preserve speaker, proposition, primary/secondary status and exact direction/conditions; do not borrow claims across accounts.

**required_facets:** direction: protection / harm / relationship development / relationship loss / contested; care, safety or social mechanism

**examples:** DOC_0151: School warning systems anticipate violence and self-harm for intervention.; DOC_0808: A chatbot enables safe participation and alerts to cyberbullying.; DOC_0190: Cheap realistic deepfakes forecast escalating school harassment and harm.; DOC_0321: Technology-only classrooms are feared to remove compassion and maturation.

**boundary_examples:** DOC_0861: Campus location of a criminal incident alone does not articulate an educational future.; DOC_0342: Public privacy demonstration by students is not itself a school-harm future.

### FR_HUMAN_PUBLIC_PURPOSE — Human development and the public purpose of education

AI-related education is reordered around moral, cultural, aesthetic or democratic human development beyond efficiency and labour supply.

**inclusion:** Explicit educational purpose safeguarding identity, compassion, emancipation, civic life or common good.

**exclusion:** Coder approval; generic ethics mention; unrelated heritage-product future.

**neighbours:** FR_CAPABILITY_PATHWAYS concerns capabilities; this articulates the ends and public meaning of education.

**co_coding:** Allowed only for distinct supported dimensions of the same educational-future account. Preserve account_id, speaker, proposition and primary/secondary status; do not combine another speaker’s reason or evaluation into this account.

**required_facets:** source-stated mechanism; direction of educational change; conditions and affected relation

**examples:** DOC_0649: The university becomes an ethical intellectual community rather than only credential production.; DOC_1089: Innovation is subordinated to aesthetic experience, cultural identity and human development.

**boundary_examples:** DOC_0487: Students preserving music through an AI product does not by itself express an educational future.

## certainty

### CERT_ASSERTED — Asserted future outcome

The account states an educational outcome as a firm projection. Explicit inevitability is retained as a stronger claim, not inferred from will-language.

**inclusion:** A firm projected outcome or an explicitly unavoidable transition.

**exclusion:** Desire, announced intention, possibility or coder confidence alone.

**neighbours:** Use the changed educational relation, not the technology or its overall reputation, to distinguish neighbouring roles.

**co_coding:** Code distinct supported relations within one attributed future account. Preserve facets, direction and evaluation separately; do not borrow another speaker’s rationale or stance.

**required_facets:** assertion strength: projected / explicitly inevitable

**examples:** DOC_0117: Speaker says education will certainly change fundamentally.; DOC_0503: Gates firmly forecasts widely available tutoring.; DOC_0115: AI integration is described as unavoidable.; DOC_0673: A shift toward human–machine co-creation is described as irreversible.

**boundary_examples:** DOC_0258: 100% current benchmark accuracy is not future certainty.; DOC_0716: A proposed pilot is not an inevitable transition.

### CERT_POSSIBLE — Possible or potential outcome

The educational future is framed as an ability, possibility or potential rather than guaranteed outcome.

**inclusion:** Could/may/potential relation to a projected or desired educational arrangement.

**exclusion:** Current tool specification without future arrangement; tentative wording unrelated to education.

**neighbours:** CERT_CONDITIONAL names dependencies; CERT_OPEN leaves outcome unsettled.

**co_coding:** Allowed only for distinct supported dimensions of the same educational-future account. Preserve account_id, speaker, proposition and primary/secondary status; do not combine another speaker’s reason or evaluation into this account.

**examples:** DOC_0063: Researcher projects a possible concentration-informed teaching application.; DOC_0107: Different speakers describe possible changes in learning and assessment.

**boundary_examples:** DOC_0253: Present benchmark results do not become a potential educational future by default.

### CERT_CONDITIONAL — Explicitly contingent future

An outcome/evaluation depends on specified implementation, action, context or use.

**inclusion:** If/only when/unless or clear causal contingency; retain which condition attaches to which future.

**exclusion:** All forecasts are uncertain in reality; do not add an implicit condition.

**neighbours:** CERT_POSSIBLE is modal strength without named dependency; CERT_NORMATIVE is what should happen.

**co_coding:** Allowed only for distinct supported dimensions of the same educational-future account. Preserve account_id, speaker, proposition and primary/secondary status; do not combine another speaker’s reason or evaluation into this account.

**examples:** DOC_0252: Expansion is explicitly conditional on effectiveness.; DOC_0737: AI education benefits require investment avoiding unequal opportunities.

**boundary_examples:** DOC_0329: Planned curriculum addition without stated dependency is not automatically conditional.

### CERT_INTENDED — Intended or committed educational future

The account articulates a desired or planned educational arrangement without treating the outcome as achieved. Aspirations, proposals and authorised commitments retain their different institutional force.

**inclusion:** An explicit hope, goal, proposal, promise, schedule or authorised implementation.

**exclusion:** An outcome asserted to occur, or a general should-statement with no actor intention.

**neighbours:** Use the changed educational relation, not the technology or its overall reputation, to distinguish neighbouring roles.

**co_coding:** Code distinct supported relations within one attributed future account. Preserve facets, direction and evaluation separately; do not borrow another speaker’s rationale or stance.

**required_facets:** institutional force: aspiration / proposed plan / promise / scheduled-authorised commitment; intending actor

**examples:** DOC_0002: Research abroad is a personal AI-learning dream.; DOC_0193: Future mentoring and research contributions are hoped for.; DOC_0271: A university commits to whole-institution AI integration.; DOC_1063: Official implementation is announced while safeguards constrain its form.

**boundary_examples:** DOC_0016: Current popularity and admission scores establish no goal.; DOC_0120: An unspecified future-applications event does not guarantee any detailed reform.

### CERT_NORMATIVE — Normative necessity or prescription

The future arrangement is asserted as what education/actors should, must or need to do.

**inclusion:** Explicit obligation, prohibition, recommendation or priority tied to educational future.

**exclusion:** Read must as probabilistic certainty; mere legal consequence of a completed event.

**neighbours:** CERT_ASSERTED says cannot be avoided; obligation can oppose what seems likely.

**co_coding:** Allowed only for distinct supported dimensions of the same educational-future account. Preserve account_id, speaker, proposition and primary/secondary status; do not combine another speaker’s reason or evaluation into this account.

**examples:** DOC_0311: Rules state what classroom AI use should permit and require.; DOC_0751: Educational purpose and teacher autonomy are prescribed.

**boundary_examples:** DOC_0925: Retrospective suspension alone is not a future prescription.

### CERT_LIMIT_DENIAL — Denied or bounded future capability

The account rules out, limits or distances a particular educational future, including replacement.

**inclusion:** Explicit cannot/never/unlikely or temporally remote capability limit tied to the future. Preserve absolute vs contextual/near-term qualifiers.

**exclusion:** Negative desirability does not mean impossible; current error alone.

**neighbours:** CERT_OPEN means unresolved; CERT_CONDITIONAL can support a limit depending on conditions.

**co_coding:** Allowed only for distinct supported dimensions of the same educational-future account. Preserve account_id, speaker, proposition and primary/secondary status; do not combine another speaker’s reason or evaluation into this account.

**examples:** DOC_0106: Human emotional interaction limits near-term teacher replacement.; DOC_0449: One speaker categorically denies replacement while another fears it.

**boundary_examples:** DOC_0321: A feared dehumanised classroom can be undesirable without being denied as possible.

### CERT_OPEN — Open, contested efficacy or unresolved outcome

The speaker explicitly leaves the future, effects or solution unresolved, uncertain or under evaluation.

**inclusion:** Open question, cannot know, wait for evidence, uncertain long-term effects or no settled solution.

**exclusion:** MISSING; disagreement between other speakers alone; generic possible statement.

**neighbours:** CERT_POSSIBLE asserts an available possibility; this foregrounds inability to settle outcome.

**co_coding:** Allowed only for distinct supported dimensions of the same educational-future account. Preserve account_id, speaker, proposition and primary/secondary status; do not combine another speaker’s reason or evaluation into this account.

**examples:** DOC_0343: Future consequences remain hard to predict.; DOC_1007: Best adaptation remains unknown and imperfect.

**boundary_examples:** DOC_0001: Unspecified probability is not a consciously open future.

## desirability

### DES_POSITIVE — Positively valued educational future

The speaker values a specified projected educational arrangement or effect as beneficial or desirable.

**inclusion:** Explicit approval, benefit, empowerment, fairness or preferred educational order, including endorsement with stated safeguards.

**exclusion:** Inevitability, novelty, technical accuracy or a policy announcement without value judgment; inferred enthusiasm.

**neighbours:** Use DES_MIXED only when the same speaker explicitly weighs favourable and adverse effects of the same target.

**co_coding:** Keep the attributed speaker, exact evaluation target and conditions. An article with rival voices is not automatically one mixed account; refusal of a ban is not automatically negative evaluation of AI.

**examples:** DOC_0007: Robots are valued for engaging, accessible language education.; DOC_0864: Responsible technology learning is positively valued as community-oriented preparation.; DOC_0288: Preschool AI is valued only with balanced interaction and safeguards.; DOC_0527: Personal support and inclusion are endorsed through responsible implementation.

**boundary_examples:** DOC_0287: Celebrated medals alone do not justify coding educational future endorsement.

### DES_NEGATIVE — Adversely valued educational future

The speaker evaluates a specified projected educational arrangement or effect as harmful or undesirable.

**inclusion:** Explicit anticipated harm, feared educational order or adverse value judgment about a specified arrangement.

**exclusion:** Capability limits, uncertainty or refusal alone. A desired protective restriction can be positively valued while the prevented outcome is negative.

**neighbours:** A rejected arrangement and a preferred alternative have different targets; code their evaluations separately.

**co_coding:** Keep the attributed speaker, exact evaluation target and conditions. An article with rival voices is not automatically one mixed account; refusal of a ban is not automatically negative evaluation of AI.

**examples:** DOC_0087: ChatGPT use is feared to reduce foundational thinking and integrity.; DOC_0386: Algorithmic accusation is presented as an educational nightmare.

**boundary_examples:** DOC_0304: Retrospective complaint and dismissal without future do not establish this value.

### DES_MIXED — Explicitly mixed evaluation of the same future

One attributed voice explicitly evaluates the same projected arrangement as having both desirable and undesirable educational implications.

**inclusion:** An explicit trade-off or ambivalence concerning a common target. Retain the beneficial and harmful mechanisms.

**exclusion:** Different speakers disagreeing; separate preferred and rejected alternatives; positive endorsement with safeguards but no adverse effect articulated.

**neighbours:** Conditional endorsement alone remains DES_POSITIVE with qualification; withheld judgment is DES_UNSETTLED.

**co_coding:** Use this compact summary for a genuinely mixed account; retain component evaluations in its explanation rather than duplicate POSITIVE and NEGATIVE mechanically. Keep the attributed speaker, exact evaluation target and conditions. An article with rival voices is not automatically one mixed account; refusal of a ban is not automatically negative evaluation of AI.

**examples:** DOC_0824: Williams recognises improved discussion of difficult topics while warning of reduced original voice; verify and preserve this specific voice rather than pooling all interviewees.

**boundary_examples:** DOC_0307: Institutional promises and McGovern’s objections are rival accounts; article-level disagreement alone is not one mixed evaluation.

### DES_UNSETTLED — Educational value remains explicitly undecided

The educational benefit/desirability or efficacy is explicitly left unproven or awaiting evaluation.

**inclusion:** Unresolved usefulness, wait for results, questioning claimed benefit.

**exclusion:** No desirability specification; opposition versus approval elsewhere without the speaker withholding judgement.

**neighbours:** CERT_OPEN concerns predictability; this concerns whether the outcome is educationally worthwhile.

**co_coding:** Allow positive/harmful/refusal or qualified/unsettled dimensions only where separately supported within the same account. A single speaker valuing both benefits and harms is an ambivalence qualifier; rival speakers remain separate accounts, not one ambivalent article. Preserve primary/secondary status and stance target.

**examples:** DOC_0250: Low-cost tutoring usefulness remains disputed rather than assumed beneficial.

**boundary_examples:** DOC_0419: No explicit value specification is MISSING, not unsettled value.; DOC_0361: The article positively reports the trial experience but leaves the larger revolutionary transformation as a question; an open efficacy claim is not by itself withheld desirability. Use DES_UNSETTLED only if value is explicitly withheld.

## rationale

### RATION_LEARNING_DEVELOPMENT — How learning and capability develop

The future is warranted by an account of how people learn or develop capability: individual fit, feedback, effort, ownership, experience or practical application. Preserve the mechanism; these warrants need not agree.

**inclusion:** An explicit explanation connecting an arrangement to learning or expertise development.

**exclusion:** A feature list or effectiveness slogan without a learning explanation.

**neighbours:** Use the changed educational relation, not the technology or its overall reputation, to distinguish neighbouring roles.

**co_coding:** Code distinct supported relations within one attributed future account. Preserve facets, direction and evaluation separately; do not borrow another speaker’s rationale or stance.

**required_facets:** learning mechanism: fit-feedback / effort-inquiry / authorship / practical transfer / other source wording

**examples:** DOC_0018: Different speeds/preferences justify differentiated pathways.; DOC_0406: Distinct learning DNA is invoked against uniform teaching.; DOC_0224: Age-appropriate AI experience helps learners recognise human feeling.; DOC_0554: Interaction and explicit pedagogic models determine learning benefits.; DOC_0323: Quick answers prevent independent problem solving.; DOC_0887: Productive struggle is argued to create lasting understanding.; DOC_0811: High-pressure realistic practice shortens classroom–lab–work transition.; DOC_1006: Real operational requirements develop capability beyond strong models.

**boundary_examples:** DOC_0273: General institutional ambition without a fit reason does not supply this rationale.; DOC_0640: A one-off decoration recipe does not establish pedagogical transformation.; DOC_0258: Correct benchmark answers do not explain formative learner effort.; DOC_0079: Biography and past achievement alone are not a prospective motivation rationale.; DOC_0495: Cultural product development alone does not articulate a future educational transfer purpose.

### RATION_RESOURCES_READINESS — Resources and readiness for educational provision

The future responds to resource constraints or conditions of viable implementation, including staffing, workload, costs, organisational capacity and developmental readiness.

**inclusion:** Explicit resource or readiness conditions explaining why the proposed arrangement is needed, feasible or inappropriate.

**exclusion:** Assumed efficiency; every age or budget mention without a justificatory relation.

**neighbours:** Use the changed educational relation, not the technology or its overall reputation, to distinguish neighbouring roles.

**co_coding:** Code distinct supported relations within one attributed future account. Preserve facets, direction and evaluation separately; do not borrow another speaker’s rationale or stance.

**required_facets:** constraint: time-staff / money-affordability / technical-organisational readiness / developmental appropriateness / other source wording

**examples:** DOC_0008: Thin counselling staff justify AI guidance.; DOC_0268: Repetitive work consumes time needed for creative and relational teaching.; DOC_0569: Class fees/travel costs support cheaper language learning.; DOC_0540: Tuition debt and return challenge credential-centred routes.; DOC_0338: Successful integration requires coordinated infrastructure, training and policy.; DOC_0727: Limited time and personnel make superficial curricular addition ineffective.; DOC_0428: Young children lack foundations for evaluating automated thinking.; DOC_0833: Early exploration must preserve movement and direct experience.

**boundary_examples:** DOC_0340: Clinical capacity pressure is outside educational scope.; DOC_0952: Fee lists without educational future do not establish a cost rationale.; DOC_0613: A directive alone does not justify its effectiveness through unstated conditions.; DOC_0423: Competing age proposals must remain speaker-specific, not a single consensus readiness rule.

### RATION_HUMAN_RELATION — Human formation and public educational value

The account justifies arrangements through human relationships, dignity, moral/civic life and the educational purpose of developing people. Preserve source-supported facets: interpersonal affective formation versus normative human/public ends. Preserve democratic purpose when explicit (DOC0649), not as an inferred property of all care.

**inclusion:** Explicit care, trust, inspiration, social experience, common good, emancipation or public mission connected to educational AI future.

**exclusion:** Generic ethics label, coder approval or presumed human emotional uniqueness.

**neighbours:** RATION_LEARNING_DEVELOPMENT concerns cognitive formation; RATION_COLLECTIVE_SELFDETERMINATION concerns rooted identity/autonomy.

**co_coding:** Co-code independent supported core dimensions within the same account. Facets are qualifiers in the coding explanation, not additional category IDs. Preserve speaker, proposition, primary/secondary status and exact direction/conditions; do not borrow claims across accounts.

**examples:** DOC_0106: No empathy or interaction explains replacement limits.; DOC_0370: Teacher care and inspiration justify a human-centred partnership.; DOC_0649: Education should be a democratic intellectual community serving the common good.; DOC_0969: Human dignity, aspiration and happiness justify keeping technology subordinate.

**boundary_examples:** DOC_0827: Technical answer reliability alone says nothing about human relational formation.; DOC_0171: Humanistic skills may be supported, but do not infer a detailed democratic mission absent from text.

### RATION_TRUST_ACCOUNTABILITY — Trustworthy and accountable educational relations

The future is warranted or constrained by the reliability of knowledge, authenticity of contribution, fairness of judgment, rights or data protection. Preserve whether the concern is epistemic reliability, academic legitimacy or rights, rather than treating all as one risk.

**inclusion:** An explicit educational justification involving reliable knowledge, honest/fair recognition, privacy, rights or accountable decisions.

**exclusion:** An incident, technical error or general safety claim without an educational-future warrant.

**neighbours:** Use the changed educational relation, not the technology or its overall reputation, to distinguish neighbouring roles.

**co_coding:** Code distinct supported relations within one attributed future account. Preserve facets, direction and evaluation separately; do not borrow another speaker’s rationale or stance.

**required_facets:** warrant: knowledge reliability / authorship-certification / fair judgment-due process / privacy-data rights / other source wording

**examples:** DOC_0118: Verified input sources are argued to make tutoring useful.; DOC_0647: Missing historical context and viral priorities risk distorted knowledge.; DOC_0189: A degree should certify actual ability rather than externally produced writing.; DOC_0868: Easy cheating destabilises honour and credential trust.; DOC_0351: False accusations injure trust, wellbeing and opportunities.; DOC_1031: Data and unapproved access justify educational control objections.

**boundary_examples:** DOC_0229: Humorous inaccurate output without a future claim remains a boundary.; DOC_0600: Retrospective prosecution alone is not an articulated future rationale.; DOC_0339: Do not invent privacy opposition when the source itself only assures security.

### RATION_EQUITY — Unequal educational opportunity

The future is justified or questioned through unequal participation, resources, guidance, disability, geography or generational access.

**inclusion:** Explicit educational distributional reason, inclusion need or risk of widening gaps.

**exclusion:** Any free tool; differences in usage alone; clinical inequality.

**neighbours:** RATION_RESOURCES_READINESS (affordability facet) identifies financial mechanism; equity identifies distribution of opportunities.

**co_coding:** Allowed only for distinct supported dimensions of the same educational-future account. Preserve account_id, speaker, proposition and primary/secondary status; do not combine another speaker’s reason or evaluation into this account.

**examples:** DOC_1052: Visual resources exclude blind children, motivating accessible reading.; DOC_0837: Unequal teacher guidance explains widening or narrowing rural gaps.

**boundary_examples:** DOC_0208: Product convenience alone does not establish a distributive rationale.

### RATION_WORK_DEMAND — Changing societal and professional requirements

The future answers AI-driven shifts in knowledge, civic life, professions or required skills, including shortages and obsolescence. Preserve source-supported facets: concrete workforce demand versus wider technological/civic change and skill obsolescence. Do not infer employment claims from a civic-literacy rationale.

**inclusion:** Explicit labour demand/requirements or rapid change explaining why education must adapt.

**exclusion:** AI called modern/inevitable without explanation; employment prediction without an educational account.

**neighbours:** RATION_COLLECTIVE_SELFDETERMINATION concerns collective strategy; RATION_LEARNING_DEVELOPMENT explains how education bridges theory and use.

**co_coding:** Co-code independent supported core dimensions within the same account. Facets are qualifiers in the coding explanation, not additional category IDs. Preserve speaker, proposition, primary/secondary status and exact direction/conditions; do not borrow claims across accounts.

**examples:** DOC_0076: Specialist skills answer growing AI workforce demand.; DOC_0818: Industry requires engineers who can use AI immediately.; DOC_0144: Fast AI change makes teacher preparation and continuing learning necessary.; DOC_1046: Predicted skill obsolescence motivates foundational adaptable education.

**boundary_examples:** DOC_0994: Generic shortage does not alone establish an AI training arrangement; weak educational linkage needs review.; DOC_0919: A new model release without an educational response does not supply this reason.

### RATION_COLLECTIVE_SELFDETERMINATION — Collective development, autonomy and identity

The educational future serves collective development, strategic standing, technological autonomy or cultural self-determination. Preserve competitive, security, political and cultural purposes as distinct source-supported warrants.

**inclusion:** Explicit collective development, standing, defence, autonomy, local linguistic-cultural validity or identity as an educational warrant.

**exclusion:** Inferred national purpose from a public speaker; infer commercial/state control from publication group; infer sovereignty from local language alone.

**neighbours:** Use the changed educational relation, not the technology or its overall reputation, to distinguish neighbouring roles.

**co_coding:** Code distinct supported relations within one attributed future account. Preserve facets, direction and evaluation separately; do not borrow another speaker’s rationale or stance.

**required_facets:** purpose: strategic development-standing / security-political obligation / technological-data autonomy / linguistic-cultural identity / other source wording; collective and scale actually named

**examples:** DOC_0014: Training is connected to bringing Vietnamese intellectual capability globally.; DOC_0547: Education investment underpins strategic digital-economic competitiveness.; DOC_0507: AI training supports ideological work and defence of Party foundations.; DOC_0665: Military pedagogic innovation is justified through command capability and homeland defence.; DOC_0914: Official examination secrecy/security motivates prevention.; DOC_0499: Foreign systems threaten the capacity to speak through verified Vietnamese cultural knowledge.; DOC_0791: Training builds autonomy in core technologies and reduces external reliance.; DOC_0328: Design education must preserve personal and national cultural identity.; DOC_1089: Direct aesthetic experience and cultural formation justify technology limits.

**boundary_examples:** DOC_0435: An individual study dream does not automatically supply a national-development rationale.; DOC_0151: Protecting pupils from bullying alone is wellbeing rather than state/ideological security.; DOC_0543: Mother-tongue summaries ease access but do not alone claim collective sovereignty.; DOC_0487: Public music preservation alone is outside educational-future scope.

### RATION_POLICY_AUTHORITY — Policy or standards as legitimating warrant

The future is justified by an explicit requirement/alignment with named policy, strategy, curricular standards or official commitments.

**inclusion:** Policy is invoked as why an arrangement should be pursued, not merely date/context.

**exclusion:** Directive counted automatically as its own rationale; legitimacy inferred by coder.

**neighbours:** RATION_RESOURCES_READINESS explains implementation; this invokes formal warrant for direction.

**co_coding:** Allowed only for distinct supported dimensions of the same educational-future account. Preserve account_id, speaker, proposition and primary/secondary status; do not combine another speaker’s reason or evaluation into this account.

**examples:** DOC_0355: AI resources are connected to competency objectives of the 2018 curriculum.; DOC_1075: National education breakthrough policy legitimates universal AI access.

**boundary_examples:** DOC_0329: Planned curriculum role has no supplied rationale; do not manufacture formal justification.

### RATION_MARKET_POWER — Commercial incentives, cost discipline and platform capture

The account explains the educational future through business revenue, client acquisition, profit-led substitution, cost discipline or commercial control.

**inclusion:** Explicit explanatory commercial motive or critique; report actor/coder distance and interest beneficiary.

**exclusion:** Assume motives from ownership or advertisements; any business collaboration alone.

**neighbours:** RATION_RESOURCES_READINESS (affordability facet) concerns educational affordability; this concerns business incentives and power.

**co_coding:** Allowed only for distinct supported dimensions of the same educational-future account. Preserve account_id, speaker, proposition and primary/secondary status; do not combine another speaker’s reason or evaluation into this account.

**examples:** DOC_0135: Profit and budgets drive automation opposed to labour interests.; DOC_0533: Free student access is interpreted as building platform habits and market position.; DOC_1069: Product expansion is explicitly connected to customer acquisition.

**boundary_examples:** DOC_0759: University–business collaboration for talent does not prove profit-led educational capture.

## technology_object

### OBJ_AI_UNSPECIFIED — AI with no specified form

The future implicates AI but source supplies no more specific supported object form.

**inclusion:** Generic future-linked AI propositions.

**exclusion:** Not an extra umbrella code on an already specified referent; absence of future-linked object is MISSING.

**neighbours:** Distinguish from OBJ_AI_KNOWLEDGE, OBJ_CONTENT_LANGUAGE, OBJ_LEARNING_SYSTEM, OBJ_ANALYSIS_MONITORING, OBJ_INTEGRITY_CHECK, OBJ_EMBODIED_SIMULATION, OBJ_SYSTEM_INFRASTRUCTURE. Assign by the defined field relation; retain variants in required_qualifiers rather than generating extra labels.

**co_coding:** Allow distinct supported families within the same articulated account, with separate primary/secondary account IDs and evidence. Do not duplicate an umbrella family for a more specific referent; do not pool unrelated claims.

**examples:** DOC_0615: AI support and assessment are discussed without naming a form.; DOC_0717: AI is a reflective assistant in the desired classroom without a specified product.

**boundary_examples:** DOC_0719: AI mathematics performance does not articulate an educational future.

### OBJ_AI_KNOWLEDGE — AI as educational knowledge/competence

AI concepts, techniques, application competence and ethics are the objects to be learned.

**inclusion:** Curriculum, literacy, technical/degree formation, research competence about AI.

**exclusion:** AI used to teach another subject is not automatically teaching about AI.

**neighbours:** Distinguish from OBJ_AI_UNSPECIFIED, OBJ_CONTENT_LANGUAGE, OBJ_LEARNING_SYSTEM, OBJ_ANALYSIS_MONITORING, OBJ_INTEGRITY_CHECK, OBJ_EMBODIED_SIMULATION, OBJ_SYSTEM_INFRASTRUCTURE. Assign by the defined field relation; retain variants in required_qualifiers rather than generating extra labels.

**co_coding:** Allow distinct supported families within the same articulated account, with separate primary/secondary account IDs and evidence. Do not duplicate an umbrella family for a more specific referent; do not pool unrelated claims.

**examples:** DOC_0346: AI competence is proposed for all pupils.; DOC_0551: AI introduction is a required university learning object.

**boundary_examples:** DOC_0289: AI degree name in a points/fees report establishes no future.

### OBJ_CONTENT_LANGUAGE — AI producing or processing language/content

AI generates, transforms, interprets or retrieves educational content, language or answers.

**inclusion:** Conversational/writing/coding tools, image/audio/video generation, transcription, translation, pronunciation and AI-mediated answer devices tied to the future.

**exclusion:** Pure learner progression system, origin detector or sensing system receives its own family; not all listed apps are AI.

**neighbours:** OBJ_LEARNING_SYSTEM requires an instructional environment/progression mechanism, not just answer/content production. OBJ_INTEGRITY_CHECK judges origin. OBJ_ANALYSIS_MONITORING concerns learner/environmental data. A chatbot can have separate supported roles.

**co_coding:** Allow distinct supported families within the same articulated account, with separate primary/secondary account IDs and evidence. Do not duplicate an umbrella family for a more specific referent; do not pool unrelated claims.

**examples:** DOC_0084: ChatGPT produces academic content in competing educational futures.; DOC_0059: AI pronunciation processing supports learner-directed language practice; do not call it generative without evidence.; DOC_0782: Music and podcast generation support literary expression.

**boundary_examples:** DOC_0628: AI Agent/captcha news has no educational future.; DOC_0600: AI exam devices in a past-offence report are not sufficient to articulate an educational future.

### OBJ_LEARNING_SYSTEM — AI instructional and learning-interaction systems

AI is configured as a learning environment, tutor, adaptive resource or learning-interaction mechanism.

**inclusion:** Personalised progression, AI tutors/textbooks, explicit AI-linked incentives; fictional direct knowledge transfer stays a fictional secondary variant.

**exclusion:** A general-purpose chatbot is not automatically an adaptive tutor; brand alone insufficient; do not infer real deployment from fiction.

**neighbours:** OBJ_CONTENT_LANGUAGE for general-purpose content processing; OBJ_SYSTEM_INFRASTRUCTURE for institution/platform capacity; an identified adaptive or incentive mechanism determines this family.

**co_coding:** Allow distinct supported families within the same articulated account, with separate primary/secondary account IDs and evidence. Do not duplicate an umbrella family for a more specific referent; do not pool unrelated claims.

**examples:** DOC_0019: VioEdu directs learner-specific pathways.; DOC_0430: Adaptive tablets promise tutoring tailored to learning gaps.; DOC_0907: AI pets organise educational incentives; an incentive qualifier prevents conflating them with cognitive adaptation.

**boundary_examples:** DOC_0701: Neural Tapestry belongs only to the explicit fictional2525 secondary account; keep neural transfer as a rare raw mechanism, not a separate core category.; DOC_0634: AI-made optional material is not necessarily an adaptive learning system.

### OBJ_ANALYSIS_MONITORING — AI analysis, prediction and sensing

AI produces educational information or decisions from learner, institutional or environmental data, including monitoring.

**inclusion:** Learning/behaviour/emotion analysis, admissions prediction/routing, attendance/proctoring/safety sensing.

**exclusion:** Origins of submitted content are a distinct integrity-checking family; raw data storage and benchmark evaluation of AI are excluded.

**neighbours:** OBJ_INTEGRITY_CHECK judges origin/similarity of submitted work. This family measures/interprets learner, institutional or environmental data; sensing and decision analytics remain qualifiers.

**co_coding:** Allow distinct supported families within the same articulated account, with separate primary/secondary account IDs and evidence. Do not duplicate an umbrella family for a more specific referent; do not pool unrelated claims.

**examples:** DOC_0063: Concentration data supports teachers changing presentation.; DOC_0987: GIS-linked analysis shapes school admissions routing.; DOC_0989: AI cameras monitor school kitchens for safety.

**boundary_examples:** DOC_0664: School knowledge benchmarking a model is not analysis of an educational future.; DOC_0351: AI text-origin checking belongs to integrity tools.

### OBJ_INTEGRITY_CHECK — Content integrity/origin checking

Tools evaluate originality, similarity, AI authorship or provenance of educational work.

**inclusion:** Text-origin/plagiarism checking and provenance techniques explicitly implicated in educational future judgment.

**exclusion:** Turnitin/Grammarly cannot be assumed to perform origin detection in every use; camera proctoring is monitoring.

**neighbours:** Distinguish from OBJ_AI_UNSPECIFIED, OBJ_AI_KNOWLEDGE, OBJ_CONTENT_LANGUAGE, OBJ_LEARNING_SYSTEM, OBJ_ANALYSIS_MONITORING, OBJ_EMBODIED_SIMULATION, OBJ_SYSTEM_INFRASTRUCTURE. Assign by the defined field relation; retain variants in required_qualifiers rather than generating extra labels.

**co_coding:** Allow distinct supported families within the same articulated account, with separate primary/secondary account IDs and evidence. Do not duplicate an umbrella family for a more specific referent; do not pool unrelated claims.

**examples:** DOC_0612: Detection tools serve integrity with human supervision.; DOC_0622: Detector-based punishment is a disputed educational ordering.

**boundary_examples:** DOC_0973: AI glasses being banned are answer-producing devices, not integrity detectors.

### OBJ_EMBODIED_SIMULATION — Embodied or simulated educational interfaces

AI enters education through physical robots or simulated/immersive practice environments.

**inclusion:** Robot tutors/practice objects and AI-linked virtual labs, XR or tactical/clinical simulations.

**exclusion:** Standalone VR/robotics background without AI educational relation; content generation alone.

**neighbours:** Distinguish from OBJ_AI_UNSPECIFIED, OBJ_AI_KNOWLEDGE, OBJ_CONTENT_LANGUAGE, OBJ_LEARNING_SYSTEM, OBJ_ANALYSIS_MONITORING, OBJ_INTEGRITY_CHECK, OBJ_SYSTEM_INFRASTRUCTURE. Assign by the defined field relation; retain variants in required_qualifiers rather than generating extra labels.

**co_coding:** Allow distinct supported families within the same articulated account, with separate primary/secondary account IDs and evidence. Do not duplicate an umbrella family for a more specific referent; do not pool unrelated claims.

**examples:** DOC_0007: Robot English teaching expands access.; DOC_0636: Educational robots enable STEM practice and future technical formation.

**boundary_examples:** DOC_0055: A robot student invention report without an educational future remains negative.; DOC_0966: Year2050 in a robot game is scenario content, not a projected real educational deadline.

### OBJ_SYSTEM_INFRASTRUCTURE — AI platforms, institutional systems and computing infrastructure

AI is envisaged as institution/platform-level capacity connecting or enabling teaching, study, research and administration.

**inclusion:** Computing labs/servers/AI PCs where research/learning capacity is itself projected; integrated institutional/native/national AI systems.

**exclusion:** Routine internet as a condition alone; a consumer tool bundle without integration; hardware product news lacking education.

**neighbours:** OBJ_LEARNING_SYSTEM for instructional interaction itself. Institution-wide integration or compute capacity, rather than a product list, establishes infrastructure.

**co_coding:** Allow distinct supported families within the same articulated account, with separate primary/secondary account IDs and evidence. Do not duplicate an umbrella family for a more specific referent; do not pool unrelated claims.

**examples:** DOC_0401: AI computing expands student and university research capacity.; DOC_1005: An integrated AI-native ecosystem connects university data and learning.

**boundary_examples:** DOC_0340: A hospital AI scanner is clinical care, not educational infrastructure.; DOC_0668: Free consumer tools are not automatically an institution-wide AI ecosystem.

## education_context

### CTX_TEACHING_STUDY — Teaching, curriculum and learner study

The future concerns organised curriculum, instruction or learner study itself, across levels and subjects.

**inclusion:** Class/home/tutored/self-study arrangements; curricular changes; language/STEM/arts/humanities/medical/legal/military/civic learning when actually implicated.

**exclusion:** No separate code for each grade, subject or delivery mode. Training an educator/professional cohort as such is capacity formation; determining achievement is assessment; learner services are institutional services.

**neighbours:** Compare the educational activity with CTX_CAPACITY_FORMATION, CTX_EXPERIENTIAL_RESEARCH, CTX_ASSESSMENT, CTX_ENTRY_GUIDANCE, CTX_INSTITUTIONAL_SERVICES. Stage, subject, audience and modality are qualifiers, not competing core categories.

**co_coding:** One code per explicitly articulated educational activity/account. Multiple activities only if the future actually reorganises each. Stage, subject, modality and audience are qualifiers and do not add core codes.

**examples:** DOC_0717: Teaching arranges exploration, learner reflection and human guidance.; DOC_0709: Supervised self-study distinguishes support from copying.; DOC_0695: Medical instruction and clinical practice retain discipline and ethics as qualifiers.

**boundary_examples:** DOC_0841: Applicant advising is admissions service, not teaching.; DOC_0340: University clinical scanner has no medical training future.

### CTX_CAPACITY_FORMATION — Educator, professional and public capacity formation

The educational future specifically organises preparation, continuing development or capability-building for educators, professionals or public/community learners.

**inclusion:** Preservice/inservice teacher education, professional bootcamps/reskilling and public/community AI or legal learning when capability formation is the educational setting.

**exclusion:** A teacher using AI while teaching pupils is instruction, not teacher formation; generic labour-market impact does not establish training; degree level alone belongs in qualifiers.

**neighbours:** Compare the educational activity with CTX_TEACHING_STUDY, CTX_EXPERIENTIAL_RESEARCH, CTX_ASSESSMENT, CTX_ENTRY_GUIDANCE, CTX_INSTITUTIONAL_SERVICES. Stage, subject, audience and modality are qualifiers, not competing core categories.

**co_coding:** One code per explicitly articulated educational activity/account. Multiple activities only if the future actually reorganises each. Stage, subject, modality and audience are qualifiers and do not add core codes.

**examples:** DOC_0144: AI prepares future teachers before school practicum.; DOC_1028: AI integrated teacher programmes form agents of educational change.; DOC_0497: Older residents learn practical AI and teach peers, a community capability-building setting.; DOC_0772: Professional communication training uses AI role-play.

**boundary_examples:** DOC_0217: Automated grading alone is teacher work, not teacher education.

### CTX_EXPERIENTIAL_RESEARCH — Experiential projects and research formation

The future develops learning/research capability through projects, clubs, contests, laboratories or scientific apprenticeship.

**inclusion:** Contest/project practice explicitly tied to formation; research residencies and supervised academic inquiry.

**exclusion:** Medal-only stories, AI product results and research findings do not by themselves constitute a future learning arrangement.

**neighbours:** Compare the educational activity with CTX_TEACHING_STUDY, CTX_CAPACITY_FORMATION, CTX_ASSESSMENT, CTX_ENTRY_GUIDANCE, CTX_INSTITUTIONAL_SERVICES. Stage, subject, audience and modality are qualifiers, not competing core categories.

**co_coding:** One code per explicitly articulated educational activity/account. Multiple activities only if the future actually reorganises each. Stage, subject, modality and audience are qualifiers and do not add core codes.

**examples:** DOC_0150: Research residency forms internationally capable AI researchers.; DOC_1084: ASEAN product co-creation teaches ethical regional collaboration.

**boundary_examples:** DOC_0637: Medal-only report has no articulated future formation.; DOC_0995: University medical AI findings alone are not researcher education.

### CTX_ASSESSMENT — Assessment, credentials and integrity

Educational achievement, knowledge, authorship or qualifications are verified/evaluated in the future arrangement.

**inclusion:** Examinations, grades, credential integrity and assessment design.

**exclusion:** Machine performance on exams alone; past offence with no projected educational ordering.

**neighbours:** Compare the educational activity with CTX_TEACHING_STUDY, CTX_CAPACITY_FORMATION, CTX_EXPERIENTIAL_RESEARCH, CTX_ENTRY_GUIDANCE, CTX_INSTITUTIONAL_SERVICES. Stage, subject, audience and modality are qualifiers, not competing core categories.

**co_coding:** One code per explicitly articulated educational activity/account. Multiple activities only if the future actually reorganises each. Stage, subject, modality and audience are qualifiers and do not add core codes.

**examples:** DOC_0650: AI-supported oral preparation plus handwritten testing restructures assessment.; DOC_0622: Detector punishment and alternative assessment concern educational judgment.

**boundary_examples:** DOC_0708: ChatGPT failing a Korean test illustrates difficulty without future assessment ordering.

### CTX_ENTRY_GUIDANCE — Admissions and educational/career guidance

The future concerns entry, enrolment, progression, programme choice or career guidance itself.

**inclusion:** Personal applicant advice, recruitment, admission essays/routing.

**exclusion:** An AI degree opening or labour-market aspiration alone is not AI-mediated guidance.

**neighbours:** Compare the educational activity with CTX_TEACHING_STUDY, CTX_CAPACITY_FORMATION, CTX_EXPERIENTIAL_RESEARCH, CTX_ASSESSMENT, CTX_INSTITUTIONAL_SERVICES. Stage, subject, audience and modality are qualifiers, not competing core categories.

**co_coding:** One code per explicitly articulated educational activity/account. Multiple activities only if the future actually reorganises each. Stage, subject, modality and audience are qualifiers and do not add core codes.

**examples:** DOC_0008: AI fills personal major-choice guidance gaps.; DOC_0822: AI advice matches applicants to programmes and study paths.

**boundary_examples:** DOC_0952: Fees/entry points report without educational future is excluded.

### CTX_INSTITUTIONAL_SERVICES — Management, educational services and learner care

Institutional/system operations or services supporting learners, including care/safety, are reorganised in the future.

**inclusion:** Administrative management, shared data, attendance, school counselling/health/kitchens and safeguarding.

**exclusion:** General clinical service in university hospital; principals speaking alone; exam fairness is assessment.

**neighbours:** Compare the educational activity with CTX_TEACHING_STUDY, CTX_CAPACITY_FORMATION, CTX_EXPERIENTIAL_RESEARCH, CTX_ASSESSMENT, CTX_ENTRY_GUIDANCE. Stage, subject, audience and modality are qualifiers, not competing core categories.

**co_coding:** One code per explicitly articulated educational activity/account. Multiple activities only if the future actually reorganises each. Stage, subject, modality and audience are qualifiers and do not add core codes.

**examples:** DOC_1081: Data-linked governance changes management and access.; DOC_0439: Human–AI counselling fills learner mental-health support gaps.; DOC_0989: Kitchen monitoring is a school safety service.

**boundary_examples:** DOC_0080: Clinical hospital diagnosis does not constitute learner care in education.

## timespan

### TIME_CALENDAR — Dated implementation or target

A specified date, school year or calendar interval bounds implementation/evaluation/outcome of the educational future.

**inclusion:** Future-linked calendar start, evaluation or strategic target.

**exclusion:** Event/publication/registration/past adoption dates and unrelated economic forecasts.

**neighbours:** TIME_CALENDAR names nonfiction dated targets; TIME_QUANTIFIED_HORIZON names numeric time-to-change; TIME_QUALITATIVE_HORIZON keeps near/enduring/open/fictional subtypes; TIME_RELATIONAL locates sequence/learning trajectory or provision-only organisation. These dimensions can coexist on one account; retain referents separately.

**co_coding:** Allow distinct supported families within the same articulated account, with separate primary/secondary account IDs and evidence. Do not duplicate an umbrella family for a more specific referent; do not pool unrelated claims.

**examples:** DOC_0714: Pilot12/2025–5/2026 and evaluation6/2026 bound rollout.; DOC_1061: 2026–2027 begins national school implementation.

**boundary_examples:** DOC_0950: Market forecast2035 is economic background, not educational horizon.

### TIME_QUANTIFIED_HORIZON — Quantified relative horizon

A stated number of months/years locates projected educational change relative to the present/reference point.

**inclusion:** In five years, within a decade,10–20years ahead.

**exclusion:** Course length, provision duration or past elapsed time is not time-to-future.

**neighbours:** TIME_CALENDAR names nonfiction dated targets; TIME_QUANTIFIED_HORIZON names numeric time-to-change; TIME_QUALITATIVE_HORIZON keeps near/enduring/open/fictional subtypes; TIME_RELATIONAL locates sequence/learning trajectory or provision-only organisation. These dimensions can coexist on one account; retain referents separately.

**co_coding:** Allow distinct supported families within the same articulated account, with separate primary/secondary account IDs and evidence. Do not duplicate an umbrella family for a more specific referent; do not pool unrelated claims.

**examples:** DOC_0711: Education prepares demands5–10 years ahead.; DOC_0731: AI youth capacity is tied to national advantage10–20 years ahead.

**boundary_examples:** DOC_0633: A12-week bootcamp specifies delivery duration rather than12weeks-to-social-future.

### TIME_QUALITATIVE_HORIZON — Explicit qualitative future horizon

Future timing is explicitly immediate/near, extended/enduring, open or speculative without a nonfiction quantified relative horizon.

**inclusion:** Soon, urgent now, long-term, someday, future generation; fictional chronology retained as explicit secondary qualifier.

**exclusion:** No temporal specification is MISSING. Do not infer urgency or long-term duration from policy topic. Fiction is not a real implementation target.

**neighbours:** TIME_CALENDAR names nonfiction dated targets; TIME_QUANTIFIED_HORIZON names numeric time-to-change; TIME_QUALITATIVE_HORIZON keeps near/enduring/open/fictional subtypes; TIME_RELATIONAL locates sequence/learning trajectory or provision-only organisation. These dimensions can coexist on one account; retain referents separately.

**co_coding:** Allow distinct supported families within the same articulated account, with separate primary/secondary account IDs and evidence. Do not duplicate an umbrella family for a more specific referent; do not pool unrelated claims.

**examples:** DOC_0590: Urgent action and long-term digital ethics are distinct supported temporal qualifiers.; DOC_0629: Long-term strategy states endurance rather than a numeric deadline.; DOC_0321: One day states an open horizon.

**boundary_examples:** DOC_0717: An undated normative classroom is MISSING unless a temporal phrase is present.; DOC_0701: 2525 belongs only to fiction, retained as a secondary qualifier, not a real dated target.

### TIME_RELATIONAL — Relational or staged educational timing

Educational timing is explicitly anchored to an educational stage, transition, implementation sequence or bounded provision rather than a calendar/date-to-future claim.

**inclusion:** After pilot evaluation, after graduation, across a learning life; duration/cadence of planned educational provision where that is the only stated temporal organisation.

**exclusion:** A contextual age/grade or historical duration alone; software availability24/7 and device support warranty alone; mere conditional desirability without temporal ordering.

**neighbours:** TIME_CALENDAR names nonfiction dated targets; TIME_QUANTIFIED_HORIZON names numeric time-to-change; TIME_QUALITATIVE_HORIZON keeps near/enduring/open/fictional subtypes; TIME_RELATIONAL locates sequence/learning trajectory or provision-only organisation. These dimensions can coexist on one account; retain referents separately.

**co_coding:** Allow distinct supported families within the same articulated account, with separate primary/secondary account IDs and evidence. Do not duplicate an umbrella family for a more specific referent; do not pool unrelated claims.

**examples:** DOC_0727: Review pilot before expansion specifies implementation sequence.; DOC_0732: After graduation anchors projected capability consequences.; DOC_0783: Learning throughout life is a life-course relation.; DOC_1044: Annual lessons specify provision cadence only; do not infer deadline for intended citizenship.

**boundary_examples:** DOC_1038: Four-year device security support is not educational timing.; DOC_0607: 24/7 chatbot availability alone does not locate educational future.

## space

### SPACE_BOUNDED_SITE — Bounded institution, community or educational site

Future reach is bounded to a named institution/network/local community or explicitly specified learning site topology.

**inclusion:** Named school/university/network, neighbourhood, school–home/lab/museum relations; preserve whether institutional, territorial or site type.

**exclusion:** Affiliation, residence or conference venue alone cannot locate the future; a school label does not automatically establish territorial scope.

**neighbours:** Distinguish from SPACE_TERRITORIAL_SYSTEM, SPACE_SUPRANATIONAL, SPACE_LOCATION_INDEPENDENT, SPACE_UNEQUAL_REACH. Assign by the defined field relation; retain variants in required_qualifiers rather than generating extra labels.

**co_coding:** Do not double-code the same reach merely because nested scales or access/inequality details coexist. Retain explicit nested scope as qualifiers (pilot/site versus intended scale). Multiple core scopes only for separately articulated reaches/accounts.

**examples:** DOC_0271: CMCU future applies to its own operations.; DOC_0497: Neighbourhood learning extends to nearby wards.; DOC_0964: Personal-device research is arranged across lecture room and home.

**boundary_examples:** DOC_0354: RMIT conference location does not bound all higher-education proposals.; DOC_0706: US training experience does not locate the author classroom future in the US.

### SPACE_TERRITORIAL_SYSTEM — Subnational or national-system scope

A future explicitly applies to a named city/province/region or country/national education system.

**inclusion:** Provincial/city rollout and nationwide reform; preserve exact scale and territory.

**exclusion:** Multiple local anecdotes do not imply regional/national rollout; Vietnamese voice/brand does not imply Vietnamese scope.

**neighbours:** SPACE_BOUNDED_SITE for a school/community rather than territorial system; SPACE_SUPRANATIONAL for explicit cross-border reach. City/province/national subtypes and country names are mandatory.

**co_coding:** Do not double-code the same reach merely because nested scales or access/inequality details coexist. Retain explicit nested scope as qualifiers (pilot/site versus intended scale). Multiple core scopes only for separately articulated reaches/accounts.

**examples:** DOC_0653: Teacher preparation applies across Hưng Yên.; DOC_0714: Uniform guidance has national reach.; DOC_0537: US school policy locates a national-system future.

**boundary_examples:** DOC_0716: Short retained proposal lacks stated geographic scope; do not infer it from ministry alone.; DOC_0726: Three school examples do not establish multi-province rollout.

### SPACE_SUPRANATIONAL — Cross-border, regional or worldwide scope

The educational future explicitly crosses countries through regional cooperation, international access or worldwide reach.

**inclusion:** Named cross-border learning/research links, ASEAN formation, all-country/global education ordering.

**exclusion:** Foreign examples or attendees, product origins, rankings and online access alone do not imply international reach.

**neighbours:** Distinguish from SPACE_BOUNDED_SITE, SPACE_TERRITORIAL_SYSTEM, SPACE_LOCATION_INDEPENDENT, SPACE_UNEQUAL_REACH. Assign by the defined field relation; retain variants in required_qualifiers rather than generating extra labels.

**co_coding:** Do not double-code the same reach merely because nested scales or access/inequality details coexist. Retain explicit nested scope as qualifiers (pilot/site versus intended scale). Multiple core scopes only for separately articulated reaches/accounts.

**examples:** DOC_0150: Formation connects Vietnam and Canadian research training.; DOC_1084: ASEAN learning collaboration has regional reach.; DOC_0135: Educational authority/fairness is discussed worldwide.

**boundary_examples:** DOC_0731: Foreign examples do not make the Vietnam proposal a cross-border arrangement.; DOC_0298: Global ranking ambition is not global education deployment.

### SPACE_UNBOUNDED_ACCESS — Explicit access without bounded geography

The future explicitly removes physical-location limits but specifies no bounded territorial or institutional reach for that access claim.

**inclusion:** Learners anywhere, mobile/remote access not bounded by a stated country/institution; if a territory is also stated, keep the appropriate territorial core and access as qualifier.

**exclusion:** No place information is MISSING; online platform alone is insufficient;24/7 is temporal availability; anywhere does not imply every country or an actual global rollout.

**neighbours:** Distinguish from SPACE_BOUNDED_SITE, SPACE_TERRITORIAL_SYSTEM, SPACE_SUPRANATIONAL, SPACE_UNEQUAL_REACH. Assign by the defined field relation; retain variants in required_qualifiers rather than generating extra labels.

**co_coding:** Do not double-code the same reach merely because nested scales or access/inequality details coexist. Retain explicit nested scope as qualifiers (pilot/site versus intended scale). Multiple core scopes only for separately articulated reaches/accounts.

**examples:** DOC_0569: Learning anywhere on a phone articulates location-independent access without stated geographic reach.; DOC_0843: Access extends beyond major centres; preserve any nationally bounded scope if source states it.

**boundary_examples:** DOC_0086: Country-wide service has a territorial core with location-independent access qualifier, rather than a second competing scope.

## speaker

### SPK_PUBLIC_AUTHORITY — Public authority

A voiced educational-future proposition presented through statutory policy, governmental or security authority.

**inclusion:** Government, legislature, ministries, local education authorities, police or public exam authorities speaking in that capacity.

**exclusion:** A public university employee is not automatically a government voice; an official named only in event background is not a speaker.

**neighbours:** SPK_EDUCATION_ORGANIZATION: statutory system-level authority versus institutional educational leadership.

**co_coding:** Allowed only for separately evidenced roles or propositions within the same educational-future account. Preserve speaker identity and primary/secondary account linkage; never transfer a role automatically between fields.

**examples:** DOC_0295: Prime Minister assigns national educational AI-development duties.; DOC_0913: Police authority prescribes prevention and training against AI-enabled exam fraud.

**boundary_examples:** DOC_0967: Named education officials in a current incident do not establish an educational-future proposition.

### SPK_EDUCATION_ORGANIZATION — Educational organization or leadership

A voiced proposition representing an educational institution, its leadership or program commitments.

**inclusion:** School/university leadership and institutionally communicated future models; organizational commitments reported without a named spokesperson.

**exclusion:** Do not infer an institutional position from every lecturer quotation or neutral event description.

**neighbours:** SPK_EDUCATOR concerns teaching practice; SPK_PUBLIC_AUTHORITY statutory authority; SPK_COMMERCIAL_ACTOR commercial capacity.

**co_coding:** Allowed only for separately evidenced roles or propositions within the same educational-future account. Preserve speaker identity and primary/secondary account linkage; never transfer a role automatically between fields.

**examples:** DOC_1005: CMC leadership presents an AI-integrated institutional redesign.; DOC_1039: Primary school head explains an AI curriculum and balanced activities.

**boundary_examples:** DOC_0953: Publication of predicted admission scores alone is not a future-model voice.

### SPK_EDUCATOR — Educator

A future proposition grounded explicitly in teaching, assessment or learner-guidance practice.

**inclusion:** Practising teachers, tutors and lecturers speaking as educators; first-person teacher arguments.

**exclusion:** Academic affiliation alone; research findings voiced in expert rather than teaching capacity.

**neighbours:** SPK_EXPERT: epistemic research/advisory warrant versus teaching practice; SPK_AUTHOR_ARGUMENT can accompany an independently explicit first-person educator role.

**co_coding:** Allowed only for separately evidenced roles or propositions within the same educational-future account. Preserve speaker identity and primary/secondary account linkage; never transfer a role automatically between fields.

**examples:** DOC_0706: Tutor argues for trust and changed classroom assignments.; DOC_0984: First-person lecturer proposes disclosure and process-based assessment.

**boundary_examples:** DOC_0946: Researchers explaining skill loss are expert voices, not automatically educators.

### SPK_EXPERT — Research or advisory expert

A voiced future proposition warranted by research, specialist analysis or professional educational advice.

**inclusion:** Named or explicitly attributed unnamed scholars, studies and specialists interpreting educational futures.

**exclusion:** Do not count every named academic as an expert speaker; company title alone does not imply independent expertise.

**neighbours:** SPK_EDUCATOR practice; SPK_COMMERCIAL_ACTOR product/employer position; SPK_CIVIC_COLLECTIVE represents organizational advocacy.

**co_coding:** Allowed only for separately evidenced roles or propositions within the same educational-future account. Preserve speaker identity and primary/secondary account linkage; never transfer a role automatically between fields.

**examples:** DOC_0940: Ali Al-Dulaimi explains integrity, assessment and unequal-access implications.; DOC_0946: Researchers discuss which skills users should retain or delegate.

**boundary_examples:** DOC_1057: An inadequate source cannot establish a substantive expert category even if its snippet names policy.

### SPK_COMMERCIAL_ACTOR — Commercial actor

A voiced future proposition representing product provision, commercial strategy or employer demand.

**inclusion:** AI/EdTech firms, technology suppliers and employers articulating educational models, skills or investments.

**exclusion:** A sponsor merely listed is not a voice; do not classify by presumed profit motive.

**neighbours:** SPK_EDUCATION_ORGANIZATION: educational institutional capacity, including private institutions; preserve explicit dual capacities rather than infer them.

**co_coding:** Allowed only for separately evidenced roles or propositions within the same educational-future account. Preserve speaker identity and primary/secondary account linkage; never transfer a role automatically between fields.

**examples:** DOC_0936: Google/NotebookLM leadership articulates source-based learning support.; DOC_0993: DENSO explains industry-linked student project development.

**boundary_examples:** DOC_0711: A captioned corporate participant alone does not demonstrate a voiced proposition.

### SPK_LEARNER — Learner

A voiced proposition from a learner about an educational future, its desirability or conditions.

**inclusion:** Pupils, students, trainees and lifelong learners; clearly attributed learner survey positions.

**exclusion:** Being an affected student or project creator does not by itself constitute speaking.

**neighbours:** SPK_EXPERT when the same person speaks through specialist analysis; retain stage/status as qualifiers.

**co_coding:** Allowed only for separately evidenced roles or propositions within the same educational-future account. Preserve speaker identity and primary/secondary account linkage; never transfer a role automatically between fields.

**examples:** DOC_0928: Students advocate selective supportive AI use without dependence.; DOC_0654: Learner calls for critical dialogue and institutional conditions.

**boundary_examples:** DOC_0871: A student medical project without an educational future does not supply a learner-future voice.

### SPK_FAMILY — Family or caregiver

A voiced educational-future proposition grounded in parenting or caregiving.

**inclusion:** Parents/caregivers expressing expectations, objections or desired learning conditions; attributed parent survey accounts.

**exclusion:** A parent mentioned only as affected or as an escort is not automatically a future speaker.

**neighbours:** SPK_CIVIC_COLLECTIVE for general public positions; retain organized parent group identity here when parental capacity grounds the claim.

**co_coding:** Allowed only for separately evidenced roles or propositions within the same educational-future account. Preserve speaker identity and primary/secondary account linkage; never transfer a role automatically between fields.

**examples:** DOC_0651: Parent-oriented account calls for boundaries and children thinking independently.; DOC_1048: Parent groups call for schools to pause AI deployment.

**boundary_examples:** DOC_1015: Teaser from another article is inadequate evidence and must not supply parenting propositions.

### SPK_CIVIC_COLLECTIVE — Civic, professional or public voice

A voiced proposition from a noncommercial collective, professional/intergovernmental organization, organizer or attributed public commentary.

**inclusion:** UNESCO and professional associations; NGOs; contest/community organizers; readers and social-media publics articulating educational futures.

**exclusion:** Listed partners without propositions; do not infer that unnamed experts are public opinion.

**neighbours:** SPK_EXPERT for expert analysis rather than collective representation; SPK_FAMILY for parental capacity; retain NGO/intergovernmental/public/organizer subtype in raw qualifiers.

**co_coding:** Allowed only for separately evidenced roles or propositions within the same educational-future account. Preserve speaker identity and primary/secondary account linkage; never transfer a role automatically between fields.

**examples:** DOC_0170: UNESCO advances safe educational AI governance.; DOC_1013: Attributed online commenters challenge the educational effectiveness of AI traps.

**boundary_examples:** DOC_0918: A public technology prediction unrelated to educational arrangements is outside eligibility.

### SPK_AUTHOR_ARGUMENT — Article author argument

The article itself articulates or evaluates an educational future in an authorial voice.

**inclusion:** Explicit normative, evaluative or interpretive argument, named or unnamed; commercial narration only when it itself advances a future proposition.

**exclusion:** Neutral bylines, attribution of others, reporting facts or a headline alone.

**neighbours:** All other speaker codes: identify whose proposition it is; do not add author merely because reporting is mediated.

**co_coding:** Allowed only for separately evidenced roles or propositions within the same educational-future account. Preserve speaker identity and primary/secondary account linkage; never transfer a role automatically between fields.

**examples:** DOC_0969: Author argues for evidence, diversity and human purposes in educational reform.; DOC_1041: Teacher-author argues for care and process-based learning in the AI future.

**boundary_examples:** DOC_0857: Inadequate VOV text and a byline do not establish authorial argument.

## affected_entities

### AFFECT_LEARNERS — Learners

People whose learning, capability, autonomy, participation or educational trajectory is positioned as changed by the future.

**inclusion:** All educational stages; adult, professional and lifelong learners; prospective learners where their educational choice is implicated.

**exclusion:** A generic user, worker or patient without an educational relation; do not treat a skill itself as a separate actor.

**neighbours:** AFFECT_EDUCATION_PROFESSIONALS when teaching/research work changes; AFFECT_WIDER_COLLECTIVE for collective workforce/national effects.

**co_coding:** Allowed only for separately evidenced roles or propositions within the same educational-future account. Preserve speaker identity and primary/secondary account linkage; never transfer a role automatically between fields.

**examples:** DOC_0928: Students independent thought and creativity are affected.; DOC_0497: Older adults learning AI are explicitly included.

**boundary_examples:** DOC_0774: AI exam performance is not evidence of human learner effects.

### AFFECT_EDUCATION_PROFESSIONALS — Education and research professionals

People whose teaching, educational management or academic research work/identity is affected.

**inclusion:** Teachers, lecturers, school managers and academic researchers; teacher trainees may also be learners if both relations are explicit.

**exclusion:** A named expert speaking does not automatically become affected; noneducational occupations require another relation.

**neighbours:** AFFECT_EDUCATION_ORGANIZATIONS for institutional arrangements rather than individual work.

**co_coding:** Allowed only for separately evidenced roles or propositions within the same educational-future account. Preserve speaker identity and primary/secondary account linkage; never transfer a role automatically between fields.

**examples:** DOC_0939: Future teachers and teacher trainees need changed competence.; DOC_0961: Young researchers and educators face integrity and capability requirements.

**boundary_examples:** DOC_0936: A product leader speaker is not automatically an affected educator.

### AFFECT_EDUCATION_ORGANIZATIONS — Educational organizations and arrangements

Institutions and collective educational arrangements explicitly positioned as transformed or at stake.

**inclusion:** Schools, universities, programs, institutional governance, assessment integrity and public trust in qualifications when explicitly implicated.

**exclusion:** Do not invent an institution for every student effect; abstract creativity or values alone are not institutional entities.

**neighbours:** AFFECT_EDUCATION_PROFESSIONALS individuals; AFFECT_WIDER_COLLECTIVE social consequences.

**co_coding:** Allowed only for separately evidenced roles or propositions within the same educational-future account. Preserve speaker identity and primary/secondary account linkage; never transfer a role automatically between fields.

**examples:** DOC_1005: University structures and governance are redesigned.; DOC_0868: Honor-system examination and institutional trust are at stake.

**boundary_examples:** DOC_0928: Individual student autonomy alone does not imply an affected institution.

### AFFECT_FAMILIES — Families and caregivers

Families whose educational participation, care, choices or resources are affected.

**inclusion:** Parent participation, school-home relations, educational spending or caregiving burdens explicitly implicated.

**exclusion:** Parent spokesperson alone is insufficient; ordinary mention of a family is not an affected educational relation.

**neighbours:** AFFECT_LEARNERS children; AFFECT_WIDER_COLLECTIVE wider public.

**co_coding:** Allowed only for separately evidenced roles or propositions within the same educational-future account. Preserve speaker identity and primary/secondary account linkage; never transfer a role automatically between fields.

**examples:** DOC_0987: Parents must navigate changed admission infrastructure.; DOC_1031: Parents are affected by minors AI deployment and school permissions.

**boundary_examples:** DOC_1039: Separate parent expectations from actual attributed impacts; voice alone does not establish all effects.

### AFFECT_MARKET_PROFESSIONS — Employers and occupational communities

Organizations or professional communities affected through education-to-work relations or educational provision markets.

**inclusion:** Employers, industry, educational providers/investors and occupational groups explicitly affected by future training, qualifications or educational business arrangements.

**exclusion:** Do not infer commercial benefit whenever a company provides resources; generic labour automation without educational relation is outside scope.

**neighbours:** AFFECT_LEARNERS for individual reskilling; AFFECT_WIDER_COLLECTIVE national workforce.

**co_coding:** Allowed only for separately evidenced roles or propositions within the same educational-future account. Preserve speaker identity and primary/secondary account linkage; never transfer a role automatically between fields.

**examples:** DOC_1008: Student project training links to businesses and economic needs.; DOC_0478: Educational franchise investors are implicated in the proposed model.

**boundary_examples:** DOC_1058: Google providing a free student plan does not by itself establish Google as affected beneficiary.

### AFFECT_WIDER_COLLECTIVE — Wider community and shared inheritance

A social collective or shared cultural/knowledge resource explicitly affected through the educational future.

**inclusion:** Communities, citizens, national/regional development, collective workforce, cultural heritage and shared knowledge when the educational link is explicit.

**exclusion:** General national AI optimism or any unrelated social application; no presumed nationwide benefit from a local tool.

**neighbours:** AFFECT_MARKET_PROFESSIONS occupational/market beneficiaries; retain country, community and cultural-resource subtype in raw.

**co_coding:** Allowed only for separately evidenced roles or propositions within the same educational-future account. Preserve speaker identity and primary/secondary account linkage; never transfer a role automatically between fields.

**examples:** DOC_1003: Educational formation is linked explicitly to future citizens and national workforce.; DOC_1089: Art education links young people, community and preservation of cultural heritage.

**boundary_examples:** DOC_0487: A music technology project without educational-future articulation is not sufficient.

## action

### ACT_CURRICULUM — Reconfigure curriculum and educational aims

Change what education formally cultivates, offers or recognizes in response to an AI future.

**inclusion:** Integrate AI/ethics across disciplines, introduce programs, revise outcomes or educational purpose and duration.

**exclusion:** Generic career choice or tool launch without curricular change.

**neighbours:** ACT_LEARNING_ASSESSMENT changes how learning/assessment proceeds; ACT_RESOURCE_IMPLEMENTATION prepares actors to implement.

**co_coding:** Allowed only for separately evidenced roles or propositions within the same educational-future account. Preserve speaker identity and primary/secondary account linkage; never transfer a role automatically between fields.

**examples:** DOC_0974: Higher education programs and outcomes integrate AI.; DOC_0939: Teacher education integrates digital, ethical and adaptable capabilities.

**boundary_examples:** DOC_0962: Buying an AI laptop is not curriculum reform.

### ACT_LEARNING_ASSESSMENT — Reorganize learning and assessment

Change how people learn, teach, demonstrate understanding or receive guidance while retaining an educational purpose.

**inclusion:** Projects, dialogue, personalized/flipped learning, self-study routines, foundational practice, human care, oral/process/authentic assessment and learner guidance.

**exclusion:** Tool availability alone, policing exams alone or merely predicting a skill requirement.

**neighbours:** ACT_CURRICULUM substantive aims/content; ACT_GOVERN_SAFEGUARD prevention/sanction; retain pedagogy, self-practice, assessment, guidance subtype.

**co_coding:** Allowed only for separately evidenced roles or propositions within the same educational-future account. Preserve speaker identity and primary/secondary account linkage; never transfer a role automatically between fields.

**examples:** DOC_0982: Flipped practice, classroom discussion and solve-before-AI routines.; DOC_0948: Process and oral assessment emphasize analysis rather than detector dependence.

**boundary_examples:** DOC_0913: Scanning exam devices prevents fraud; it does not itself redesign evidence of learning.

### ACT_RESOURCE_IMPLEMENTATION — Develop capacity and provide educational resources

Actors build the human or material capacity needed to enact the educational future through preparation, financing, tools, data, facilities or access provision.

**inclusion:** An explicit implementing-actor preparation or resource/provision action.

**exclusion:** Ordinary learner coursework alone; product existence without an action linked to the future.

**neighbours:** Use the changed educational relation, not the technology or its overall reputation, to distinguish neighbouring roles.

**co_coding:** Code distinct supported relations within one attributed future account. Preserve facets, direction and evaluation separately; do not borrow another speaker’s rationale or stance.

**required_facets:** resource: implementer capability / finance / tools-data-materials / facilities-access / other source wording

**examples:** DOC_1093: Teacher training combines safety, lesson design and adapted assessment.; DOC_0522: Regional trainer preparation is intended to spread educational capability.; DOC_1000: Labs, deidentified data, scholarships and internships are provided.; DOC_1058: Google provides student services and learning spaces.

**boundary_examples:** DOC_0928: A student choosing to think critically is learning practice, not workforce training of implementers.; DOC_0668: Free subscription eligibility alone is not proof of equitable educational access.

### ACT_GOVERN_SAFEGUARD — Govern, safeguard and hold educational use accountable

Actors shape the permissible and accountable educational arrangement through rules, safeguards, retained human judgment, restrictions or enforcement. Enabling safeguards and prohibitions remain distinct interventions.

**inclusion:** A source-stated governance, rights-protection, human oversight, restriction or compliance action tied to the educational future.

**exclusion:** A harm forecast with no action; treating every rule as prohibition or every safeguard as endorsement.

**neighbours:** Use the changed educational relation, not the technology or its overall reputation, to distinguish neighbouring roles.

**co_coding:** Code distinct supported relations within one attributed future account. Preserve facets, direction and evaluation separately; do not borrow another speaker’s rationale or stance.

**required_facets:** intervention: enabling rules / human oversight / protection / restriction / enforcement / other source wording; target and responsible actor

**examples:** DOC_0954: Institutional AI rules, integrity and provider duties are prescribed.; DOC_0984: Lecturer proposes shared disclosure rules and school/national policy.; DOC_1052: Human experts screen narrative content before visually impaired children receive it.; DOC_0979: Controlled trials and human invigilator decisions safeguard exam use.; DOC_1048: Parent and district accounts call for a pause or permission controls.; DOC_0916: Police enforce exam security and prohibit assisting fraud.

**boundary_examples:** DOC_1038: A provider simply designing a product is not educational governance unless rules are specified.; DOC_0850: Warnings about future cognitive loss do not by themselves prescribe protective steps.; DOC_0948: Avoiding detector reliance and redesigning assessment does not imply an AI ban.

### ACT_COLLABORATION — Coordinate and mobilize educational relationships

Construct relations among actors to realize the future or communicate it publicly.

**inclusion:** School-industry collaboration, expert/community networks, joint competitions, mentoring ecosystems, consultations and public educational outreach.

**exclusion:** Co-mention or a list of event attendees is not collaboration; resource provision alone is insufficient.

**neighbours:** ACT_RESOURCE_IMPLEMENTATION resources; ACT_RESOURCE_IMPLEMENTATION training; preserve partnership, competition and public outreach facets.

**co_coding:** Allowed only for separately evidenced roles or propositions within the same educational-future account. Preserve speaker identity and primary/secondary account linkage; never transfer a role automatically between fields.

**examples:** DOC_1084: Regional contest links students, experts and prototype development.; DOC_1089: School-artisan-community ecosystem connects cultural education.

**boundary_examples:** DOC_0711: A captioned partner without an articulated coordinating action is insufficient.

### ACT_EVIDENCE_ADAPTATION — Investigate and adapt with evidence

Generate or use evidence to decide whether and how the educational future should proceed.

**inclusion:** Pilots, independent evaluation, research, feedback, monitoring impacts and revising designs after results.

**exclusion:** A study cited merely to describe harm is a rationale/evidence, not automatically a proposed action.

**neighbours:** ACT_GOVERN_SAFEGUARD formal accountability measures; ACT_GOVERN_SAFEGUARD verifying individual outputs.

**co_coding:** Allowed only for separately evidenced roles or propositions within the same educational-future account. Preserve speaker identity and primary/secondary account linkage; never transfer a role automatically between fields.

**examples:** DOC_0674: Controlled educational trial measures the proposed approach.; DOC_0969: Author requires evidence-based educational reform and evaluation of progress.

**boundary_examples:** DOC_0946: Reported study results alone should not be coded as a newly prescribed trial.

## responsibility

### RESP_PUBLIC_AUTHORITY — Public authority

Governmental, legislative, public administration or security actors explicitly assigned work/accountability for the future.

**inclusion:** Central/local ministries and authorities, police, public examination boards and statutory public agencies; preserve level and function.

**exclusion:** Do not infer government accountability from Vietnam location or public institutional affiliation.

**neighbours:** RESP_EDUCATION_ORGANIZATION for school/university own delivery duties.

**co_coding:** Allowed only for separately evidenced roles or propositions within the same educational-future account. Preserve speaker identity and primary/secondary account linkage; never transfer a role automatically between fields.

**examples:** DOC_0295: Government assigns ministry duties.; DOC_1063: Sở and provincial government are assigned implementation/resource duties.

**boundary_examples:** DOC_0946: Research warnings without a governmental assignment do not imply state responsibility.

### RESP_EDUCATION_ORGANIZATION — Educational organization

An educational institution or its internal organizational units explicitly charged with realizing or governing the future.

**inclusion:** School/university, department, institutional leadership and local school exam administration acting institutionally.

**exclusion:** Do not copy institutional speaker to responsibility when no work is assigned.

**neighbours:** RESP_PUBLIC_AUTHORITY statutory policy/exam authority; RESP_EDUCATION_PROFESSIONALS individual instructional/research tasks.

**co_coding:** Allowed only for separately evidenced roles or propositions within the same educational-future account. Preserve speaker identity and primary/secondary account linkage; never transfer a role automatically between fields.

**examples:** DOC_0974: Institutions autonomously design and assure program quality.; DOC_1005: University and departments implement redesigned structures.

**boundary_examples:** DOC_0947: Product positioning with unspecified responsibility cannot imply university duties.

### RESP_EDUCATION_PROFESSIONALS — Education and research professionals

Teachers, instructors, researchers or educational specialists explicitly charged with instructional, evaluative or research work.

**inclusion:** Design learning/assessment, guide students, verify materials, conduct research, mentor and make professional judgments.

**exclusion:** A quoted expert is not automatically responsible; affiliation does not establish a task.

**neighbours:** RESP_EDUCATION_ORGANIZATION collective policy/delivery; RESP_LEARNER_USER own learning/output duties.

**co_coding:** Allowed only for separately evidenced roles or propositions within the same educational-future account. Preserve speaker identity and primary/secondary account linkage; never transfer a role automatically between fields.

**examples:** DOC_0982: Lecturers design and guide critical flipped learning.; DOC_1052: Teachers/specialists screen material and researchers complete development.

**boundary_examples:** DOC_0940: An expert explaining risks is not automatically assigned every institutional duty discussed.

### RESP_LEARNER_USER — Learner or educational user

Individuals explicitly charged with their learning choices, conduct, AI outputs or demonstration of understanding.

**inclusion:** Students/trainees, educational users and researchers acting as accountable users; own checking, disclosure, self-study, choices and project development.

**exclusion:** Being affected does not entail responsibility; do not turn a predicted skill need into an obligation absent prescription.

**neighbours:** RESP_EDUCATION_PROFESSIONALS professional guidance/research; retain user role if the same person has both explicit tasks.

**co_coding:** Allowed only for separately evidenced roles or propositions within the same educational-future account. Preserve speaker identity and primary/secondary account linkage; never transfer a role automatically between fields.

**examples:** DOC_0999: Students are to judge use and assume responsibility.; DOC_0984: Students disclose, verify and remain responsible for work.

**boundary_examples:** DOC_0975: Future affected learners with no specified duty remain missing for responsibility.

### RESP_FAMILY — Family or caregiver

Parents/caregivers explicitly assigned educational support, supervision, decisions or restraint.

**inclusion:** Guidance, safety supervision, admission preparation, supporting learning and refusing complicity in fraud.

**exclusion:** Parent concerns or expectations alone are not duties; do not assume all child education makes parents responsible.

**neighbours:** RESP_LEARNER_USER childs duties; RESP_COMMUNITY collective organizing.

**co_coding:** Allowed only for separately evidenced roles or propositions within the same educational-future account. Preserve speaker identity and primary/secondary account linkage; never transfer a role automatically between fields.

**examples:** DOC_0916: Parents must not assist exam fraud.; DOC_1020: Parents support handwriting, music and cautious early AI use.

**boundary_examples:** DOC_1039: Parent expectations do not themselves assign parents extra work.

### RESP_COMMERCIAL_ACTOR — Commercial provider or employer

A company/provider/employer explicitly assigned provision, design, resource or partnership duties.

**inclusion:** Develop/safeguard tools, provide data/resources, finance or mentor, host practical work and comply with educational standards.

**exclusion:** A company named, promoted or benefiting does not automatically have a duty.

**neighbours:** RESP_EDUCATION_ORGANIZATION private school pedagogical duties; preserve provider versus employer/funder role as qualifier.

**co_coding:** Allowed only for separately evidenced roles or propositions within the same educational-future account. Preserve speaker identity and primary/secondary account linkage; never transfer a role automatically between fields.

**examples:** DOC_0954: Platform providers must meet standards and transfer data.; DOC_1000: SHB provides resources, problems, data and experts.

**boundary_examples:** DOC_0668: Student subscription instructions alone do not assign broad provider educational accountability.

### RESP_COMMUNITY — Civic, professional or collective actor

An explicitly charged civic/professional collective, organizer, community or broadly stated human collective.

**inclusion:** NGOs, associations, international organizations, volunteer networks, media organizers, community participants; explicit we/society/conhuman obligations with referent retained.

**exclusion:** No inferred all-society responsibility from unspecified passive prescriptions.

**neighbours:** RESP_PUBLIC_AUTHORITY governmental authority; RESP_EDUCATION_PROFESSIONALS individual specialist work; retain named/unspecified collective facet.

**co_coding:** Allowed only for separately evidenced roles or propositions within the same educational-future account. Preserve speaker identity and primary/secondary account linkage; never transfer a role automatically between fields.

**examples:** DOC_1089: Artisans, artists and community join the educational ecosystem.; DOC_1093: UNICEF and project organizations support teacher training.

**boundary_examples:** DOC_1032: Call to tighten exams with responsibility not specified must not become generic community duty.

## Thay đổi từ v1.0

| Mã trước | Bản sửa |
|---|---|
| FR_SPECIALIST_FORMATION | FR_CAPABILITY_PATHWAYS |
| FR_AI_LITERACY | FR_CAPABILITY_PATHWAYS |
| FR_WORK_LIFE_ADAPTATION | FR_CAPABILITY_PATHWAYS |
| FR_COGNITIVE_AGENCY | FR_COGNITION_AGENCY |
| FR_COGNITIVE_EROSION | FR_COGNITION_AGENCY |
| FR_TEACHER_AUGMENTATION | FR_TEACHING_LABOUR |
| FR_TEACHER_DISPLACEMENT | FR_TEACHING_LABOUR |
| FR_ASSESSMENT_REDESIGN | FR_ACADEMIC_JUDGMENT |
| FR_INTEGRITY_CONTROL | FR_ACADEMIC_JUDGMENT |
| FR_ACCESS_INCLUSION | FR_ACCESS_DISTRIBUTION |
| FR_WELLBEING_PROTECTION | FR_WELLBEING_RELATIONS |
| RATION_PEDAGOGIC_DESIGN | RATION_LEARNING_DEVELOPMENT |
| RATION_ACTIVE_LEARNING | RATION_LEARNING_DEVELOPMENT |
| RATION_PRACTICE_TRANSFER | RATION_LEARNING_DEVELOPMENT |
| RATION_CAPACITY_WORKLOAD | RATION_RESOURCES_READINESS |
| RATION_FEASIBILITY | RATION_RESOURCES_READINESS |
| RATION_RELIABILITY_CONTEXT | RATION_TRUST_ACCOUNTABILITY |
| RATION_INTEGRITY | RATION_TRUST_ACCOUNTABILITY |
| RATION_RIGHTS_DATA | RATION_TRUST_ACCOUNTABILITY |
| RATION_NATIONAL_STANDING | RATION_COLLECTIVE_SELFDETERMINATION |
| RATION_SOVEREIGNTY | RATION_COLLECTIVE_SELFDETERMINATION |
| ACT_GOVERNANCE | ACT_GOVERN_SAFEGUARD |
| ACT_SAFEGUARD_JUDGMENT | ACT_GOVERN_SAFEGUARD |
| ACT_RESTRICTION_ENFORCEMENT | ACT_GOVERN_SAFEGUARD |
| ACT_CAPABILITY_DEVELOPMENT | ACT_RESOURCE_IMPLEMENTATION |
| ACT_PROVISION | ACT_RESOURCE_IMPLEMENTATION |
| CERT_ASSERTIVE | CERT_ASSERTED |
| CERT_INEVITABLE | CERT_ASSERTED |
| CERT_ASPIRATIONAL | CERT_INTENDED |
| CERT_COMMITMENT | CERT_INTENDED |
| DES_ENDORSED | DES_POSITIVE |
| DES_QUALIFIED | DES_POSITIVE |
| DES_HARMFUL | DES_NEGATIVE |
| DES_REJECTED | target-dependent evaluation + stance qualifier; no automatic valence mapping |

## Giới hạn

Áp dụng phiên bản được chốt theo trạng thái trên; mọi sửa đổi sau chốt phải được ghi và các bản ghi bị ảnh hưởng cần mã hoá lại. Kiểm tra cấu trúc và anchors không phải độ tin cậy liên mã hoá. So sánh valence cần giữ đơn vị account và bài riêng, kiểm tra thành phần outlet/năm và các URL có producing publication chưa rõ. Không suy luận thiên hướng của corpus từ tên category.
