# Năm future role — dữ liệu hiện hành

Cập nhật 2026-10-17; codebook v3.2. Đã rà ngữ cảnh của 119 account trước đây chưa gán mã, nối được 103 account với role có căn cứ; còn 16 / 3.004 account chưa khớp.

Giữ nguyên năm future role. Phiên bản 3.2 thống nhất mười nhóm tác nhân cho speaker, responsibility và affected_entities; các nhóm có thể chồng lấn trong từng field khi có bằng chứng. Chín field còn lại, gồm desirability, không thay đổi. Future role xác định tương lai đang được nói đến; desirability giữ nguyên cách đánh giá tích cực, tiêu cực, mixed hoặc undecided. Một cảnh báo hay điều kiện triển khai không trở thành một imaginary riêng.

Ưu tiên phát biểu và open extraction đã có; đối chiếu nguồn khi cần làm rõ ngữ cảnh. Chỉ nối khi cùng công cụ, chương trình, đối tượng được đánh giá hoặc cùng mạch lập luận có quy thuộc rõ. Không chuyển thái độ, ý định hay độ chắc chắn từ người nói khác. Dẫn chứng và lý do được lưu ngay trong bộ code gốc; không có bộ code hay thư mục lưu trữ song song. Đây là lượt mã hóa của trợ lý, không phải kiểm định độc lập giữa người mã hóa.

## Mức độ hiện diện

Mẫu chính gồm 828 bài: 424 public/central và 404 commercial/general. Mỗi role được đếm tối đa một lần trong một bài. Một bài có thể có nhiều role nên các tỷ lệ không cộng thành 100%.

| Future role | Toàn mẫu | Public/central | Commercial/general |
|---|---:|---:|---:|
| AI as a Learning Partner | 501 (60.5%) | 250 (59.0%) | 251 (62.1%) |
| AI as a Force Reshaping Educational Judgment | 312 (37.7%) | 153 (36.1%) | 159 (39.4%) |
| AI as an Educational Management Tool | 85 (10.3%) | 55 (13.0%) | 30 (7.4%) |
| AI Literacy as an Educational Imperative | 439 (53.0%) | 247 (58.2%) | 192 (47.5%) |
| AI as a Driver of National Development | 162 (19.6%) | 109 (25.7%) | 53 (13.1%) |

## Các field trong từng role

Tỷ lệ dưới đây tính trên account thuộc role, không ghép các người nói khác nhau trong một bài. File `future_role_profiles.json` có đủ 11 field và phân bố theo hai nhóm outlet.

### AI as a Learning Partner — 1297 account

- Đánh giá: Desirable: 872 (67.2%); Undesirable: 250 (19.3%); Explicitly mixed: 67 (5.2%). MISSING: 108.
- Người nói: Educators, researchers and specialists: 435 (33.5%); Article author or editorial voice: 283 (21.8%); Educational organisations and leadership: 179 (13.8%). MISSING: 29.
- Lý do: Learning quality: 497 (38.3%); Operational feasibility and efficiency: 152 (11.7%); Rights, reliability and academic integrity: 132 (10.2%). MISSING: 460.
- Hành động: Change learning, teaching or assessment practice: 545 (42.0%); Provide resources or implementation capacity: 217 (16.7%); Set rules, safeguards or restrictions: 134 (10.3%). MISSING: 492.

### AI as a Force Reshaping Educational Judgment — 634 account

- Đánh giá: Desirable: 389 (61.4%); Undesirable: 144 (22.7%); Explicitly mixed: 16 (2.5%). MISSING: 84.
- Người nói: Educators, researchers and specialists: 201 (31.7%); Article author or editorial voice: 118 (18.6%); Educational organisations and leadership: 114 (18.0%). MISSING: 17.
- Lý do: Rights, reliability and academic integrity: 289 (45.6%); Learning quality: 92 (14.5%); Operational feasibility and efficiency: 48 (7.6%). MISSING: 229.
- Hành động: Change learning, teaching or assessment practice: 251 (39.6%); Set rules, safeguards or restrictions: 240 (37.9%); Provide resources or implementation capacity: 105 (16.6%). MISSING: 186.

### AI as an Educational Management Tool — 130 account

- Đánh giá: Desirable: 101 (77.7%); Undesirable: 5 (3.8%); Explicitly mixed: 3 (2.3%). MISSING: 21.
- Người nói: Educational organisations and leadership: 31 (23.8%); Public authorities: 26 (20.0%); Article author or editorial voice: 26 (20.0%). MISSING: 2.
- Lý do: Operational feasibility and efficiency: 38 (29.2%); Rights, reliability and academic integrity: 15 (11.5%); Learning quality: 10 (7.7%). MISSING: 65.
- Hành động: Provide resources or implementation capacity: 52 (40.0%); Change learning, teaching or assessment practice: 34 (26.2%); Set rules, safeguards or restrictions: 19 (14.6%). MISSING: 33.

### AI Literacy as an Educational Imperative — 862 account

- Đánh giá: Desirable: 730 (84.7%); Undesirable: 34 (3.9%); Explicitly mixed: 7 (0.8%). MISSING: 91.
- Người nói: Educational organisations and leadership: 242 (28.1%); Public authorities: 181 (21.0%); Educators, researchers and specialists: 171 (19.8%). MISSING: 13.
- Lý do: Learning quality: 256 (29.7%); Employment and economic returns: 145 (16.8%); Operational feasibility and efficiency: 125 (14.5%). MISSING: 269.
- Hành động: Change learning, teaching or assessment practice: 345 (40.0%); Change curriculum content or credentials: 343 (39.8%); Provide resources or implementation capacity: 315 (36.5%). MISSING: 128.

### AI as a Driver of National Development — 217 account

- Đánh giá: Desirable: 199 (91.7%); Undesirable: 7 (3.2%). MISSING: 11.
- Người nói: Public authorities: 56 (25.8%); Educational organisations and leadership: 55 (25.3%); Article author or editorial voice: 46 (21.2%). MISSING: 2.
- Lý do: National development and strategic autonomy: 93 (42.9%); Employment and economic returns: 62 (28.6%); Policy or standards compliance: 27 (12.4%). MISSING: 41.
- Hành động: Provide resources or implementation capacity: 104 (47.9%); Change curriculum content or credentials: 95 (43.8%); Establish coordination or partnerships: 66 (30.4%). MISSING: 30.

## Đánh giá tích cực và tiêu cực

Trong 2760 account của mẫu chính, có 2005 tích cực, 400 tiêu cực, 77 mixed, 1 undecided và 277 MISSING. Có 274/828 bài chứa ít nhất một account tiêu cực. Các tổng này không thay đổi sau khi nối lại future role.

Tần suất hiện diện không tự chứng minh tương lai đã được lựa chọn bằng chính sách hay nguồn lực. Nhãn outlet được kế thừa; không đồng nhất hai nhóm với sở hữu nhà nước/tư nhân. DES_NEGATIVE là đánh giá đối tượng cụ thể, không phải một phép đếm đầy đủ mọi lời phê phán: ủng hộ một biện pháp bảo vệ vẫn có thể được mã tích cực.

## Phần chưa khớp

Các trường hợp còn lại chủ yếu là AI tự đóng vai sinh viên; tác hại deepfake không gắn với một vai trò giáo dục cụ thể; dự báo thị trường, hạ tầng nghiên cứu hoặc phát biểu đổi mới/chính sách quá chung. Nội dung và các field khác vẫn được giữ trong corpus. Không ép mã để đạt bao phủ 100%.
