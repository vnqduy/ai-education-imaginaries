You are assisting with qualitative coding for a media study of AI in education.

Do not rely on outside knowledge. Use only the framework definition and coding instructions provided below.

Framework for this task:
A Sociotechnical Imaginary in Public Communication, or SIPC, is a publicly communicated vision of a desirable or undesirable future involving a technology.

For this study:

- The technology is AI.
- The domain is education.
- The data are Vietnamese news articles.

A SIPC has the following elements:

1. Speaker
   Who communicates or promotes the vision?
   This may be a journalist, government official, ministry representative, school leader, teacher, student, parent, researcher, company, or another actor. If the article mainly quotes someone, identify the quoted speaker. If the journalist adds their own evaluation, mention that too.

2. Technology object
   What specific AI technology, system, tool, or AI-related object is being discussed?
   Use the article's wording. Examples might include a named chatbot, AI software, automated system, robot, camera system, AI curriculum, or general "AI." Do not force examples if they are not in the article.

3. Education context
   Where or in what educational activity is AI being imagined?
   This could be classroom learning, exams, homework, university admissions, teacher work, school management, curriculum, research, training, or another setting. Use the article's wording.

4. Future role
   What role is AI imagined to play in the future of education?
   Complete this sentence using the article's evidence:
   "AI is imagined as something that could/should/will ______."

5. Certainty
   How certain is the article that this future will happen?
   Look for language such as will, can, could, may, expected to, already happening, inevitable, experimental, proposed, warned against, or uncertain. Use the article's wording.

6. Desirability
   How is this imagined future evaluated in the article?
   Is it presented as beneficial, harmful, necessary, risky, controversial, mixed, unclear, or not evaluated? Use the article's wording and do not impose your own judgment.

7. Affected entities
   Who or what is presented as benefiting, being harmed, being changed, being protected, being governed, or being made responsible?
   Use the article's wording.

8. Rationale
   Why is the imagined future presented as desirable, undesirable, necessary, risky, or important?
   Extract the reason given in the article.

9. Timespan
   When is the future located?
   Examples: already happening, currently being piloted, in the coming school year, by a named year, in the near future, long-term future, or not specified.

10. Space
    Where is the future located?
    Examples: a school, university, province/city, Vietnam, another country, global education, or not specified.

11. Action recommendation
    What action does the article suggest, recommend, demand, warn against, or imply should happen?
    Use the article's wording. If no action is suggested, write "not specified".

12. Action responsibility
    Who is presented as responsible for taking action?
    Use the article's wording. If no responsible actor is specified, write "not specified".

Important rules:

- This is open extraction, not classification.
- Do not use pre-made labels.
- Do not name the imaginary.
- Do not infer beyond the article.
- If something is absent, write "not specified".
- If the article contains no future-oriented vision of AI in education, set "sipc_present_raw" to "no".
- If the article contains only a weak or indirect future vision, set "sipc_present_raw" to "weak".
- If the article contains a clear future-oriented vision, set "sipc_present_raw" to "yes".
- If there are multiple visions, code the dominant one and briefly describe the secondary one.
- Always include a short evidence quote that supports the coded future role.
- Return valid JSON only.

Article metadata:
ID: {{ID}}
Date: {{date}}
Outlet: {{outlet_name}}
Outlet type: {{outlet_type}}
Period: {{period}}
Title: {{title}}

Article text:
{{contents}}

Return this JSON:

{
  "ID": "{{ID}}",
  "sipc_present_raw": "",
  "speaker_raw": "",
  "technology_object_raw": "",
  "education_context_raw": "",
  "future_role_raw": "",
  "certainty_raw": "",
  "desirability_raw": "",
  "affected_entities_raw": "",
  "rationale_raw": "",
  "timespan_raw": "",
  "space_raw": "",
  "action_raw": "",
  "responsibility_raw": "",
  "evidence_quote": "",
  "secondary_vision_raw": "",
  "coder_memo": "",
  "llm_confidence": ""
}

Use "not specified" consistently for absent information.

For evidence_quote, choose a quote that directly supports future_role_raw.
