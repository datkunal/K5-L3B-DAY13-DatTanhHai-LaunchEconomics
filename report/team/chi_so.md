# Chỉ số, event và rủi ro kinh tế · Nhiệm vụ E

## E1 · Đặc tả chỉ số

Số do `src/lab13.py`, bảng E1 và D3 tính từ dữ liệu giả lập của lab. Đây là chỉ số trong đợt chạy thử, chưa có đối chứng để kết luận tác động.

| Loại | Chỉ số và công thức | Kết quả toàn mẫu |
| --- | --- | --- |
| Chính | Số yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày / tổng yêu cầu | 994/1.200 = 82,83% |
| Dùng | Số quyết định sửa hoặc bỏ / số yêu cầu được xem lại | 48/177 = 27,12% |
| An toàn | Số yêu cầu mở lại trong 7 ngày / tổng yêu cầu | 51/1.200 = 4,25% |
| Dùng, đề xuất | Số yêu cầu can thiệp trong phạm vi có mở trợ lý / tổng yêu cầu can thiệp trong phạm vi; theo tuần, đếm request_id duy nhất | Chưa đo; ngưỡng kế hoạch ≥70% |
| An toàn, đề xuất | Số yêu cầu sai tiền qua kiểm tra / số yêu cầu được kiểm tra ngẫu nhiên; theo tuần, báo riêng từng loại và số mẫu | Chưa đo; kiểm tra 100 yêu cầu/tuần, cảnh báo khi >1% |

Trong phạm vi noi_dia + hang_nang: chỉ số chính 906/982 = 92,26%; mở lại 39/982 = 3,97%. hang_nang mở lại 13/158 = 8,23%. Không dùng baseline giả định 70% để tuyên bố mức cải thiện.

Quy ước pilot: nhóm theo phân công ban đầu; chỉ số chính dùng bước 50%; chỉ kết luận sau khi đủ 24 giờ và 7 ngày theo dõi. Quyết định sửa/bỏ tính trên yêu cầu được xem lại có quyết định cuối; thiếu event phải báo riêng, không mặc định là giữ.

## Danh sách event

Mọi event có `trace_id`, `request_id`, `event_id`, `occurred_at`; bảng phân công lưu staff_id, arm, depot và phiên bản phân công. Chống ghi trùng bằng event_id, nối nhiều lần chạy qua request_id.

| Event | Ai tạo | Thuộc tính bổ sung | Thời điểm |
| --- | --- | --- | --- |
| refund_request_created | Hệ thống ticket | loai, staff_id, arm, depot, created_at, trace_id | Nhận yêu cầu |
| agent_opened | Giao diện nhân viên | staff_id, arm, trace_id | Mở trợ lý, kể cả tài khoản đối chứng |
| agent_run_completed | Agent | attempt, tokens_in, tokens_out, tool_calls, status, trace_id | Sau mọi lần chạy |
| agent_suggestion_shown | Giao diện nhân viên | suggestion_id, staff_id, so_tien_de_xuat, trace_id | Hiển thị gợi ý |
| staff_review_decision | Giao diện nhân viên | suggestion_id, giu/sua/bo, phut_xem_lai đo thật, final, reason (sai_tien/sai_chinh_sach/khac), is_incorrect, trace_id | Chốt xem lại |
| staff_rework_completed | Giao diện nhân viên | phut_lam_lai đo thật, reason, trace_id | Xong làm lại |
| refund_ledger_write | Dịch vụ sổ cái | idempotency_key, amount, result, policy_version, trace_id | Mỗi lần ghi sổ |
| handoff_to_staff | Agent | reason, summary, trace_id | Chuyển nhân viên |
| category_mismatch_detected | Giao diện tiếp nhận | category_selected, category_inferred, confirmed_category, trace_id | Phát hiện mục chọn không khớp mô tả |
| ticket_closed | Hệ thống ticket | closed_at, trace_id | Đóng yêu cầu |
| ticket_reopened | Hệ thống ticket | reopened_at, reason, trace_id | Mở lại |
| audit_sample_checked | Kế toán | sample_id, selection_probability, amount_actual, amount_correct, policy_version, trace_id | Kiểm tra mẫu mỗi tuần |

arm lấy từ bảng phân công đã chốt, nhận giá trị treatment/control; không suy ra arm từ việc có mở trợ lý. reason bắt buộc khi sửa/bỏ; is_incorrect ghi rõ lỗi tiền/chính sách, vì sửa văn phong không đồng nghĩa gợi ý sai.

