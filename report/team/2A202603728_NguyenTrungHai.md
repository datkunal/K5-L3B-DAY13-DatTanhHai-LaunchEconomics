# Báo cáo cá nhân — NguyenTrungHai-2A202603728

## 1. Thông tin thành viên

- Họ tên: Nguyễn Trung Hải
- MSSV: 2A202603728
- Email: trunghaicva@gmail.com
- Vai: người gắn nhãn 2, kiêm giữ hồ sơ; nhiệm vụ C, E.

## 2. Phần việc phụ trách

Gắn nhãn bộ 2 cho 20 ca; tổng hợp bảng lỗi, chỉ số và event, rủi ro kinh tế, hồ sơ launch v0 và báo cáo nhóm. Phối hợp nhóm bảo vệ đề xuất và duyệt chéo khi được tổ chức.

## 3. Đóng góp cụ thể

- bang_loi.md: bộ nhãn của Hải; hai bộ nhãn trùng 20/20, bảng khắc phục 5 loại.
- chi_so.md: 3 chỉ số tính thử, 2 chỉ số đề xuất; 12 event, có lý do sửa/bỏ để đo luật 6 và lượt mở trợ lý để đo luật 4/5; 4 rủi ro kinh tế.
- src/lab13.py: bổ sung bảng E1 in tử số, mẫu số và tỷ lệ ba chỉ số.
- ho_so_launch_v0.md: 7 mục, phạm vi noi_dia + hang_nang, đề xuất Go có điều kiện, nêu chi phí bước đầu và giới hạn power/ICC.
- group_report.md và TEAM.md: tổng hợp đóng góp và trạng thái thực tế.

## 4. Bằng chứng

- Nhãn 20 ca tại bang_loi.md (cập nhật trên repo ở commit 7879e7c).
- E1: 994/1.200 = 82,83%; 48/177 = 27,12%; 51/1.200 = 4,25%.
- CPS toàn mẫu 4.472 đ [simulated]; 6 luật dừng trong pilot_plan.yaml, ngày quyết định 13/01/2027, dự phòng 20/01 theo luật 5.
- Hải xác nhận đã tự chạy script và kiểm lại phép tính; kiểm tra bằng công cụ của Codex cũng chạy hết script và đọc YAML thành công. Chưa ghi nhận phép tính tay cụ thể để tránh gán một thao tác chưa xác nhận.

## 5. Công cụ AI đã dùng

Codex hỗ trợ đọc yêu cầu, kiểm tra Git, bổ sung code E1, soạn chỉ số/event, hồ sơ launch, báo cáo và rà tính nhất quán. Số được đối chiếu với đầu ra lab13.py; ba phép thử A1 đạt, YAML đọc được, các đầu vào thời gian giả lập được ghi simulated. Bộ nhãn do thành viên cung cấp, Codex không thay đổi nhãn gốc và không tạo điểm duyệt chéo.

## 6. Tự đánh giá

Hoàn thiện phần tổng hợp để quyết định pilot gắn với bằng chứng, nêu cả chi phí bước 10% 24.267 đ = 2,02× và hang_nang 16.638 đ = 1,39× [simulated]. Hiểu rằng chưa có đối chứng nên không thể quy 82,83% cho tác động trợ lý; phải giữ cảnh báo power 0,64 ở mức 5 điểm. Hạn chế: phút simulated, chưa có kết quả duyệt chéo, hiệu quả thực tế và ICC cần kiểm chứng qua pilot. Cần đọc lại bản báo cáo và tự giải thích các số trước hội đồng.
