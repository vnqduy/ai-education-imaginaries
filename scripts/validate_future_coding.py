"""Check v2 coverage, schema and exact evidence; not interpretive accuracy."""
import argparse
import collections
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / 'data/sipc_future_coding'


def rows(path):
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def validate(records, complete=False):
    manifest = json.loads((WORK / 'manifest.json').read_text())
    book_path = ROOT / manifest.get('codebook_path', 'data/sipc_future_coding/codebook.json')
    book = json.loads(book_path.read_text())
    source_rows = rows(ROOT / 'data/source_corpus.jsonl')
    sources = {r['ID']: r for r in source_rows}
    reviews = {r['ID']: r for r in rows(ROOT / 'data/source_review.jsonl')}
    fields = set(book['fields'])
    allowed = {f: {e['code'] for e in entries} | {'MISSING'} for f, entries in book['fields'].items()}
    errors = []
    def fail(ID, message, account=None, field=None):
        errors.append({'ID': ID, 'error': message, **({'account_id': account} if account else {}), **({'field': field} if field else {})})
    actor_fields = ('speaker', 'responsibility', 'affected_entities')
    actor_definitions = [[(e['code'], e['label'], e['definition'])
                          for e in book['fields'][field]] for field in actor_fields]
    if any(definitions != actor_definitions[0] for definitions in actor_definitions[1:]):
        fail(None, 'Actor fields must share identical ordered categories and definitions')
    if hashlib.sha256(book_path.read_bytes()).hexdigest() != manifest['codebook_sha256']:
        fail(None, 'Frozen codebook hash differs from manifest')
    if hashlib.sha256((ROOT / 'data/source_corpus.jsonl').read_bytes()).hexdigest() != manifest['source_sha256']:
        fail(None, 'Source hash differs from manifest')
    counts = collections.Counter(r.get('ID') for r in records)
    for ID, n in counts.items():
        if ID not in sources or n != 1:
            fail(ID, f'Unexpected ID or duplicate count {n}')
    if len(sources) != manifest['total_articles']:
        fail(None, 'Source population differs from frozen manifest')
    if len(source_rows) != len(sources):
        fail(None, 'Duplicate source IDs')
    missing = sorted(set(sources) - set(counts))
    if complete and missing:
        fail(None, f'Incomplete corpus: {len(missing)} missing IDs')
    eligible = {'clear_future', 'borderline_future'}
    def check_codes(ID, codes, active, aid=None):
        if not isinstance(codes, dict) or set(codes) != fields:
            fail(ID, 'Exactly twelve field keys required', aid)
            return
        for f, vals in codes.items():
            if not isinstance(vals, list) or not all(isinstance(v, str) for v in vals):
                fail(ID, 'String-array codes required', aid, f)
                continue
            if len(vals) != len(set(vals)) or set(vals) - allowed[f]:
                fail(ID, 'Duplicate or unknown code', aid, f)
            if active != bool(vals):
                fail(ID, 'Eligible fields require codes/MISSING; noneligible fields empty', aid, f)
            if 'MISSING' in vals and len(vals) != 1:
                fail(ID, 'MISSING must be exclusive', aid, f)
            if f == 'technology_object' and 'OBJ_UNSPECIFIED' in vals and len(vals) != 1:
                fail(ID, 'Unspecified object must be exclusive', aid, f)
            if f == 'desirability' and active and len(vals) != 1:
                fail(ID, 'One desirability value per evaluation target', aid, f)
    accounts_total = evidence_total = 0
    for r in records:
        ID = r.get('ID'); active = r.get('eligibility') in eligible
        if r.get('eligibility') not in eligible | {'no_educational_future', 'unresolved_source'}:
            fail(ID, 'Invalid eligibility')
        if r.get('codebook_version') != book['version']:
            fail(ID, 'Wrong codebook version')
        if ID in reviews and r.get('source_adequacy') != reviews[ID]['source_adequacy']:
            fail(ID, 'Source adequacy differs from reviewed source')
        if ID in reviews and reviews[ID]['source_adequacy'] == 'inadequate' and r.get('eligibility') != 'unresolved_source':
            fail(ID, 'Inadequate source must remain unresolved')
        for key in ['eligibility_rationale', 'primary_future_statement', 'relational_memo', 'evidence_reference', 'primary_selection_reason']:
            if not isinstance(r.get(key), str) or not r[key].strip():
                fail(ID, f'Missing textual {key}')
        check_codes(ID, r.get('codes'), active)
        accounts = r.get('accounts')
        if not isinstance(accounts, list):
            fail(ID, 'Accounts must be array'); continue
        accounts_total += len(accounts)
        if not active:
            if accounts: fail(ID, 'Noneligible record has accounts')
            continue
        primary = [a for a in accounts if a.get('position') == 'primary']
        if len(primary) != 1:
            fail(ID, 'Exactly one primary account required')
        elif primary[0].get('codes') != r.get('codes') or primary[0].get('future_statement') != r.get('primary_future_statement'):
            fail(ID, 'Article must match its primary account')
        aids = [a.get('account_id') for a in accounts]
        if any(not isinstance(a, str) or not a for a in aids) or len(set(aids)) != len(aids):
            fail(ID, 'Account IDs must be unique nonempty strings')
        for a in accounts:
            aid = a.get('account_id'); codes = a.get('codes', {})
            check_codes(ID, codes, True, aid)
            if a.get('position') not in {'primary', 'secondary'}: fail(ID, 'Invalid position', aid)
            for key in ['speaker_reference', 'future_statement', 'evaluation_target', 'stance', 'qualification', 'evidence_reference']:
                if not isinstance(a.get(key), str) or not a[key].strip(): fail(ID, f'Missing textual {key}', aid)
            propositions = a.get('propositions', [])
            if not isinstance(propositions, list) or not propositions:
                fail(ID, 'Propositions required', aid); propositions = []
            pids = [p.get('proposition_id') for p in propositions]
            if len(set(pids)) != len(pids) or any(not isinstance(p, str) or not p for p in pids):
                fail(ID, 'Invalid proposition IDs', aid)
            for p in propositions:
                for key in ['statement', 'target', 'claim_mode']:
                    if not isinstance(p.get(key), str) or not p[key].strip(): fail(ID, f'Missing proposition {key}', aid)
            ev = a.get('field_evidence', {})
            notes = a.get('missing_notes', {})
            if not isinstance(ev, dict) or set(ev) != fields:
                fail(ID, 'Twelve field evidence keys required', aid); ev = {}
            if not isinstance(notes, dict): fail(ID, 'Missing notes must be object', aid); notes = {}
            for f, vals in codes.items():
                if f not in fields or not isinstance(vals, list): continue
                entries = ev.get(f, [])
                if not isinstance(entries, list): fail(ID, 'Evidence entries must be array', aid, f); continue
                if vals == ['MISSING']:
                    if entries or not isinstance(notes.get(f), str) or not notes[f].strip():
                        fail(ID, 'MISSING requires empty evidence and absence note', aid, f)
                elif set(e.get('code') for e in entries) != set(vals):
                    fail(ID, 'Evidence must cover exactly assigned codes', aid, f)
                for e in entries:
                    evidence_total += 1
                    q = e.get('quote')
                    source_text = sources.get(ID, {}).get('full_text', '')
                    if q is not None:
                        if not isinstance(q, str) or not q.strip() or q not in source_text:
                            fail(ID, 'Evidence quote not exact contiguous source span', aid, f)
                    else:
                        start, end = e.get('char_start'), e.get('char_end')
                        if type(start) is not int or type(end) is not int or not (0 <= start < end <= len(source_text)) or not source_text[start:end].strip():
                            fail(ID, 'Invalid retained-source character locator', aid, f)
                    if e.get('proposition_id') not in pids or not isinstance(e.get('reason'), str) or not e['reason'].strip():
                        fail(ID, 'Evidence requires valid proposition and reason', aid, f)
            roles = set(codes.get('future_role', [])) - {'MISSING'}
            details = a.get('role_details')
            if not isinstance(details, dict) or set(details) != roles:
                fail(ID, 'Role details must match assigned roles', aid)
            else:
                for detail in details.values():
                    for key in ['mechanism', 'direction', 'conditions', 'evidence_reference']:
                        if not isinstance(detail.get(key), str) or not detail[key].strip(): fail(ID, f'Missing role detail {key}', aid)
            literal = a.get('literal_details')
            if not isinstance(literal, dict):
                fail(ID, 'Literal details must be object', aid)
            elif 'SPACE_FOREIGN_DOMESTIC' in codes.get('space', []):
                space = literal.get('space', {})
                if not isinstance(space, dict) or not isinstance(space.get('country'), str) or not space['country'].strip():
                    fail(ID, 'Foreign domestic scope requires literal space.country', aid, 'space')
    return {'valid': not errors, 'scope': 'complete' if complete else 'partial', 'records': len(records), 'accounts': accounts_total, 'evidence_entries': evidence_total, 'missing_count': len(missing), 'eligibility': dict(collections.Counter(r.get('eligibility') for r in records)), 'errors': errors, 'limitation': 'Schema, coverage and exact spans only; no claim of semantic validity or intercoder reliability.'}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('paths', nargs='*', type=Path)
    parser.add_argument('--complete', action='store_true')
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    paths = args.paths or [WORK / 'coded_corpus.jsonl']
    report = validate([r for p in paths for r in rows(p)], args.complete)
    out = json.dumps(report, ensure_ascii=False, indent=2)
    if args.output: args.output.write_text(out + '\n')
    print(out)
    raise SystemExit(0 if report['valid'] else 1)


if __name__ == '__main__':
    main()
