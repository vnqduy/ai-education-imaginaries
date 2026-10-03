# AI education imaginaries in Vietnamese news

Research data, methods and results for a SIPC analysis of AI education news in Vietnam.

- `data/`: article texts, open extraction, final coding and outlet classification.
- `methods/`: codebook, extraction prompt and two data collection notebooks.
- `evidence/`: qualitative findings and 22 Vietnamese quotations with English translations.
- `results/results.xlsx`: descriptive results, the 917-record analytical corpus and 7 excluded records.
- `scripts/reproduce_results.py`: reproduce the CSV tables and verify quotations.

```sh
python3 -m pip install -r requirements.txt
python3 scripts/reproduce_results.py
```

Reproduced tables are saved to the temporary `sipc-results` directory. Use `--output-dir PATH` to choose another location.

The manuscript is reserved for an OSF preprint and is excluded from this repository.
