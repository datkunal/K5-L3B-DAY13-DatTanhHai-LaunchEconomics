# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: **Tuấn Anh** · Người gắn nhãn 2: **Hải** 



| Ca | Tuấn Anh | Hải | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Hệ thống | Có | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** 20 / 20 = 100% 

## Quy tắc phân biệt cho các ca không trùng

Không có ca không trùng. Ghi lại quy tắc cho các ca dễ lẫn:

- Ca 6, 9: gốc là khách chọn sai mục hoặc nhập sai mã, nên là Do người dùng; việc trợ lý không gợi ý là chỗ cần sửa.
- Ca 13: gốc là yêu cầu ngoài phạm vi, nên là Giới hạn hệ thống; trả lời không rõ là chỗ cần sửa.
- Ca 8, 15: sai so với chính sách và đề không nói bị bỏ sót, hoặc nhân viên đã bắt được, nên là Hệ thống, không phải Ngầm.
- Ca 10, 16, 18: đúng thiết kế hoặc chính sách, chỉ không khớp kỳ vọng của khách, nên là Ngữ cảnh.
- Ca 12: kết quả đúng nhưng chi phí gấp 3 lần suốt 3 tuần không ai thấy, nên là Ngầm; sai về chi phí cũng là sai.
- Ca 20: khách gửi lại là hành vi bình thường, gốc là thiếu khoá chống trùng, nên là Hệ thống.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 6 | Do người dùng | Event `category_mismatch_detected` khi mục khách chọn khác loại suy ra từ mô tả; đếm mỗi ngày, cảnh báo khi vượt 2% số yêu cầu | Trước khi từ chối, hỏi lại một câu để khách xác nhận mục, rồi chuyển sang luồng đúng; không xác định được thì chuyển nhân viên kèm tóm tắt | PM trợ lý hoàn phí |
| 20 | Hệ thống | Đối soát sổ cái mỗi giờ: hai `refund_ledger_write` ok cho cùng một đơn; ngưỡng 0 ca, từ 1 ca là tắt trợ lý trong 30 phút (luật dừng 2 của `pilot_plan.yaml`) | Khoá chống trùng theo mã đơn ở dịch vụ sổ cái; thu hồi hoặc bù trừ khoản thừa và báo khách; gửi xác nhận "đã nhận yêu cầu" ngay để khách khỏi gửi lại | Kỹ sư trưởng agent |
| 10 | Ngữ cảnh | Event `ticket_reopened` có lý do "không đồng ý chính sách" mà kiểm tra thấy quyết định đúng; báo cáo mỗi tuần, ngưỡng 1% số yêu cầu | Tin nhắn từ chối ghi rõ điều khoản bất khả kháng và lý do (bão, ngày); ứng dụng ẩn dòng "cam kết giao 24 giờ" ở khu vực đang có thiên tai | Trưởng nhóm CSKH |
| 13 | Giới hạn hệ thống | Event `handoff_to_staff` với `reason = ngoai_pham_vi`, và kiểm tra mẫu 50 hội thoại mỗi tuần tìm ca ngoài phạm vi không được chuyển; ngưỡng 2% | Nhận diện yêu cầu bảo hiểm, nói rõ là không xử lý được, đưa kênh liên hệ công ty bảo hiểm và chuyển nhân viên kèm tóm tắt | PM trợ lý hoàn phí |
| 5 | Ngầm | Event `audit_sample_checked`: kế toán tính lại 100 đơn mỗi tuần, gồm ít nhất 30 đơn có mã giảm giá; ngưỡng 1% đơn lệch tiền | Sửa quy tắc để hoàn theo số tiền khách thực trả, thêm test cho đơn có mã giảm giá, rà lại các đơn đã hoàn từ ngày có lỗi | Kế toán trưởng |
