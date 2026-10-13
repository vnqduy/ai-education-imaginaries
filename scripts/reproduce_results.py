"""Validate and reproduce final private coding exports and public aggregates."""
import csv,json,subprocess,sys
from pathlib import Path
from validate_future_coding import ROOT,WORK,rows,validate

def main():
    coded=rows(WORK/'coded_corpus.jsonl');report=validate(coded,complete=True)
    (ROOT/'results/validation.json').write_text(json.dumps(report,indent=2)+'\n')
    if not report['valid']:raise SystemExit('Complete validation failed')
    source={r['ID']:r for r in rows(ROOT/'data/source_corpus.jsonl')}
    book=json.load((WORK/'codebook.json').open());fields=list(book['fields'])
    articles=[];accounts=[]
    for r in coded:
        union={f:sorted({c for a in r['accounts'] for c in a['codes'][f]}-{'MISSING'}) for f in fields}
        for f in fields:
            if r['accounts'] and not union[f]:union[f]=['MISSING']
        articles.append({'ID':r['ID'],'legacy_extraction_id':r['legacy_extraction_id'],'title':source[r['ID']]['title'],'date':source[r['ID']]['date'],'outlet_domain':source[r['ID']]['outlet_domain'],'eligibility':r['eligibility'],'source_adequacy':r['source_adequacy'],'account_count':len(r['accounts']),**{f+'_codes':union[f] for f in fields},'primary_account_codes':r['codes']})
        for a in r['accounts']:
            accounts.append({'ID':r['ID'],'account_id':a['account_id'],'position':a['position'],'speaker_reference':a['speaker_reference'],'future_statement':a['future_statement'],**{f+'_codes':a['codes'][f] for f in fields}})
    for name,data in [('coded_articles.csv',articles),('coded_accounts.csv',accounts)]:
        with (WORK/name).open('w',newline='',encoding='utf-8-sig') as f:
            w=csv.DictWriter(f,fieldnames=list(data[0]));w.writeheader()
            w.writerows({k:json.dumps(v,ensure_ascii=False) if isinstance(v,(list,dict)) else v for k,v in row.items()} for row in data)
    subprocess.run([sys.executable,'-B',str(ROOT/'scripts/summarize_future_coding.py')],check=True,cwd=ROOT)
    print(json.dumps({'articles':len(coded),'accounts':len(accounts),'validation':'passed','private_exports':'data/sipc_future_coding/','public_aggregates':'results/'}))

if __name__=='__main__':main()
