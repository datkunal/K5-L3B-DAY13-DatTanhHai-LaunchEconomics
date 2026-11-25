# Báo cáo cá nhân — TranTuanAnh-2A202603909

## 1. Thông tin thành viên

- Họ tên: Trần Tuấn Anh
- MSSV: 2A202603909
- Email:
- Vai trong nhóm: người kiểm số, viết code D1, người gắn nhãn 1 (nhóm 3 người)

## 2. Phần việc phụ trách

Nhiệm vụ D (kế hoạch pilot), kiểm lại số phần A, gắn nhãn bộ 1 cho 20 ca lỗi, điền phiếu chấm sau duyệt chéo.

## 3. Đóng góp cụ thể

- `src/lab13.py`: các hàm `co_mau`, `he_so_thiet_ke`, `co_mau_hieu_dung`, `m_toi_thieu`, `power_khi`, `icc_anova`, `chi_phi_theo_xem_lai`; bảng D1 và D3.
- `report/team/pilot_plan.yaml`: D1, D2, đánh đổi, và toàn bộ các trường.

Bốn ý chính từ phần việc:

- **Vì sao số cụm quyết định, không phải tổng số yêu cầu:** hiệu dụng = c × m ÷ (1 + (m − 1) × ICC), khi m rất lớn chỉ tiến tới c ÷ ICC. 20 nhân viên mỗi nhóm tối đa 20 ÷ 0,02 = 1.000, dưới 1.251, nên chạy thêm bao lâu cũng không thấy được mức chênh 5 điểm.
- **Vì sao vẫn chọn chia theo nhân viên:** chia theo yêu cầu đủ 1.251 nhưng một người vừa dùng vừa không dùng trợ lý, đối chứng không còn sạch. Đánh đổi là chỉ bảo đảm thấy mức 6 điểm; ở 5 điểm power chỉ 0,64.
- **Vì sao bước 0.50 dài 14 ngày:** trong phạm vi mỗi người có 30,7 yêu cầu/ngày, 299 yêu cầu cần 9,7 ngày; một tuần chỉ được 215.
- **Vì sao ngưỡng mở lại là +2 điểm và trần 6%:** hiện tại đã 4,25% (phạm vi 3,97%), đặt 1–3% thì dừng ngay tuần đầu. Cả 39 ca mở lại trong phạm vi đều không được xem lại, nên bước 0.10 xem lại 100% rồi mới giảm theo bậc.

## 4. Bằng chứng

- `cd src && python lab13.py`: in D1 (1.251 · 3.103 và 42 người · 1.000 · 300 · 299) và bảng D3.
- `pilot_plan.yaml` đọc được bằng `yaml.safe_load`, không còn dấu hỏi ngoài chú thích, có 5 luật dừng đủ bốn vế.
- Con số bất lợi đã nêu: bước 0.10 xem lại 100% và cộng chi phí cố định là 24.267 đ = 2,02× [simulated]; `hang_nang` xem lại 100% là 16.638 đ = 1,39× [simulated]; ICC từ 0,0233 thì không đủ mẫu cho 6 điểm.
- Commit của `Tanh0406` trên `src/lab13.py`, `report/team/pilot_plan.yaml`, `TEAM.md`.

## 5. Công cụ AI đã dùng

- **Công cụ:** Claude Code (Claude Opus 5.5).
- **Dùng vào việc gì:** đọc và tóm tắt đề, viết code CP4 trong `lab13.py`, soạn `pilot_plan.yaml`, mục cá nhân trong `TEAM.md` và bản nháp báo cáo này.
- **Kiểm tra kết quả:** phần A của Đạt được tính lại bằng một đoạn code riêng không dùng `lab13.py` (A2, A3, B3 và ba chỉ số), ra cùng số. D1 đối chiếu với statsmodels (1.249,6 so với 1.251) và đáp án slide 73.
- Phép tính tay để đối chiếu: 1.251 × 2,48 = 3.102,48 → 3.103; 3.103 ÷ 75 = 41,4 → 42 người; câu e: m ≥ 859 × 0,98 ÷ (20 − 859 × 0,02) = 841,82 ÷ 2,82 = 298,5 → 299; 1.500 × 982/1.200 ÷ 40 = 30,7 yêu cầu/ngày.
- AI không gắn nhãn ca nào trong 20 ca lỗi và không chấm duyệt chéo.

## 6. Tự đánh giá

- **Làm được:** năm câu D1 khớp đáp án; kế hoạch có đối chứng cùng lúc, 20 cụm mỗi nhóm, 5 luật dừng có ngưỡng, thời hạn và người có quyền dừng; nêu rõ đánh đổi và con số bất lợi.
- **Hạn chế:** không đủ mẫu cho mức 5 điểm. Baseline 0,70 là của mọi loại yêu cầu, chưa có số đối chứng riêng cho phạm vi. Chi phí theo bậc xem lại dựa trên phút simulated và coi tỉ lệ sai như đợt chạy thử. Ngưỡng 70% và 2% là giả định của nhóm, chưa có dữ liệu.
