import json,csv,collections
from pathlib import Path
p=Path('data/sipc_future_coding')
def read(f): return [json.loads(x) for x in Path(f).read_text().splitlines()]
s={r['ID']:r for r in read('data/source_corpus.jsonl')}
h={r['ID'] for r in read('data/hosted_publisher_flags.jsonl')}
g={r['outlet_domain']:r['outlet_type'] for r in csv.DictReader(open('data/outlet_classification.csv',encoding='utf-8-sig'))}
rs=[r for r in read(p/'coded_corpus.jsonl') if r['eligibility']=='clear_future' and r['ID'] not in h]
metrics={'FR_CAPABILITY_PATHWAYS':'future_role','FR_INSTITUTIONAL_REORGANISATION':'future_role','FR_COGNITION_AGENCY':'future_role','SPK_PUBLIC_AUTHORITY':'speaker','SPK_LEARNER':'speaker','ACT_COLLABORATION':'action','ACT_CURRICULUM':'action','RESP_COMMERCIAL_ACTOR':'responsibility','DES_POSITIVE':'desirability','DES_NEGATIVE':'desirability','RATION_WORK_DEMAND':'rationale'}
years=['2023','2024','2025','2026']; yc=collections.Counter(s[r['ID']]['date'].split('/')[-1] for r in rs if s[r['ID']]['date'].split('/')[-1] in years);total=sum(yc.values())
result=[]
for code,field in metrics.items():
 row={'code':code,'field':field}
 for group in ['public/central','commercial/general']:
  rr=[r for r in rs if g[s[r['ID']]['outlet_domain']]==group]
  row[group]={'n':len(rr),'primary_pct':100*sum(code in r['codes'][field] for r in rr)/len(rr),'any_account_pct':100*sum(any(code in a['codes'][field] for a in r['accounts']) for r in rr)/len(rr)}
  row[group]['year_standardized_pct']=sum(yc[y]/total*100*sum(code in r['codes'][field] for r in rr if s[r['ID']]['date'].split('/')[-1]==y)/sum(s[r['ID']]['date'].split('/')[-1]==y for r in rr) for y in years)
 row['standardized_difference_pp']=row['public/central']['year_standardized_pct']-row['commercial/general']['year_standardized_pct'];result.append(row)
out={'method':'Primary future account; 808 clear-future articles excluding hosted-publisher flags. Any-account sensitivity counts each article once per code. Year standardization uses pooled article weights for common 2023–2026 years; descriptive adjustment only.','metrics':result}
comparison_path=Path('results/outlet_comparison.json')
comparison=json.loads(comparison_path.read_text())
comparison['account_and_year_sensitivity']=out
comparison_path.write_text(json.dumps(comparison,ensure_ascii=False,indent=2))
for r in result: print(r['code'],*[round(r[x]['primary_pct'],1) for x in ['public/central','commercial/general']], 'year-diff',round(r['standardized_difference_pp'],1),'any-diff',round(r['public/central']['any_account_pct']-r['commercial/general']['any_account_pct'],1))
