#!/usr/bin/env python3
"""Reproduce descriptive SIPC results from frozen coding, without network or LLM calls."""
from pathlib import Path
from collections import Counter
from datetime import datetime
from itertools import combinations
import argparse,csv,hashlib,json,platform,tempfile
import openpyxl
ROOT=Path(__file__).resolve().parents[1]
KEYS=[('public/central','pre'),('public/central','post'),('commercial/general','pre'),('commercial/general','post')]
CUTOFF=datetime(2022,11,30)
def read_csv(path):
 with path.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def unique(rows,key):
 out={}
 for row in rows:
  value=row[key]
  if not value or value in out:raise ValueError(f'Blank or duplicate {key}: {value}')
  out[value]=row
 return out
def write(path,fields,rows):
 with path.open('w',encoding='utf-8',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
def status(col):return col.split('__')[0]+'__status'
def compute(rows,cols,cutoff=CUTOFF):
 groups=[[r for r in rows if r['group']==g and ('pre' if r['date']<cutoff else 'post')==p] for g,p in KEYS]
 result=[]
 for col in cols:
  for (g,p),group in zip(KEYS,groups):
   valid=[r for r in group if r[status(col)]=='coded'];n=sum(r[col]==1 for r in valid);N=len(valid)
   result.append(dict(outcome=col,outlet_type=g,period=p,n=n,valid_N=N,eligible_N=len(group),missing=sum(r[status(col)]=='missing' for r in group),unresolved=sum(r[status(col)]=='unresolved' for r in group),percent=100*n/N if N else None))
 return result
def verify_quotes(raw, coded):
 lookup={r['extraction_id']:r for r in coded}
 quotes=read_csv(ROOT/'evidence/quotation_translation_register.csv')
 assert len(quotes)==22 and len({q['evidence_id'] for q in quotes})==22
 assert len({q['article_id'] for q in quotes})==9
 for q in quotes:
  r=raw[q['extraction_id']];c=lookup[q['extraction_id']]
  assert c['article_id']==q['article_id'] and c['id_match_status']=='matched' and c['sipc_present_raw'] in ('yes','weak')
  start,end=int(q['char_start']),int(q['char_end'])
  assert r['full_text'][start:end]==q['quote_vi']
  assert hashlib.sha256(r['full_text'].encode()).hexdigest()==q['source_text_sha256']
  assert r['full_text'][:start].count('\n')+1==int(q['source_line'])
  assert all(q[k]==r[k] for k in ('title','date')) and q['url']==r['real_url']
  assert q['speaker'] and q['translation_en'] and q['attribution_mode']
 return len(quotes)

def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output-dir',type=Path,default=Path(tempfile.gettempdir())/'sipc-results');args=ap.parse_args();out=args.output_dir;out.mkdir(parents=True,exist_ok=True)
 inputs=['data/article_texts_and_open_extraction.csv','data/final_article_coding.xlsx','data/outlet_classification.csv','data/original_article_register.csv','methods/coding_codebook.xlsx']
 raw=unique(read_csv(ROOT/inputs[0]),'ID');mapping=unique(read_csv(ROOT/inputs[2]),'outlet_domain')
 originals=unique(read_csv(ROOT/inputs[3]),'ID')
 wb=openpyxl.load_workbook(ROOT/inputs[1],read_only=True,data_only=True);it=iter(wb['Coded articles'].values);headers=next(it);coded=list(unique([dict(zip(headers,v)) for v in it],'extraction_id').values());wb.close()
 assert set(raw)=={r['extraction_id'] for r in coded},'Extraction/coding ID coverage differs'
 verified_quotes=verify_quotes(raw,coded)
 cols=[c for c in headers if '__' in c and not c.endswith('__status')];dims=list(dict.fromkeys(c.split('__')[0] for c in cols))
 rows=[];excluded=[]
 for c in coded:
  r=raw[c['extraction_id']];assert c['sipc_present_raw']==r['sipc_present_raw']
  if c['id_match_status']=='matched':assert c['article_id'] in originals
  if c['sipc_present_raw'] not in ('yes','weak'):continue
  if c['id_match_status']!='matched':
   excluded.append(dict(extraction_id=c['extraction_id'],article_id=c['article_id'],id_match_status=c['id_match_status'],sipc_present_raw=c['sipc_present_raw'],title=r['title'],date=r['date'],outlet_domain=r['outlet_domain'],reason='Excluded from analytical corpus by matched-status rule on 2026-09-29'))
   continue
  assert r['outlet_domain'] in mapping
  c.update(domain=r['outlet_domain'],group=mapping[r['outlet_domain']]['outlet_type'],date=datetime.strptime(r['date'],'%d/%m/%Y'))
  assert c['group'] in {g for g,p in KEYS}
  for col in cols:
   assert c[status(col)] in ('coded','missing','unresolved'),(c['extraction_id'],col)
   assert c[col] in (0,1) if c[status(col)]=='coded' else c[col] is None,(c['extraction_id'],col,c[col])
  rows.append(c)
 assert len(coded)==1098 and len(rows)==917 and len(excluded)==7,'Frozen corpus size changed; reconcile before updating manuscript'
 assert len({r['article_id'] for r in rows})==917
 write(out/'excluded_records_7.csv',list(excluded[0]),excluded)
 write(out/'analytical_corpus_917_records.csv',['extraction_id','article_id','domain','group','date','sipc_present_raw'],[{k:(r[k].date().isoformat() if k=='date' else r[k]) for k in ['extraction_id','article_id','domain','group','date','sipc_present_raw']} for r in rows])
 findings=compute(rows,cols);fields=list(findings[0]);write(out/'outlet_period_code_frequencies.csv',fields,findings)
 assert [r['eligible_N'] for r in findings[:4]]==[9,433,37,438]
 sensitivity=[]
 for name,rs,cut in [('yes_only',[r for r in rows if r['sipc_present_raw']=='yes'],CUTOFF),('calendar_cutoff',rows,datetime(2023,1,1))]:
  result=compute(rs,cols,cut)
  for i,col in enumerate(cols):sensitivity.append(dict(zip(['analysis','outcome','central_pre_pct','central_post_pct','commercial_pre_pct','commercial_post_pct'],[name,col,*[v['percent'] for v in result[i*4:i*4+4]]])))
 write(out/'sensitivity_checks.csv',list(sensitivity[0]),sensitivity)
 aggregate=[]
 for col in cols:
  vv=[r for r in rows if r[status(col)]=='coded'];n=sum(r[col]==1 for r in vv)
  aggregate.append(dict(outcome=col,n=n,valid_N=len(vv),eligible_N=len(rows),valid_percent=100*n/len(vv),eligible_percent=100*n/len(rows)))
 write(out/'overall_code_frequencies.csv',list(aggregate[0]),aggregate)
 coverage=[dict(dimension=dim,**{s:sum(r[dim+'__status']==s for r in rows) for s in ['coded','missing','unresolved']}) for dim in dims]
 write(out/'coding_completeness_by_dimension.csv',list(coverage[0]),coverage)
 pairs=[]
 for a,b in combinations(cols,2):
  vv=[r for r in rows if r[status(a)]==r[status(b)]=='coded'];N=len(vv);na=sum(r[a]==1 for r in vv);nb=sum(r[b]==1 for r in vv);both=sum(r[a]==r[b]==1 for r in vv)
  pairs.append(dict(code_a=a,code_b=b,joint_valid_N=N,a_n=na,b_n=nb,both_n=both,b_given_a_percent=100*both/na if na else None,a_given_b_percent=100*both/nb if nb else None,lift=both*N/(na*nb) if na*nb else None))
 write(out/'code_cooccurrence.csv',list(pairs[0]),pairs)
 concentration=[]
 for g,p in KEYS:
  gg=[r for r in rows if r['group']==g and ('pre' if r['date']<CUTOFF else 'post')==p]
  for domain,n in sorted(Counter(r['domain'] for r in gg).items()):concentration.append(dict(outlet_type=g,period=p,domain=domain,n=n,cell_N=len(gg),percent=100*n/len(gg)))
 write(out/'outlet_composition_by_period.csv',list(concentration[0]),concentration)
 contrasts=[]
 for i,col in enumerate(cols):
  v=[r['percent'] for r in findings[i*4:i*4+4]]
  contrasts.append(dict(outcome=col,central_change_pp=v[1]-v[0],commercial_change_pp=v[3]-v[2],central_minus_commercial_pre_pp=v[0]-v[2],central_minus_commercial_post_pp=v[1]-v[3],descriptive_interaction_pp=(v[1]-v[0])-(v[3]-v[2])))
 write(out/'outlet_period_percentage_point_differences.csv',list(contrasts[0]),contrasts)
 # Assertions independently tie the output to key manuscript quantities.
 by={r['outcome']:r for r in aggregate}
 for col,n,N in [('future_role__augmentation',498,909),('desirability__positive',810,908),('desirability__negative',328,908),('speaker__learners',71,896),('affected_entities__learners',832,916)]:assert (by[col]['n'],by[col]['valid_N'])==(n,N)
 for dim in coverage:assert dim['coded']+dim['missing']+dim['unresolved']==917
 audit=dict(python=platform.python_version(),openpyxl=openpyxl.__version__,reporting_unit='eligible extraction record',extraction_records=len(coded),presence_counts=dict(Counter(r['sipc_present_raw'] for r in coded)),eligible_records=len(rows),eligible_matched_records=sum(r['id_match_status']=='matched' for r in rows),eligible_unique_matched_ids=len({r['article_id'] for r in rows if r['id_match_status']=='matched'}),cutoff=CUTOFF.date().isoformat(),input_sha256={f:hashlib.sha256((ROOT/f).read_bytes()).hexdigest() for f in inputs},validation='passed',scope='Reproduces numerical summaries from frozen final coding; does not regenerate historical LLM extraction, human coding, qualitative synthesis or manuscript prose.')
 audit.update(verified_quotations=verified_quotes,eligibility_rule="sipc_present_raw in ('yes','weak') and id_match_status == 'matched'",sipc_eligible_before_linkage_filter=924,excluded_by_linkage_status=dict(Counter(r['id_match_status'] for r in excluded)),analysis_presence_counts=dict(Counter(r['sipc_present_raw'] for r in rows)),revision_date='2026-09-29',script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
 (out/'numerical_validation.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
 print(f'Validated {len(rows)} records and {verified_quotes} quotations; reproduced CSV tables in {out}')
if __name__=='__main__':main()
