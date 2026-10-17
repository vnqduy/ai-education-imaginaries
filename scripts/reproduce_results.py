"""Export one article-level rectangular CSV for analysis in R."""
import collections
import csv
import datetime
import io
import json
from validate_future_coding import ROOT, WORK, rows, validate


def main():
    coded = rows(WORK / 'coded_corpus.jsonl')
    report = validate(coded, complete=True)
    if not report['valid']:
        raise SystemExit(json.dumps(report, ensure_ascii=False))
    sources = {r['ID']: r for r in rows(ROOT / 'data/source_corpus.jsonl')}
    hosted = {r['ID'] for r in rows(ROOT / 'data/hosted_publisher_flags.jsonl')}
    with (ROOT / 'data/outlet_classification.csv').open(encoding='utf-8-sig', newline='') as handle:
        outlets = {r['outlet_domain']: r for r in csv.DictReader(handle)}
    manifest = json.loads((WORK / 'manifest.json').read_text())
    book = json.loads((ROOT / manifest['codebook_path']).read_text())
    definitions = {field: [entry['code'] for entry in entries] for field, entries in book['fields'].items()}
    metadata = ['article_id', 'title', 'date', 'year', 'url',
                'outlet_domain', 'outlet_name', 'outlet_group', 'publisher_uncertain',
                'eligibility', 'source_adequacy', 'account_count', 'main_sample', 'codebook_version']
    columns = metadata + [column for field, codes in definitions.items()
                          for column in [*[field + '__' + code for code in codes], field + '__missing']]
    if len(set(columns)) != len(columns):
        raise SystemExit('Duplicate dataframe column names')
    matrix = []
    for record in coded:
        source = sources[record['ID']]
        outlet = outlets[source['outlet_domain']]
        date = datetime.datetime.strptime(source['date'], '%d/%m/%Y').date()
        eligible = record['eligibility'] in {'clear_future', 'borderline_future'}
        row = {
            'article_id': record['ID'],
            'title': source['title'], 'date': date.isoformat(), 'year': date.year, 'url': source['real_url'],
            'outlet_domain': source['outlet_domain'], 'outlet_name': outlet['outlet_name'],
            'outlet_group': outlet['outlet_type'], 'publisher_uncertain': int(record['ID'] in hosted),
            'eligibility': record['eligibility'], 'source_adequacy': record['source_adequacy'],
            'account_count': len(record['accounts']),
            'main_sample': int(record['eligibility'] == 'clear_future' and record['ID'] not in hosted),
            'codebook_version': record['codebook_version'],
        }
        for field, codes in definitions.items():
            present = {code for account in record['accounts'] for code in account['codes'][field]} - {'MISSING'}
            observed = eligible and bool(present)
            row[field + '__missing'] = int(not observed) if eligible else None
            for code in codes:
                row[field + '__' + code] = int(code in present) if observed else None
        matrix.append(row)
    target = ROOT / 'results/article_coding.csv'
    target.parent.mkdir(exist_ok=True)
    handle = io.StringIO(newline='')
    writer = csv.DictWriter(handle, fieldnames=columns, lineterminator='\n')
    writer.writeheader()
    writer.writerows(matrix)
    # Round-trip verification of scalar types, missingness and rectangular coverage.
    handle.seek(0)
    reader = csv.DictReader(handle)
    if reader.fieldnames != columns:
        raise SystemExit('CSV header mismatch')
    restored = list(reader)
    if len(restored) != len(coded) or len({r['article_id'] for r in restored}) != len(coded):
        raise SystemExit('CSV row coverage/uniqueness failed')
    for expected, actual in zip(matrix, restored):
        if set(actual) != set(columns) or any(actual[c] != ('' if expected[c] is None else str(expected[c])) for c in columns):
            raise SystemExit('CSV values changed during serialization: ' + expected['article_id'])
    target.write_text(handle.getvalue(), encoding='utf-8')
    print(json.dumps({'output': str(target), 'rows': len(matrix), 'columns': len(columns),
                      'metadata_columns': len(metadata), 'substantive_code_columns': sum(map(len, definitions.values())),
                      'field_missing_columns': len(definitions),
                      'main_sample_articles': sum(r['main_sample'] for r in matrix),
                      'eligibility_counts': dict(collections.Counter(r['eligibility'] for r in matrix)),
                      'validation': 'Complete source coding and CSV round-trip checks passed.'}))


if __name__ == '__main__':
    main()
