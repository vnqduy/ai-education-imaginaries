"""Descriptive SIPC comparisons; frequencies support relational interpretation."""
import collections
import csv
import json
from pathlib import Path


def load(path):
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def main():
    root = Path('data/sipc_future_coding')
    validation = json.loads((Path('results/validation.json')).read_text())
    if validation['errors']:
        raise SystemExit('Resolve coding validation errors first.')
    coded = load(root / 'coded_corpus.jsonl')
    sources = {r['ID']: r for r in load(Path('data/source_corpus.jsonl'))}
    hosted = {r['ID'] for r in load(Path('data/hosted_publisher_flags.jsonl'))}
    with Path('data/outlet_classification.csv').open(encoding='utf-8-sig') as f:
        groups = {r['outlet_domain']: r['outlet_type'] for r in csv.DictReader(f)}
    book = json.loads((root / 'codebook.json').read_text())
    labels = {entry['code']: entry['label'] for entries in book['fields'].values() for entry in entries}
    scenarios = {
        'clear_unflagged_publisher': lambda r: r['eligibility']=='clear_future' and r['ID'] not in hosted,
        'clear_and_borderline_unflagged_publisher': lambda r: r['eligibility'] in {'clear_future','borderline_future'} and r['ID'] not in hosted,
        'clear_all_supplied_host_groups': lambda r: r['eligibility']=='clear_future',
        'clear_complete_sources_unflagged_publisher': lambda r: r['eligibility']=='clear_future' and r['ID'] not in hosted and r['source_adequacy'] in {'adequate','recovered'},
    }
    counts, outlet_counts, contrasts, concentration = [], [], [], []
    denominator_rows, year_composition = [], []
    for scenario, keep in scenarios.items():
        records = [r for r in coded if keep(r)]
        bygroup = collections.defaultdict(list)
        byoutlet = collections.defaultdict(list)
        for r in records:
            domain = sources[r['ID']]['outlet_domain']
            bygroup[groups[domain]].append(r)
            byoutlet[domain].append(r)
        for group, rows in bygroup.items():
            denominator_rows.append({'scenario':scenario,'group':group,'articles':len(rows)})
            years = collections.Counter(sources[r['ID']]['date'].split('/')[-1] for r in rows)
            for year, n in sorted(years.items()):
                year_composition.append({'scenario':scenario,'group':group,'year':year,'articles':n,'group_articles':len(rows),'share':n/len(rows)})
            domain_counts = collections.Counter(sources[r['ID']]['outlet_domain'] for r in rows)
            leading, leading_n = domain_counts.most_common(1)[0]
            concentration.append({'scenario':scenario,'group':group,'leading_outlet':leading,'leading_articles':leading_n,'group_articles':len(rows),'leading_share':leading_n/len(rows)})
            for field in book['fields']:
                c = collections.Counter(code for r in rows for code in r['codes'][field])
                for code in ['MISSING', *[e['code'] for e in book['fields'][field]]]:
                    counts.append({'scenario':scenario,'group':group,'field':field,'code':code,'label':labels.get(code,'not specified'),'articles':c[code],'denominator':len(rows),'proportion':c[code]/len(rows)})
        for outlet, rows in byoutlet.items():
            for field in book['fields']:
                c = collections.Counter(code for r in rows for code in r['codes'][field])
                for code, n in c.items():
                    outlet_counts.append({'scenario':scenario,'outlet':outlet,'group':groups[outlet],'field':field,'code':code,'articles':n,'denominator':len(rows),'proportion':n/len(rows)})
        if {'public/central','commercial/general'}.issubset(bygroup):
            for field in book['fields']:
                for entry in book['fields'][field]:
                    code=entry['code']
                    def difference(excluded=None):
                        result={}
                        for group, rows in bygroup.items():
                            subset=[r for r in rows if sources[r['ID']]['outlet_domain']!=excluded]
                            if not subset:return None
                            result[group]=sum(code in r['codes'][field] for r in subset)/len(subset)
                        return result['public/central']-result['commercial/general']
                    baseline=difference()
                    omitted=[(outlet,difference(outlet)) for outlet in byoutlet]
                    values=[d for outlet,d in omitted if d is not None]
                    contrasts.append({'scenario':scenario,'field':field,'code':code,'label':entry['label'],'public_minus_commercial_percentage_points':100*baseline,'leave_one_outlet_out_min_pp':100*min(values) if values else None,'leave_one_outlet_out_max_pp':100*max(values) if values else None})
    comparison = {'group_counts': counts, 'outlet_counts': outlet_counts, 'contrasts': contrasts,
                  'denominators': denominator_rows, 'concentration': concentration, 'year_composition': year_composition}
    Path('results/outlet_comparison.json').write_text(json.dumps(comparison, ensure_ascii=False, indent=2))
    summary={'population':len(coded),'eligibility_counts':dict(collections.Counter(r['eligibility'] for r in coded)),'source_adequacy_counts':dict(collections.Counter(r['source_adequacy'] for r in coded)),'hosted_publisher_flags':len(hosted),'denominators':denominator_rows,'note':'Code frequencies are article-level constituent presence, not imaginary assignments. Multi-coding proportions need not sum to one. Supplied grouping labels are exploratory; host-route flags are omitted in primary comparisons. No causal control/ownership inference or significance test is made.'}
    # Counts preserve the original primary account and attributed secondary voices.
    summary['account_count'] = sum(len(r['accounts']) for r in coded)
    summary['multi_account_articles'] = sum(len(r['accounts']) > 1 for r in coded)
    summary['distributions'] = []
    for scenario in ['clear_only', 'clear_and_borderline']:
        selected = [r for r in coded if r['eligibility'] == 'clear_future' or
                    (scenario == 'clear_and_borderline' and r['eligibility'] == 'borderline_future')]
        for unit in ['primary_article_account', 'all_attributed_accounts']:
            rows = selected if unit == 'primary_article_account' else [a for r in selected for a in r['accounts']]
            for field in book['fields']:
                counter = collections.Counter(c for r in rows for c in r['codes'][field])
                for code, n in sorted(counter.items()):
                    summary['distributions'].append({'scenario': scenario, 'unit': unit, 'field': field,
                          'code': code, 'count': n, 'denominator': len(rows), 'proportion': n/len(rows)})
    Path('results/corpus_summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2))
    print(json.dumps({'records':len(coded),'outputs':['results/outlet_comparison.json','results/corpus_summary.json']}))


if __name__=='__main__':
    main()