Đối chiếu event với chỉ số:

- Chính: refund_request_created + ticket_closed + ticket_reopened; created_at đến closed_at ≤24 giờ và không mở lại trong cửa sổ 7 ngày sau đóng.
- Bỏ qua: staff_review_decision, đếm quyết định cuối theo request_id; suggestion_shown kiểm tra gợi ý có thực sự hiện.
- Mở lại: ticket_reopened + ticket_closed; chỉ dùng đoàn hệ đã đủ 7 ngày theo dõi sau đóng.
- Mức sử dụng và nhiễm đối chứng: agent_opened + refund_request_created + bảng phân công; đếm yêu cầu duy nhất.
- Luật 6: số yêu cầu xem lại có is_incorrect và reason sai_tien hoặc sai_chinh_sach / toàn bộ yêu cầu có quyết định xem lại cuối; bước 10% xem lại 100%, theo dõi 3 ngày liên tiếp, ngưỡng >10%. Thiếu reason phải báo lỗi dữ liệu, không tính là đúng.
- Luật 4: bỏ qua >40% hoặc sử dụng <70%; luật 5: tỷ lệ yêu cầu đối chứng có agent_opened >2%, theo cửa sổ 7 ngày.
- Sai tiền: audit_sample_checked, đối chiếu refund_ledger_write và bảng giá; không chỉ kiểm tra ca đã được nhân viên phát hiện.
- Chi phí: agent_run_completed + staff_review_decision + staff_rework_completed; tách phút đo thật với phút simulated, cộng mọi lần chạy.

## E2 · Rủi ro kinh tế

Số tham chiếu từ bang_chi_phi.md (B1, B4) và pilot_plan.yaml (D3), đều simulated khi có chi phí nhân viên.

| Rủi ro | Tác động đã tính | Theo dõi | Hành động | Phụ trách |
| --- | --- | --- | --- | --- |
| Làm lại tăng gấp đôi | CPS toàn mẫu 6.787 đ, +51,8% [simulated] | Ca làm lại và phút làm lại theo tuần, từng loại | Nếu CPS biến đổi bước 50% >8.000 đ trong 7 ngày, dừng mở rộng và thu hẹp noi_dia theo pilot | PM trợ lý hoàn phí |
| Xem lại toàn bộ kéo dài | Trong phạm vi 11.743–12.415 đ, chưa cố định [simulated] | Phút xem lại thật; ≥6 phút trong 7 ngày kích hoạt luật dừng | Chỉ giảm xem lại noi_dia theo cổng an toàn; hang_nang giữ 100% | Trưởng nhóm CSKH |
| Pilot nhỏ gánh chi phí cố định | Bước 10%: 24.267 đ = 2,02×; bước 50%: 8.010 đ = 0,67×, gồm cố định [simulated] | Khối lượng, CPS có và không có cố định mỗi tuần | Duyệt ngân sách học thử trước khi chạy; không tuyên bố tiết kiệm ở bước đầu | Giám đốc vận hành |
| hang_nang chưa kinh tế khi kiểm toàn bộ | 16.638 đ = 1,39×, chưa cố định [simulated]; mở lại 8,23% | Sai gợi ý qua xem lại và mở lại đã đủ cửa sổ | Không mở rộng nếu sai gợi ý >7%; giữ xem lại 100% | PM trợ lý hoàn phí |

## Giới hạn khi diễn giải luật dừng

Luật 1 chỉ đủ dữ liệu mở lại từ 15/12/2026; trước đó dùng đối soát mỗi giờ và luật 6. Bảng D3 dùng xấp xỉ chuẩn: xác suất vượt ngưỡng sai >10% sau 3 ngày là 0,5% nếu tỷ lệ thật 5,06%, 50% nếu thật 10%, 94,4% nếu thật 15%. Đây là xác suất tại một lần đánh giá, không phải xác suất thỏa cả chuỗi 3 ngày liên tiếp.

Tương tự, xác suất vượt trần mở lại 6% tại các bước là 9,2% / 1,8% / 0,1% theo giả định ICC 0,02; không suy thành xác suất dừng của toàn pilot. Khi nhiễm đối chứng, bỏ ngày nhiễm ở cả hai nhóm; chỉ kéo dài một lần nếu còn dưới 10 ngày sạch, quyết định dự phòng 20/01/2027.
