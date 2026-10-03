# AI education imaginaries in Vietnamese news

Research data, methods and results for a SIPC analysis of AI education news in Vietnam.

- `data/final_analysis_dataset.csv`: analysis-ready data for the 917 retained articles, with metadata and all final coding fields; no article texts or intermediate extraction fields.
- Other files in `data/`: source texts, extraction, coding workbook and outlet classification.
- `methods/`: codebook, extraction prompt and two data collection notebooks.
- `evidence/`: qualitative findings and 22 Vietnamese quotations with English translations.
- `results/post_period_robustness.csv`: post-period gaps and leave-one-outlet-out sensitivity.
- `results/results.xlsx`: descriptive results, the 917-record analytical corpus and 7 excluded records.
- `scripts/reproduce_results.py`: reproduce the CSV tables and verify quotations.

```sh
python3 -m pip install -r requirements.txt
python3 scripts/reproduce_results.py
```

Reproduced tables are saved to the temporary `sipc-results` directory. Use `--output-dir PATH` to choose another location.

The manuscript is reserved for an OSF preprint and is excluded from this repository.

For R, use `read.csv("data/final_analysis_dataset.csv", fileEncoding = "UTF-8", na.strings = "")`. Dates use YYYY-MM-DD. Theme codes are 0/1; blank values are NA, with `__status` distinguishing coded, missing and unresolved fields. `sipc_presence` retains yes/weak eligibility for sensitivity analysis. `chatgpt_period` uses 30 November 2022. Outlet labels retain the project mapping; substantive group names await the classification review. Code definitions are in `methods/coding_codebook.xlsx`.
