"""Export validated article/account coding without flattening rival voices."""
import collections
import csv
import datetime
import hashlib
import json
from pathlib import Path


root = Path('data/sipc_future_coding')
import subprocess, sys
subprocess.run([sys.executable, 'scripts/validate_future_coding.py'], check=True)
validation = json.loads(Path('results/validation.json').read_text())
if validation.get('errors') or validation.get('status') != 'complete validation' or validation['records'] != validation['population']:
    raise SystemExit('Complete coding validation required before export.')
book = json.loads((root / 'codebook.json').read_text())
records = list(map(json.loads, (root / 'coded_corpus.jsonl').read_text().splitlines()))
inputs = {r['ID']: r for r in map(json.loads, (Path('data/source_corpus.jsonl')).read_text().splitlines())}
fields = list(book['fields'])
eligible = {'clear_future', 'borderline_future'}


def write_csv(path, rows, keys):
    with path.open('w', newline='', encoding='utf-8-sig') as handle:
        writer = csv.DictWriter(handle, fieldnames=keys)
        writer.writeheader()
        for row in rows:
            writer.writerow({key: json.dumps(row[key], ensure_ascii=False) if isinstance(row.get(key), (dict, list)) else row.get(key, '') for key in keys})


article_rows, account_rows = [], []
for record in records:
    article_rows.append({
        **{key: record[key] for key in ['ID', 'eligibility', 'eligibility_rationale', 'source_adequacy', 'primary_future_statement', 'relational_memo', 'evidence_reference', 'codebook_version']},
        'title': inputs[record['ID']]['title'], 'date': inputs[record['ID']]['date'],
        'account_count': len(record['accounts']),
        **{f'{field}_codes': record['codes'][field] for field in fields},
    })
    for account in record['accounts']:
        account_rows.append({
            'ID': record['ID'], 'eligibility': record['eligibility'], 'source_adequacy': record['source_adequacy'],
            **{key: account[key] for key in ['account_id', 'position', 'speaker_reference', 'future_statement', 'evaluation_target', 'stance', 'qualification', 'role_details', 'evidence_reference']},
            'codebook_version': record['codebook_version'],
            **{f'{field}_codes': account['codes'][field] for field in fields},
        })
write_csv(root / 'coded_articles.csv', article_rows, list(article_rows[0]))
write_csv(root / 'coded_accounts.csv', account_rows, list(account_rows[0]) if account_rows else ['ID', 'account_id'])



subprocess.run([sys.executable, 'scripts/summarize_future_coding.py'], check=True)
subprocess.run([sys.executable, 'scripts/review_outlet_comparison.py'], check=True)
