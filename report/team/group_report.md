# Báo cáo nhóm · LAB13

## 1. Thông tin nhóm

DatTanhHai · L3B · 3 thành viên: Vũ Tuấn Đạt, Trần Tuấn Anh, Nguyễn Trung Hải. Thông tin và phân vai tại TEAM.md.

## 2. Mục tiêu và cách tiếp cận

Đánh giá trợ lý hoàn phí bằng 1.200 yêu cầu và 1.624 lần chạy giả lập; tính đủ token, tool, xem lại và làm lại, phân tích theo loại rồi thiết kế pilot có đối chứng để kiểm chứng giá trị kinh tế và an toàn.

## 3. Giải pháp

- A–B: lab13.py tính chi phí, 9 kịch bản độ nhạy và chi phí cả hệ thống; số tại bang_chi_phi.md.
- C: bang_loi.md lưu hai bộ nhãn 20 ca, đồng thuận và cách khắc phục đủ 5 loại lỗi.
- D: pilot_plan.yaml chia ngẫu nhiên theo nhân viên, 20 + 20, MDE 6 điểm, lịch đo và 6 luật dừng.
- E: chi_so.md đặc tả 5 chỉ số, 12 event có trace_id và 4 rủi ro; ho_so_launch_v0.md tổng hợp 7 mục và điều kiện pilot.

## 4. Kết quả

Ba phép thử A1 đạt. CPS toàn mẫu 4.472 đ; CPS trong phạm vi 3.414 đ [simulated]. Chi phí cả hệ thống trong phạm vi gồm cố định ở quy mô đầy đủ là 5.217 đ/yêu cầu [simulated]. Ba chỉ số toàn mẫu: 82,83%, 27,12%, 4,25%. Hai bộ nhãn trùng 20/20 = 100%.

Đề xuất Go có điều kiện cho noi_dia + hang_nang. Bước 10% gồm cố định 24.267 đ = 2,02×; hang_nang xem lại 100% 16.638 đ = 1,39× [simulated]. Phải đo phút thật và kiểm soát lỗi trước giảm xem lại. Pilot 20 + 20 đủ mục tiêu 6 điểm theo giả định ICC 0,02; tác động 5 điểm chỉ có power 0,64.

Duyệt chéo: chưa thực hiện theo xác nhận của Hải; chưa có điểm hoặc nhận xét từ hội đồng, chưa có điểm nhóm chấm nhóm khác. Phiếu chấm giữ trạng thái chờ, không tự tạo kết quả.

## 5. Khó khăn và cách xử lý

Nhóm có 3 người thay vì 4; Hải xác nhận coach đã chấp nhận. Nhóm gộp vai, vẫn giữ hai người gắn nhãn, code A–B do Đạt và D do Tuấn Anh thực hiện. Máy của Hải thiếu statsmodels; Codex tạo src/.venv và cài requirements.txt, sau đó chạy hết script thành công.

## 6. Tổng hợp đóng góp

Đạt: A–B, mô hình chi phí và bảng độ nhạy. Tuấn Anh: D1/D3, kế hoạch pilot, kiểm số và nhãn bộ 1. Hải: nhãn bộ 2, tổng hợp bảng lỗi, chỉ số, event, hồ sơ launch và báo cáo nhóm; dùng Codex hỗ trợ soạn thảo và kiểm tra. Chi tiết tại TEAM.md.

## 7. Hạn chế và hướng cải thiện

Chưa có đối chứng trong đợt chạy thử; không suy luận nhân quả. Chi phí dùng phút simulated. ICC, baseline và giả định duy trì tỷ lệ lỗi cần xác nhận; từ ICC 0,0233, 20 cụm/nhóm không đủ 859 hiệu dụng. Phải đo phút thật, ghi lý do sửa/bỏ và kiểm tra độc lập lỗi ngầm. Luật 5 chỉ cho gia hạn một lần, ngày quyết định dự phòng 20/01/2027; thiếu mẫu thì không kết luận mở rộng.

## 8. Tài liệu tham khảo

README.md, RULES.md, CHECKPOINTS.md, RUBRIC.md, SUBMISSION.md; docs/du_lieu_va_cong_thuc.md; đề bài và hướng dẫn LAB13 trong docs/. Số liệu lấy từ src/lab13.py, bảng A–B và D1/D3/E1.
