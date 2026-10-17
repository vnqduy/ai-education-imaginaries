"""Summarize the canonical corpus; no backup inputs or parallel coding files."""
import collections
import csv
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def main():
    records=[json.loads(s) for s in (ROOT/'data/sipc_future_coding/coded_corpus.jsonl').read_text().splitlines()]
    book=json.loads((ROOT/'data/sipc_future_coding/codebook.json').read_text())
    manifest=json.loads((ROOT/'data/sipc_future_coding/manifest.json').read_text())
    with (ROOT/'results/article_coding.csv').open() as f: meta={r['article_id']:r for r in csv.DictReader(f)}
    main_records=[r for r in records if meta[r['ID']]['main_sample']=='1']
    fields=[f for f in book['fields'] if f!='future_role']
    names={e['code']:e['label'] for entries in book['fields'].values() for e in entries}
    groups=['all','public/central','commercial/general']
    out={'version':book['version'],'article_denominator':'Existing main_sample: clear_future and not publisher_uncertain.',
         'role_prevalence':'Each role counted once per article; roles can coexist.',
         'field_profiles':'Counts within the same attributed account as the role. Missing included in denominators. Multiple roles/codes may coexist. Context-linked roles identify the target of a warning or condition, not necessarily an endorsed future.',
         'groups':{},'unmatched_accounts':sum(a['codes']['future_role']==['MISSING'] for r in records for a in r['accounts'])}
    for g in groups:
        rr=[r for r in main_records if g=='all' or meta[r['ID']]['outlet_group']==g];aa=[a for r in rr for a in r['accounts']]
        z={'articles':len(rr),'accounts':len(aa),'desirability_accounts':dict(collections.Counter(a['codes']['desirability'][0] for a in aa)),
           'articles_with_negative_account':sum(any('DES_NEGATIVE' in a['codes']['desirability'] for a in r['accounts']) for r in rr),'roles':{}}
        for e in book['fields']['future_role']:
            role=e['code'];matched=[a for a in aa if role in a['codes']['future_role']]
            n=sum(any(role in a['codes']['future_role'] for a in r['accounts']) for r in rr)
            z['roles'][role]={'label':e['label'],'articles':n,'article_percent':round(100*n/len(rr),2),'accounts':len(matched),
                             'field_counts':{f:dict(collections.Counter(c for a in matched for c in a['codes'][f])) for f in fields}}
        out['groups'][g]=z
    (ROOT/'results/future_role_profiles.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    rev=manifest['future_role_revision'];z=out['groups']['all'];updated=manifest.get('actor_revision', rev)['date']
    lines=['# Năm future role — dữ liệu hiện hành','',f"Cập nhật {updated}; codebook v{book['version']}. Đã rà ngữ cảnh của {rev['context_reviewed']} account trước đây chưa gán mã, nối được {rev['context_resolved']} account với role có căn cứ; còn {out['unmatched_accounts']} / 3.004 account chưa khớp.",'',
           'Giữ nguyên năm future role. Phiên bản 3.2 thống nhất mười nhóm tác nhân cho speaker, responsibility và affected_entities; các nhóm có thể chồng lấn trong từng field khi có bằng chứng. Chín field còn lại, gồm desirability, không thay đổi. Future role xác định tương lai đang được nói đến; desirability giữ nguyên cách đánh giá tích cực, tiêu cực, mixed hoặc undecided. Một cảnh báo hay điều kiện triển khai không trở thành một imaginary riêng.','',
           'Ưu tiên phát biểu và open extraction đã có; đối chiếu nguồn khi cần làm rõ ngữ cảnh. Chỉ nối khi cùng công cụ, chương trình, đối tượng được đánh giá hoặc cùng mạch lập luận có quy thuộc rõ. Không chuyển thái độ, ý định hay độ chắc chắn từ người nói khác. Dẫn chứng và lý do được lưu ngay trong bộ code gốc; không có bộ code hay thư mục lưu trữ song song. Đây là lượt mã hóa của trợ lý, không phải kiểm định độc lập giữa người mã hóa.','',
           '## Mức độ hiện diện','',
           'Mẫu chính gồm 828 bài: 424 public/central và 404 commercial/general. Mỗi role được đếm tối đa một lần trong một bài. Một bài có thể có nhiều role nên các tỷ lệ không cộng thành 100%.','',
           '| Future role | Toàn mẫu | Public/central | Commercial/general |','|---|---:|---:|---:|']
    for e in book['fields']['future_role']:
        cells=[]
        for g in groups:
            v=out['groups'][g]['roles'][e['code']];cells.append(f"{v['articles']} ({v['article_percent']:.1f}%)")
        lines.append('| '+e['label']+' | '+' | '.join(cells)+' |')
    lines+=['','## Các field trong từng role','','Tỷ lệ dưới đây tính trên account thuộc role, không ghép các người nói khác nhau trong một bài. File `future_role_profiles.json` có đủ 11 field và phân bố theo hai nhóm outlet.']
    for e in book['fields']['future_role']:
        v=z['roles'][e['code']];n=v['accounts'];lines+=['',f"### {e['label']} — {n} account",'']
        for f,title in [('desirability','Đánh giá'),('speaker','Người nói'),('rationale','Lý do'),('action','Hành động')]:
            counts=v['field_counts'][f];ranked=sorted(((c,k) for k,c in counts.items() if k!='MISSING'),reverse=True)[:3]
            desc='; '.join(f'{names[k]}: {c} ({100*c/n:.1f}%)' for c,k in ranked)
            lines.append(f"- {title}: {desc}. MISSING: {counts.get('MISSING',0)}.")
    lines+=['','## Đánh giá tích cực và tiêu cực','',
            f"Trong {z['accounts']} account của mẫu chính, có {z['desirability_accounts'].get('DES_POSITIVE',0)} tích cực, {z['desirability_accounts'].get('DES_NEGATIVE',0)} tiêu cực, {z['desirability_accounts'].get('DES_MIXED',0)} mixed, {z['desirability_accounts'].get('DES_UNDECIDED',0)} undecided và {z['desirability_accounts'].get('MISSING',0)} MISSING. Có {z['articles_with_negative_account']}/828 bài chứa ít nhất một account tiêu cực. Các tổng này không thay đổi sau khi nối lại future role.",'',
            'Tần suất hiện diện không tự chứng minh tương lai đã được lựa chọn bằng chính sách hay nguồn lực. Nhãn outlet được kế thừa; không đồng nhất hai nhóm với sở hữu nhà nước/tư nhân. DES_NEGATIVE là đánh giá đối tượng cụ thể, không phải một phép đếm đầy đủ mọi lời phê phán: ủng hộ một biện pháp bảo vệ vẫn có thể được mã tích cực.','',
            '## Phần chưa khớp','',
            'Các trường hợp còn lại chủ yếu là AI tự đóng vai sinh viên; tác hại deepfake không gắn với một vai trò giáo dục cụ thể; dự báo thị trường, hạ tầng nghiên cứu hoặc phát biểu đổi mới/chính sách quá chung. Nội dung và các field khác vẫn được giữ trong corpus. Không ép mã để đạt bao phủ 100%.','']
    (ROOT/'results/future_role_summary.md').write_text('\n'.join(lines))
    print(json.dumps({'version':book['version'],'unmatched':out['unmatched_accounts'],'main_articles':len(main_records)}))
if __name__=='__main__':main()
