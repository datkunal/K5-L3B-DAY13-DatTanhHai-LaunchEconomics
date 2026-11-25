# Hồ sơ launch v0 · LogiX-VN · Gate 2a

Nhóm DatTanhHai · L3B · Phạm vi đề nghị: noi_dia + hang_nang, 12 depot. Số chi phí phụ thuộc phút giả lập đều ghi simulated; các biện pháp dưới đây là kế hoạch, chưa phải hệ thống đã triển khai.

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | Toàn mẫu 4.472 đ; phạm vi 3.414 đ, cộng cố định ở quy mô đầy đủ 4.599 đ [simulated] | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | Làm lại gấp đôi +51,8%; xem lại gấp đôi +40,7%; lương +25% làm CPS +23,1% [simulated] | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Nhân viên 12.000 đ/yêu cầu; cả hệ thống trong phạm vi gồm việc chuyển nhân viên và cố định ở quy mô đầy đủ 5.217 đ/yêu cầu, 0,43× [simulated]. quoc_te CPS 22.515 đ, 1,88× [simulated], nên loại; doi_tac 0,85× [simulated] sát ngưỡng, chỉ 68 ca, có điều khoản riêng nên chưa đưa vào | Giả lập | Giám đốc vận hành |
| 4 · Chỉ số chính, dùng, an toàn | Toàn mẫu: 994/1.200 = 82,83%; sửa/bỏ 48/177 = 27,12%; mở lại 51/1.200 = 4,25%. 12 event có trace_id được đặc tả, chưa bật trong hệ thống thật | Xong, có bằng chứng | Trưởng nhóm CSKH |
| 5 · Lỗi và khắc phục | Hai bộ nhãn 20/20 trùng (100%); 5 loại có phát hiện đo được và chủ trách nhiệm; ưu tiên khóa chống trùng và đối soát mỗi giờ | Xong, có bằng chứng | Kỹ sư trưởng agent |
| 6 · Pilot plan | 20 + 20 nhân viên; MDE 6 điểm; 859 hiệu dụng/nhóm, ≥299 yêu cầu/người. Power chỉ 0,64 nếu tác động 5 điểm; ICC ≥0,0233 không đủ mẫu. 6 luật dừng, quyết định 13/01/2027 hoặc 20/01 theo luật 5 | Xong, có bằng chứng | Giám đốc vận hành |
| 7 · Rủi ro kinh tế | Xem lại 100% cả phạm vi: 11.743 đ = 0,98×, cộng cố định 1.185 đ/việc thành 12.928 đ = 1,08×, đắt hơn nhân viên tự làm [simulated]; xử lý: giảm xem lại noi_dia theo bậc khi đạt cổng an toàn. Bước 10% gồm cố định 24.267 đ = 2,02×; hang_nang xem lại 100%: 16.638 đ = 1,39× [simulated], mở lại 8,23%. Giữ xem lại 100% hang_nang, không mở rộng nếu sai gợi ý >7% | Giả lập | PM trợ lý hoàn phí |

Điều kiện pilot (chi tiết trong pilot_plan.yaml):

- Kỹ sư trưởng agent: kiểm tra khóa chống trùng và đối soát sổ cái trước 04/12/2026.
- PM trợ lý hoàn phí: kiểm tra đủ event, reason sai tiền/sai chính sách và đo phút thật trước 04/12/2026; thay đầu vào simulated bằng số đo sau tuần đầu.
- Trưởng nhóm CSKH: rút quyền đối chứng từ 30/11, kiểm tra danh sách ngẫu nhiên 20 + 20 và quyền truy cập ngày 04/12/2026.
- Giám đốc vận hành: ngày 04/12/2026 ký chấp nhận MDE 6 điểm, power 0,64 tại 5 điểm và ngân sách bước đầu chưa tiết kiệm; kiểm tra baseline đối chứng, chốt mục tiêu trước 21/12.
- Trưởng ca CSKH, kiểm tra ngày 13/12/2026 (hết bước 10%) và 20/12/2026 (hết bước 25%): bước 10% xem lại 100%, dừng nếu sai gợi ý >10% trong 3 ngày liên tiếp; luật mở lại +2 điểm hoặc trần 6% chỉ đủ dữ liệu từ 15/12. Chỉ giảm xem lại khi đạt cổng an toàn; ngưỡng CPS biến đổi 8.000 đ áp ở bước 50%.

Đánh giá chính dùng bước 50% từ 21/12–03/01, chờ đủ kết quả đến 11/01. Chỉ kéo dài một lần vì nhiễm đối chứng theo luật 5; vẫn dưới 10 ngày sạch thì không đủ bằng chứng để mở rộng. Không diễn giải 82,83% là cải thiện do trợ lý.

**Đề xuất: Go có điều kiện** — chỉ duyệt pilot khi đủ các điều kiện trên, chưa đề nghị mở rộng ngay.
