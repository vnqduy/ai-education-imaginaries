"""Independent source audit; does not read manuscript or existing semantic codes.
Run with python3 analysis/fresh_review_2026-10-15/audit_raw.py.
Similarity and lexical flags are screening aids, not validated coding.
"""
import collections, csv, datetime, hashlib, json, re
from pathlib import Path
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
source = ROOT / 'data/source_corpus.jsonl'
rows = [json.loads(x) for x in source.read_text().splitlines() if x.strip()]
def write_csv(name, data):
    if not data: return
    with (OUT/name).open('w', newline='', encoding='utf-8-sig') as f:
        w=csv.DictWriter(f, fieldnames=list(data[0])); w.writeheader(); w.writerows(data)

byyear=collections.Counter(); byoutlet=collections.Counter(); yearoutlet=collections.Counter()
for r in rows:
    r['parsed_date']=datetime.datetime.strptime(r['date'],'%d/%m/%Y').date()
    byyear[r['parsed_date'].year]+=1;byoutlet[r['outlet_domain']]+=1
    yearoutlet[(r['parsed_date'].year,r['outlet_domain'])]+=1
write_csv('year_outlet_counts.csv',[dict(year=y,outlet=o,n=n) for (y,o),n in sorted(yearoutlet.items())])
titles=collections.defaultdict(list)
for r in rows: titles[r['title']].append(r)
dups=[v for v in titles.values() if len(v)>1]
write_csv('duplicate_titles.csv',[dict(title=v[0]['title'],n=len(v),ids=' | '.join(r['ID'] for r in v),urls=' | '.join(r['real_url'] for r in v)) for v in dups])
# Word bigram TF-IDF is used only to nominate similar full retained texts.
# Boilerplate remains present: every candidate requires body-level adjudication.
X=TfidfVectorizer(ngram_range=(2,2),min_df=2,sublinear_tf=True).fit_transform([r['full_text'] for r in rows])
S=(X@X.T).toarray(); pairs=[]
for i,j in zip(*np.where(np.triu(S,k=1)>=.80)):
    a,b=rows[i],rows[j]
    pairs.append(dict(id_a=a['ID'],id_b=b['ID'],cosine=round(float(S[i,j]),6),title_a=a['title'],title_b=b['title'],same_host=a['outlet_domain']==b['outlet_domain']))
pairs.sort(key=lambda r:-r['cosine']);write_csv('similar_text_candidates.csv',pairs)
pattern={
    'ai_term':r'\bAI\b|trí tuệ nhân tạo|trí thông minh nhân tạo|Chat\s?GPT',
    'genai_named':r'Chat\s?GPT|Gemini|Copilot|Claude|DeepSeek|AI tạo sinh|AI sinh tạo|trí tuệ nhân tạo tạo sinh',
    'workforce':r'nhân lực|lực lượng lao động|thị trường lao động|việc làm',
    'learning_process':r'tư duy|tự học|phản biện|sáng tạo',
    'integrity':r'gian lận|đạo văn|liêm chính',
    'privacy':r'quyền riêng tư|bảo vệ dữ liệu|bảo mật dữ liệu',
    'equity':r'bất bình đẳng|bình đẳng|công bằng|khoảng cách số|khuyết tật',
    'inevitability':r'tất yếu|không thể đảo ngược|không thể đứng ngoài|không thể tránh',
}
flags=[]
for r in rows:
    f=dict(ID=r['ID'],year=r['parsed_date'].year,outlet=r['outlet_domain'],title=r['title'])
    f.update({k:int(bool(re.search(p,r['full_text'],re.I))) for k,p in pattern.items()});flags.append(f)
write_csv('lexical_screen_NOT_semantic_codes.csv',flags)
summary=dict(source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),n=len(rows),n_outlets=len(byoutlet),
    min_date=str(min(r['parsed_date'] for r in rows)),max_date=str(max(r['parsed_date'] for r in rows)),
    years=dict(sorted(byyear.items())),outlets=dict(byoutlet.most_common()),
    unique_ids=len({r['ID'] for r in rows}),unique_urls=len({r['real_url'] for r in rows}),
    unique_exact_texts=len({r['full_text'] for r in rows}),duplicate_title_groups=len(dups),
    articles_in_duplicate_title_groups=sum(map(len,dups)),duplicate_title_excess=sum(len(v)-1 for v in dups),
    similarity_pairs_ge_080=len(pairs),similarity_pairs_ge_095=sum(p['cosine']>=.95 for p in pairs),
    similarity_flagged_articles=len({p[k] for p in pairs for k in ['id_a','id_b']}),
    lexical_counts={k:sum(f[k] for f in flags) for k in pattern},
    warning='Lexical and similarity outputs are unvalidated screens on retained text including boilerplate; not substantive prevalence estimates.')
(OUT/'raw_audit_summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2))
print(json.dumps(summary,ensure_ascii=False,indent=2))
print('TOP SIMILARITY CANDIDATES',json.dumps(pairs[:16],ensure_ascii=False))
