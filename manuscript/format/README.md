# LMT manuscript exports

Checked against the [official Learning, Media and Technology instructions](https://www.tandfonline.com/action/authorSubmission?show=instructions&journalCode=cjem20) on 20 October 2026 through the publisher’s author-instructions page.

## Render

Run from the repository root (Quarto executes R relative to the input file):

```sh
quarto render manuscript/manuscript.qmd --to docx
quarto render manuscript/manuscript.qmd --to pdf
quarto render manuscript/manuscript.qmd --to all
quarto render supplementary/supplementary.qmd --to all
```

Outputs are written next to each QMD. Both formats use the same data, source text, table calculations, bibliography and citation style. Tables in Word are native editable tables, not images. PDF tables use repeated headers. Do not run two exports of the same QMD simultaneously because Quarto uses shared intermediate files.

Requirements: Quarto, R with tidyverse, kableExtra and jsonlite, XeLaTeX for PDF, and Times New Roman. The Word reference document is included; no Python package or Word installation is needed for normal export.

## Formatting choices and journal requirements

- LMT accepts format-free initial submissions, including DOCX and PDF, with tables inline or in separate files. This working manuscript keeps tables inline.
- Research articles: no more than 8,000 words, explicitly including the abstract, tables, captions, footnotes and endnotes. The official list does not explicitly mention references; check counts both with and without references before submission.
- Unstructured abstract: 200 words. Keywords: 5–7 (six included).
- Consistent scholarly references are acceptable initially. Both exports use the journal's Taylor & Francis Chicago author–date style via the included CSL rather than APA.
- A4, 1-inch margins, Times New Roman 12 pt and 1.5-line body spacing are readable working-manuscript choices, not claimed journal mandates. Tables use compact type.
- Title page, separate abstract/keywords page, main text and references. Full profiles, sensitivity checks and methodological documentation remain in the separate supplementary document.
- For a review copy without the title-page author details, add `-M anonymous:true --output manuscript-anonymous.docx` (or `.pdf`). Inspect self-identifying text and file metadata before actual submission. The default remains the author copy.

## Files

- `tables.R`: format-aware table renderer, preserving data and row groups in Word/PDF.
- `lmt.lua`: shared front matter and Word table text styles.
- `lmt-reference.docx`: Word paragraph, heading, table, page and footer styles.
- `taylor-and-francis-chicago-author-date.csl`: CSL project style, downloaded from https://github.com/citation-style-language/styles/blob/master/taylor-and-francis-chicago-author-date.csl (license retained in file).

## Submission information still requiring the author

These are not invented or filled with unverified “none” declarations:

- Funding sources or confirmation of no funding.
- Financial and non-financial competing interests.
- AI use: full tool/model versions, reason and method of use in research and manuscript preparation. Existing Methods describes AI-assisted coding but is not yet a complete disclosure.
- Data availability statement and repository/DOI or chosen access arrangement.
- Acknowledgments, if applicable; CRediT roles and ORCID, if available.
- Exact collection dates and other outstanding methodological details in the manuscript.

LMT uses double-anonymous review. Prepare the anonymised manuscript and author information according to the submission portal when submitting. No submission has been made.


## AI reporting and author completion

Methods and the supplementary document report the AI workflow; H1–H4 mark the short factual contributions still to be supplied by the author. Do not convert these prompts into claims of completed human review. In particular, the initial 100-article batch was AI extraction, not evidence of 100 articles manually coded by the author.

Checked on 20 October 2026: [Taylor & Francis guidance](https://authorservices.taylorandfrancis.com/editorial-policies/using-ai-in-your-research-and-manuscript-preparations/) permits methodological AI assistance with disclosure and retained records, but expressly disallows AI-generated first drafts of manuscripts or sections. This project includes substantive AI drafting/revision, not only copyediting. Preserve that distinction in disclosure and resolve the submission implications with the journal before submission; do not state compliance merely because the outputs have been checked. No submission has been made.
