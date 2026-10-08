"""Validate coverage and codebook membership, not interpretive accuracy."""
import collections
import json
from pathlib import Path
import sys


def read_jsonl(path):
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def main():
    args = [arg for arg in sys.argv[1:] if arg != '--partial']
    partial = '--partial' in sys.argv
    root = Path(args[0] if args else 'data/sipc_future_coding')
    book = json.loads((root / 'codebook.json').read_text())
    import hashlib
    approved_hash = 'dc12c1321eff668b5cde06230bca7811895bcdb43b1b0d30858519762fe4affe'
    if hashlib.sha256((root / 'codebook.json').read_bytes()).hexdigest() != approved_hash:
        raise SystemExit('Codebook differs from the user-approved frozen v1.1 file.')
    fields = book['fields']
    specification = json.loads((root / 'record_specification.json').read_text())
    if set(fields) != set(specification['record']['codes']):
        raise SystemExit('Codebook does not cover the twelve SIPC fields.')
    code_ids = [entry['code'] for entries in fields.values() for entry in entries]
    if len(code_ids) != len(set(code_ids)) or 'MISSING' in code_ids:
        raise SystemExit('Substantive code IDs must be unique across fields and cannot use MISSING.')
    allowed = {field: {'MISSING', *[entry['code'] for entry in entries]} for field, entries in fields.items()}
    records = read_jsonl(root / 'coded_corpus.jsonl')
    inputs = read_jsonl(Path('data/source_corpus.jsonl'))
    expected = {row['ID'] for row in inputs}
    reviews = read_jsonl(Path('data/source_review.jsonl'))
    source_adequacy = {row['ID']: row['source_adequacy'] for row in reviews}
    if len(expected) != len(inputs) or set(source_adequacy) != expected or len(reviews) != len(inputs):
        raise SystemExit('Source corpus/review IDs must be unique and aligned.')
    counts = collections.Counter(row['ID'] for row in records)
    errors = []
    if set(counts)-expected or (not partial and set(counts) != expected):
        errors.append({'missing_IDs': sorted(expected-set(counts)), 'unexpected_IDs': sorted(set(counts)-expected)})
    if any(count != 1 for count in counts.values()):
        errors.append({'duplicate_IDs': [id for id, count in counts.items() if count != 1]})
    eligible = {'clear_future', 'borderline_future'}
    statuses = eligible | {'no_educational_future', 'unresolved_source'}

    def check_codes(id, codes, is_eligible, account_id=None):
        context = {'ID': id, **({'account_id': account_id} if account_id else {})}
        if not isinstance(codes, dict) or set(codes) != set(fields):
            errors.append({**context, 'error': 'twelve field keys differ from codebook'})
            return
        for field, values in codes.items():
            if not isinstance(values, list) or not all(isinstance(v, str) for v in values):
                errors.append({**context, 'field': field, 'error': 'codes must be string arrays'})
                continue
            if len(values) != len(set(values)) or set(values)-allowed[field]:
                errors.append({**context, 'field': field, 'error': 'duplicate or unknown codes', 'values': values})
            if 'MISSING' in values and len(values) != 1:
                errors.append({**context, 'field': field, 'error': 'missing cannot be co-coded'})
            if field == 'technology_object' and 'OBJ_AI_UNSPECIFIED' in values and len(values) != 1:
                errors.append({**context, 'field': field, 'error': 'unspecified AI is a fallback and cannot accompany a specific form'})
            if is_eligible and not values:
                errors.append({**context, 'field': field, 'error': 'eligible field requires code or MISSING'})
            if not is_eligible and values:
                errors.append({**context, 'field': field, 'error': 'noneligible article has substantive future codes'})

    for row in records:
        id = row['ID']
        if row.get('eligibility') not in statuses:
            errors.append({'ID': id, 'error': 'invalid eligibility'})
        if row.get('codebook_version') != book['version']:
            errors.append({'ID': id, 'error': 'codebook version mismatch'})
        if id in source_adequacy:
            if row.get('source_adequacy') != source_adequacy[id]:
                errors.append({'ID': id, 'error': 'source adequacy differs from reviewed source'})
            if source_adequacy[id] == 'inadequate' and row.get('eligibility') != 'unresolved_source':
                errors.append({'ID': id, 'error': 'inadequate source must remain unresolved'})
        codes = row.get('codes', {})
        check_codes(id, codes, row.get('eligibility') in eligible)
        for key in ['eligibility_rationale', 'source_adequacy', 'primary_future_statement', 'relational_memo', 'evidence_reference']:
            if not isinstance(row.get(key), str) or not row[key].strip():
                errors.append({'ID': id, 'error': f'missing textual {key}'})
        accounts = row.get('accounts')
        if not isinstance(accounts, list):
            errors.append({'ID': id, 'error': 'accounts must be an array'})
            continue
        if row.get('eligibility') not in eligible:
            if accounts:
                errors.append({'ID': id, 'error': 'noneligible article has future accounts'})
            continue
        primary = [a for a in accounts if a.get('position') == 'primary']
        if len(primary) != 1:
            errors.append({'ID': id, 'error': 'exactly one primary account required'})
        elif primary[0].get('codes') != codes or primary[0].get('future_statement') != row.get('primary_future_statement'):
            errors.append({'ID': id, 'error': 'primary account and article summary differ'})
        account_ids = [a.get('account_id') for a in accounts]
        if any(not isinstance(a, str) or not a for a in account_ids) or len(set(account_ids)) != len(account_ids):
            errors.append({'ID': id, 'error': 'account IDs must be nonempty and unique within article'})
        for account in accounts:
            aid = account.get('account_id')
            if account.get('position') not in {'primary', 'secondary'}:
                errors.append({'ID': id, 'account_id': aid, 'error': 'invalid account position'})
            check_codes(id, account.get('codes', {}), True, aid)
            for key in ['speaker_reference', 'future_statement', 'evaluation_target', 'stance', 'qualification', 'evidence_reference']:
                if not isinstance(account.get(key), str) or not account[key].strip():
                    errors.append({'ID': id, 'account_id': aid, 'error': f'missing account {key}'})
            roles = set(account.get('codes', {}).get('future_role', []))-{'MISSING'}
            details = account.get('role_details')
            if not isinstance(details, dict) or set(details) != roles:
                errors.append({'ID': id, 'account_id': aid, 'error': 'role details must cover assigned roles exactly'})
                continue
            for role, detail in details.items():
                for key in ['mechanism', 'direction', 'conditions', 'evidence_reference']:
                    if not isinstance(detail, dict) or not isinstance(detail.get(key), str) or not detail[key].strip():
                        errors.append({'ID': id, 'account_id': aid, 'role': role, 'error': f'missing role detail {key}'})
    result = {'population': len(expected), 'records': len(records), 'errors': errors,
              'status': 'partial checkpoint' if partial else 'complete validation',
              'eligibility_counts': dict(collections.Counter(row.get('eligibility') for row in records)),
              'accounts': sum(len(row.get('accounts', [])) for row in records),
              'note': 'Coverage and membership checks do not measure substantive coding agreement.'}
    report_path = Path('results/validation.json')
    report_path.write_text(json.dumps(result, ensure_ascii=False, indent=2))
    if errors:
        print(json.dumps({'errors': len(errors), 'report': str(report_path)}))
        raise SystemExit(1)
    if partial:
        print(json.dumps({'checkpoint_records': len(records), 'accounts': result['accounts'], 'errors': 0}))
        return
    print(json.dumps({'validated_records': len(records), 'eligibility_counts': result['eligibility_counts']}))


if __name__ == '__main__':
    main()
