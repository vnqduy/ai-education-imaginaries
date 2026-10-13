"""Reproduce the two final aggregate results from validated private coding."""
import collections
import csv
import json
import re
from pathlib import Path
from validate_future_coding import ROOT, WORK, rows, validate


def article_has_code(record, field, code):
    """Article presence without conflating the relationships of separate accounts."""
    values = {c for a in record['accounts'] for c in a['codes'][field]}
    if code == 'MISSING':
        return bool(record['accounts']) and not (values - {'MISSING'})
    return code in values


def main():
    coded = rows(WORK / 'coded_corpus.jsonl')
    report = validate(coded, complete=True)
    if not report['valid']:
        raise SystemExit('Complete v2 validation required before aggregating results.')
    sources = {r['ID']:r for r in rows(ROOT / 'data/source_corpus.jsonl')}
    hosted = {r['ID'] for r in rows(ROOT / 'data/hosted_publisher_flags.jsonl')}
    with (ROOT / 'data/outlet_classification.csv').open(encoding='utf-8-sig') as f:
        groups = {r['outlet_domain']:r['outlet_type'] for r in csv.DictReader(f)}
    manifest = json.loads((WORK / 'manifest.json').read_text())
    book = json.loads((ROOT / manifest.get('codebook_path', 'data/sipc_future_coding/codebook.json')).read_text())
    definitions = {f: {'MISSING':'No assigned substantive code', **{e['code']:e['label'] for e in entries}} for f,entries in book['fields'].items()}
    for s in sources.values():
        if s['outlet_domain'] not in groups:
            raise SystemExit('Unclassified outlet: '+s['outlet_domain'])
    scenarios = {
        'clear_unflagged_publisher':lambda r:r['eligibility']=='clear_future' and r['ID'] not in hosted,
        'clear_and_borderline_unflagged_publisher':lambda r:r['eligibility'] in {'clear_future','borderline_future'} and r['ID'] not in hosted,
        'clear_all_supplied_host_groups':lambda r:r['eligibility']=='clear_future',
        'clear_complete_sources_unflagged_publisher':lambda r:r['eligibility']=='clear_future' and r['ID'] not in hosted and r['source_adequacy'] in {'adequate','recovered'},
    }
    def year(r):
        match = re.search(r'\b(?:19|20)\d{2}\b', sources[r['ID']]['date'])
        return match.group() if match else 'unknown'
    counts, contrasts, denominators, concentrations, years, byoutlet = [],[],[],[],[],[]
    for name, keep in scenarios.items():
        selected = [r for r in coded if keep(r)]
        split = {g:[r for r in selected if groups[sources[r['ID']]['outlet_domain']]==g] for g in sorted(set(groups.values()))}
        for group, subset in split.items():
            n = len(subset)
            denominators.append({'scenario':name,'group':group,'articles':n})
            outlets = collections.Counter(sources[r['ID']]['outlet_domain'] for r in subset)
            concentrations.append({'scenario':name,'group':group,'outlets':dict(outlets),'leading_share':max(outlets.values())/n if n else None})
            for y,num in sorted(collections.Counter(year(r) for r in subset).items()):
                years.append({'scenario':name,'group':group,'year':y,'articles':num,'denominator':n})
            for unit in ['any_account_article','primary_article_account']:
                for field, labels in definitions.items():
                    for code,label in labels.items():
                        hits = sum(code in r['codes'][field] if unit=='primary_article_account' else article_has_code(r, field, code) for r in subset)
                        counts.append({'scenario':name,'group':group,'unit':unit,'field':field,'code':code,'label':label,'articles':hits,'denominator':n,'proportion':hits/n if n else None})
            for outlet in outlets:
                rr = [r for r in subset if sources[r['ID']]['outlet_domain']==outlet]
                for f, labels in definitions.items():
                    for c,label in labels.items():
                        num = sum(article_has_code(r, f, c) for r in rr)
                        byoutlet.append({'scenario':name,'outlet':outlet,'group':group,'unit':'any_account_article','field':f,'code':c,'articles':num,'denominator':len(rr),'proportion':num/len(rr)})
        if all(split.get(g) for g in ['public/central','commercial/general']):
            for unit in ['any_account_article','primary_article_account']:
                for f,labels in definitions.items():
                    for c,label in labels.items():
                        def pct(rr):
                            if not rr:return None
                            return 100*sum(c in r['codes'][f] if unit=='primary_article_account' else article_has_code(r, f, c) for r in rr)/len(rr)
                        def diff(excluded=None):
                            vals = [pct([r for r in split[g] if sources[r['ID']]['outlet_domain']!=excluded]) for g in ['public/central','commercial/general']]
                            return vals[0]-vals[1] if all(v is not None for v in vals) else None
                        omitted = [diff(o) for o in {sources[r['ID']]['outlet_domain'] for r in selected}]
                        omitted = [v for v in omitted if v is not None]
                        common = set(year(r) for r in split['public/central']) & set(year(r) for r in split['commercial/general']) - {'unknown'}
                        yc = collections.Counter(year(r) for r in selected if year(r) in common)
                        total = sum(yc.values())
                        std = sum(yc[y]/total*(pct([r for r in split['public/central'] if year(r)==y])-pct([r for r in split['commercial/general'] if year(r)==y])) for y in common) if total else None
                        contrasts.append({'scenario':name,'unit':unit,'field':f,'code':c,'label':label,'public_minus_commercial_pp':diff(),'leave_one_outlet_out_min_pp':min(omitted) if omitted else None,'leave_one_outlet_out_max_pp':max(omitted) if omitted else None,'year_standardized_difference_pp':std,'common_years':sorted(common)})
    summary = {'codebook_version':book['version'],'population':len(coded),'eligibility_counts':dict(collections.Counter(r['eligibility'] for r in coded)),'source_adequacy_counts':dict(collections.Counter(r['source_adequacy'] for r in coded)),'accounts':sum(len(r['accounts']) for r in coded),'multi_account_articles':sum(len(r['accounts'])>1 for r in coded),'hosted_publisher_flags':len(hosted),'distributions':[]}
    for name, statuses in [('clear_only',{'clear_future'}),('clear_and_borderline',{'clear_future','borderline_future'})]:
        selected = [r for r in coded if r['eligibility'] in statuses]
        for unit, rr in [('any_account_article',selected),('primary_article_account',selected),('all_attributed_accounts',[a for r in selected for a in r['accounts']])]:
            for field, labels in definitions.items():
                for code,label in labels.items():
                    count = sum(article_has_code(r, field, code) if unit == 'any_account_article' else code in r['codes'][field] for r in rr)
                    summary['distributions'].append({'scenario':name,'unit':unit,'field':field,'code':code,'label':label,'count':count,'denominator':len(rr),'proportion':count/len(rr) if rr else None})
    summary['main_unit'] = 'any_account_article'
    summary['sensitivity_unit'] = 'primary_article_account'
    note = 'Main unit is the article: presence in any account, once per code per article. Article MISSING means no account assigns a substantive code for that field; partial missingness within individual accounts remains in the coding records. Primary-account counts are a prominence sensitivity; pooled account counts are supplementary. Never combine different accounts into synthetic relational futures. Constituent frequencies are not imaginary assignments. Any-account counts each article once per code. Unequal outlet/year composition and exploratory group labels limit inference; descriptive adjustment is not causal control or statistical significance. Structural validation is not semantic reliability.'
    summary['note'] = note
    comparison = {'main_unit':'any_account_article','sensitivity_unit':'primary_article_account','codebook_version':book['version'],'group_counts':counts,'contrasts':contrasts,'denominators':denominators,'concentration':concentrations,'year_composition':years,'outlet_counts':byoutlet,'note':note}
    output = ROOT / 'results'
    output.mkdir(exist_ok=True)
    for name,data in [('corpus_summary',summary),('outlet_comparison',comparison)]:
        (output / (name+'.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'records':len(coded),'accounts':summary['accounts'],'aggregate_directory':str(output),'validation':'complete coverage/schema/source locators passed'}))


if __name__=='__main__':
    main()
