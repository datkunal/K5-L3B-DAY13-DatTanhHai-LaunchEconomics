# Team

## Thông tin nhóm

- Tên nhóm: DatTanhHai (3 người)
- Lớp: L3B
- Repo nhóm: `K5-L3B-DAY13-DatTanhHai-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: https://github.com/datkunal/K5-L3B-DAY13-DatTanhHai-LaunchEconomics · `main` · commit cuối trước 23h59 ngày 25/11/2026

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Vũ Tuấn Đạt | 2A202603744 | 26ai.datvt@vinuni.edu.vn | datkunal | Nhóm trưởng, người viết code (nhiệm vụ A, B) |
|   2 | Trần Tuấn Anh | 2A202603909 | 26ai.anhtt6@vinuni.edu.vn | Tanh0406 | Người kiểm số, viết code D1, người gắn nhãn 1 (nhiệm vụ D) |
|   3 | Nguyễn Trung Hải | 2A202603728 | trunghaicva@gmail.com | nguyentrunghai7 | Người gắn nhãn 2, kiêm giữ hồ sơ (nhiệm vụ C, E) |

Nhóm có 3 người nên gộp bốn vai của lab. Vẫn giữ hai người gắn nhãn khác nhau cho CP3; người viết code (Đạt) không gắn nhãn. Người viết code đổi từ Đạt (A, B) sang Tuấn Anh (D1), nên ít nhất hai người tự tay tính được.

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/team/` theo dạng `MSSV_HoTen.md`.

## VuTuanDat-2A202603744

### Phần việc phụ trách

- Nhiệm vụ A (CP1) và B (CP2): mô hình chi phí, bảng độ nhạy.
- Tạo repo nhóm, mời thành viên, phân việc.

### Đóng góp cụ thể

- `src/lab13.py`: ba hàm A1, `mo_hinh`, các bảng A2–A4 và B1–B4.
- `report/team/bang_chi_phi.md`: điền toàn bộ A1–A4, B1–B4.

### Bằng chứng

- `cd src && python lab13.py` in `Ba phép thử đáp án biết trước: ĐẠT` và chi phí mỗi việc thành công 4.472 đ [simulated].
- Lịch sử commit của `datkunal` trên `src/lab13.py`, `report/team/bang_chi_phi.md`, `TEAM.md`.
- Báo cáo cá nhân: `report/team/2A202603744_VuTuanDat.md`.

## TranTuanAnh-2A202603909

### Phần việc phụ trách

- Nhiệm vụ D (CP4): cỡ mẫu D1, kế hoạch pilot.
- Kiểm lại số phần A trên máy khác; gắn nhãn bộ 1 cho 20 ca lỗi (CP3); điền phiếu chấm sau duyệt chéo.

### Đóng góp cụ thể

- `src/lab13.py`: các hàm cỡ mẫu và chi phí theo bậc xem lại, bảng D1 và D3.
- `report/team/pilot_plan.yaml`: D1, D2, đánh đổi và toàn bộ các trường, 6 luật dừng.
- `report/team/bang_loi.md`: bộ nhãn 1 cho 20 ca lỗi, tự gắn độc lập.

### Bằng chứng

- `cd src && python lab13.py` in D1: 1.251 · 3.103 (42 người mỗi nhóm) · 1.000 · 300 · 299.
- Lịch sử commit của `Tanh0406` trên `src/lab13.py`, `report/team/pilot_plan.yaml`, `TEAM.md`.
- Báo cáo cá nhân: `report/team/2A202603909_TranTuanAnh.md`.

## NguyenTrungHai-2A202603728

### Phần việc phụ trách

- Người gắn nhãn 2, kiêm giữ hồ sơ; nhiệm vụ C và E.

### Đóng góp cụ thể

- Bộ nhãn Hải trong bang_loi.md; tổng hợp chỉ số, 12 event và rủi ro tại chi_so.md.
- Bảng E1 trong src/lab13.py; hồ sơ launch v0, báo cáo nhóm và báo cáo cá nhân với Codex hỗ trợ.

### Bằng chứng

- bang_loi.md: hai bộ nhãn trùng 20/20 = 100%; không chỉnh bộ nhãn ban đầu.
- E1: 82,83% · 27,12% · 4,25%; hồ sơ đủ 7 mục và đề xuất Go có điều kiện.
- Báo cáo: report/team/2A202603728_NguyenTrungHai.md. Chưa có kết quả duyệt chéo.
