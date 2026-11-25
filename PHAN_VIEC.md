# Phân việc Lab 13 (file tạm, sẽ xóa trước khi nộp)

Hạn nộp: **23:59 hôm nay, 25/11**. Mỗi người tự nộp link repo trên LMS bằng tài khoản của mình; ai không nộp thì không có điểm.

Làm nối tiếp **A → B → C**: người trước push xong và nhắn, người sau `git pull` rồi mới làm.

| | A · Đạt (`datkunal`) | B · Tuấn Anh (`Tanh0406`) | C · Hải (`nguyentrunghai7`) |
| --- | --- | --- | --- |
| Nhiệm vụ | A, B: chi phí và độ nhạy | D: pilot; gắn nhãn bộ 1 | C, E: bảng lỗi, chỉ số, hồ sơ; gắn nhãn bộ 2 |
| Điểm rubric | C1 20 + C2 15 | C4 15 (+ C8 10) | C3 10 + C5 10 (+ C6, C7) |
| File | `src/lab13.py` (CP1, CP2), `bang_chi_phi.md` | `src/lab13.py` (CP4), `pilot_plan.yaml`, `phieu_cham.md` | `bang_loi.md`, `chi_so.md`, `ho_so_launch_v0.md`, `group_report.md` |
| Xong trước | 19:00 | 20:30 | 22:15 |

Các file hồ sơ nằm trong `report/team/`. Nếu coach vẫn duyệt chéo lúc 17:00, xem mục "Làm trước được gì".

## Ai cũng phải làm

- Copy `report/team/MSSV_HoTen.md` thành file riêng (`MSSV_HoTen` không dấu), điền đủ 6 mục. Mục 5 ghi công cụ AI đã dùng và cách tự kiểm tra.
- Điền dòng của mình và mục cá nhân trong `TEAM.md`.
- Commit bằng tài khoản GitHub của mình. Không force-push, không sửa ngày commit.
- Nộp link repo trên LMS.

## Không được dùng AI để làm thay (RULES.md)

- **Nhãn 20 ca lỗi** (B và C): tự đọc, tự gắn, không trao đổi.
- **Điểm và kết quả duyệt chéo** (cả ba).
- **Số**: phải do `lab13.py` tính ra, hoặc tính tay có ghi cách tính.

## A · Đạt

- [ ] Phần chung trong `TEAM.md`
- [ ] Ba hàm A1, `mo_hinh`, A3, A4, B1–B4 trong `src/lab13.py`
- [ ] `bang_chi_phi.md` đủ A1–A4, B1–B4
- [ ] **Bàn giao khi:** `python lab13.py` chạy hết, in ĐẠT, ra 4.472; `bang_chi_phi.md` không còn `...`

## B · Tuấn Anh

1. [ ] `git pull`, chạy `cd src && python lab13.py` trên máy mình, tính tay một số để kiểm lại phần A.
2. [ ] Gắn nhãn 20 ca (trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`). **Chưa push, gửi riêng cho Đạt giữ.**
3. [ ] Dòng `TODO CP4` trong `lab13.py`: tính 5 câu D1 (a–e).
4. [ ] `pilot_plan.yaml`: ghi D1, D2 vào chú thích đầu file, điền mọi dấu `?`.
5. [ ] Ít nhất 3 luật dừng (an toàn, chi phí, mức sử dụng), đủ bốn vế NẾU – TRONG – THÌ (ai làm) – KHÔNG THÌ.
6. [ ] Sau duyệt chéo: điền `phieu_cham.md` theo điểm cả ba đã thống nhất.

Cần để ý:
- Không cách chia theo cụm nào đủ mẫu cho mức chênh 5 điểm. Chọn mức 6 điểm thì phải ghi rõ đánh đổi.
- Bước 50% cần 299 yêu cầu mỗi nhân viên, trong phạm vi mỗi người chỉ khoảng 31 yêu cầu/ngày, tức **khoảng 10 ngày**, cộng 7 ngày chờ xem có mở lại không. "Mỗi bước một tuần" không đủ.
- Tỉ lệ mở lại hiện tại là 4,25%. Đặt ngưỡng dừng 1–3% thì pilot dừng ngay tuần đầu. Slide chữa yêu cầu thêm xem lại 100% ở bước 10%, rồi giảm dần.

**Bàn giao khi:** hai lệnh sau (chạy trong `src/`) ổn, và đã push:

```bash
python -c "import yaml; yaml.safe_load(open('../report/team/pilot_plan.yaml', encoding='utf-8'))"
grep -v '^ *#' ../report/team/pilot_plan.yaml | grep -n '?'     # không in gì
```

## C · Hải

1. [ ] `git pull`, gắn nhãn 20 ca của mình **trước khi** nhận nhãn của Tuấn Anh từ Đạt.
2. [ ] `bang_loi.md`: hai bộ nhãn, tỉ lệ đồng thuận (cần từ 16/20), quy tắc cho ca lệch, bảng khắc phục 5 ca. Mỗi dòng có cách phát hiện đo được và một vai trò phụ trách.
3. [ ] `chi_so.md`: tính thử 3 chỉ số, đề xuất thêm 1 chỉ số dùng và 1 chỉ số an toàn, từ 6 event có `trace_id`, kiểm tra chéo, từ 2 dòng rủi ro lấy số từ `bang_chi_phi.md`.
4. [ ] `ho_so_launch_v0.md`: đủ 7 mục, cột trạng thái đúng ba giá trị, dòng cuối là Go / Go có điều kiện / No-go.
5. [ ] `group_report.md`: ghi rõ nhóm chỉ có 3 người ở mục 5, và kết quả duyệt chéo thật ở mục 4.

Cần để ý:
- Viết "chỉ số trong đợt chạy thử là 82,83%", không viết "trợ lý đã nâng chỉ số".
- Nêu cả con số bất lợi (xem lại 100%, power ở mức 5 điểm) kèm cách xử lý, để được 10 điểm tiêu chí C6.

**Xong khi:** hết checklist trong `SUBMISSION.md`; `grep -rni production report/team` không in gì.

## Gắn nhãn độc lập khi làm nối tiếp

Tuấn Anh gắn xong gửi riêng cho Đạt (Đạt không gắn nhãn). Hải gắn xong mới lấy nhãn của Tuấn Anh ra so. Đã so rồi thì không sửa bộ nhãn. **Cả hai không xem trước** mục "Nhiệm vụ C" trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` và slide 71 vì có đáp án.

## Duyệt chéo Gate 2a (cả ba)

Hải trình bày 1 phút, Đạt trả lời về chi phí, Tuấn Anh trả lời về pilot. Phiếu chấm nhóm khác cả ba cùng chấm.

## Làm trước được gì khi chưa đến lượt

- Tuấn Anh: gắn nhãn, tính D1 (không cần số của A).
- Hải: gắn nhãn, viết danh sách event, đề xuất chỉ số.
