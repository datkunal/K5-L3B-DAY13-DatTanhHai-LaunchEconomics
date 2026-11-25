# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py`. Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 (ĐẠT) |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 (ĐẠT) |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 (ĐẠT) |

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 | `logix_runs.csv`, mọi lần chạy kể cả lần lỗi | đo từ trace |
| Tool | 84.000 | `logix_runs.csv`, 5.600 lần gọi × 15 đ | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 | attempt lớn hơn 1 (đã nằm trong token và tool) | đo từ trace |
| Xem lại | 1.780.000 | `phut_xem_lai_simulated`, 890 phút × 2.000 đ | simulated |
| Làm lại | 2.264.000 | `phut_lam_lai_simulated`, 1.132 phút × 2.000 đ | simulated |
| Tổng chi phí | 4.373.585 | token + tool + xem lại + làm lại | simulated (92,5% từ cột `_simulated`) |
| Số việc thành công | 978 | `ket_qua` bằng `thanh_cong` | đếm từ dữ liệu |
| Chi phí mỗi việc thành công | 4.472 | 4.373.585 ÷ 978 | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,7 | (245.585 + 84.000) ÷ 1.200 | đo từ trace |

- Chi phí mỗi việc thành công gấp bao nhiêu lần "hoá đơn chia số yêu cầu"? **16,3 lần** (4.472 đ so với 274,7 đ) [simulated].
- Khoản nào chiếm tỉ trọng lớn nhất trong tổng chi phí, bao nhiêu phần trăm? **Làm lại, 51,8%** [simulated]; tiếp theo là xem lại 40,7% [simulated]. Hai khoản này là giờ nhân viên, cộng lại 92,5%; token và tool chỉ 7,5%.
- So công bằng với 12.000 đ phải cộng phần nhân viên làm thay 222 yêu cầu không thành công: (4.373.585 + 222 × 12.000) ÷ 1.200 = **5.865 đ/yêu cầu = 0,49×** [simulated], không phải 4.472 ÷ 12.000 = 0,37×.

## A3 · Tách theo loại yêu cầu

Hai cột chi phí bên phải: simulated.

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công [simulated] | So với 12.000 đ [simulated] |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% (783) | 1,11 | 2.696 đ | 0,22× |
| hang_nang | 158 | 74,1% (117) | 1,47 | 8.221 đ | 0,69× |
| quoc_te | 150 | 27,3% (41) | 2,32 | 22.515 đ | 1,88× |
| doi_tac | 68 | 54,4% (37) | 1,88 | 10.215 đ | 0,85× |

Tỉ lệ lần chạy `ok` theo lần thử (đo từ trace), để biết chạy lại có giúp không:

| Loại | Lần 1 | Lần 2 | Lần 3 |
| --- | ---: | ---: | ---: |
| noi_dia | 91,0% (750/824) | 75,7% (56/74) | 38,9% (7/18) |
| hang_nang | 70,9% (112/158) | 39,1% (18/46) | 17,9% (5/28) |
| quoc_te | 30,0% (45/150) | 11,4% (12/105) | 2,2% (2/93) |
| doi_tac | 51,5% (35/68) | 18,2% (6/33) | 14,8% (4/27) |

- Loại nào không đáng để trợ lý xử lý? Với loại đó, cho chạy lại tới 3 lần có giúp không? **quoc_te**: 22.515 đ = 1,88× [simulated], chạy 2,32 lần mỗi yêu cầu mà chỉ 27,3% thành công.
  Chạy lại không giúp: lần 1 ok 30,0%, lần 2 11,4%, lần 3 2,2%. Từ tối đa 2 lên 3 lần, việc thành công vẫn là 41/150 nhưng chi phí tăng từ 20.605 lên 22.515 đ [simulated].
- Phạm vi pilot: **noi_dia + hang_nang**. Loại thêm `doi_tac` vì sát ngưỡng (0,85×; tính cả nhân viên làm thay là 11.029 đ/yêu cầu = 0,92×) [simulated], mẫu chỉ 68 yêu cầu và có điều khoản riêng.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

Trong phạm vi: 982 yêu cầu, 900 thành công, 3.072.513 ÷ 900 = 3.414 đ mỗi việc thành công [simulated]. Việc thành công mỗi tháng = 45.000 × 900 ÷ 1.200. Các cột chi phí: simulated.

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định [simulated] | So với 12.000 đ [simulated] |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | 4.599 đ | 0,38× |
| Một nửa khối lượng | 16.875 | 2.370 đ | 5.784 đ | 0,48× |

- Chi phí cố định có đổi kết luận không? Ở khối lượng nào? Không đổi ở 45.000 yêu cầu/tháng (0,38×) và ở một nửa (0,48×) [simulated].
  Chỉ đổi khi còn dưới khoảng **6.212 yêu cầu/tháng** (13,8% của 45.000): 40.000.000 ÷ (12.000 − 3.414) ÷ (900 ÷ 1.200) [simulated].
- Cộng cả phần nhân viên làm thay 82 yêu cầu không thành công: 5.217 đ/yêu cầu = 0,43× ở quy mô đầy đủ, 6.303 đ = 0,53× ở một nửa khối lượng [simulated].

## B1 · Đổi từng yếu tố

Gốc (A2): 4.472 đ [simulated]. Cột chi phí và thay đổi: simulated.

| Kịch bản | Cách tính | Chi phí mỗi việc thành công [simulated] | Thay đổi (%) [simulated] |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4.723 đ | +5,6% |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346 đ | −2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 đ | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 đ | −20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 đ | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 đ | −25,9% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 đ | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien | 4.237 đ (966 thành công) | −5,2% |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4.111 đ (881 thành công) | −8,1% |

Tự kiểm tra: mỗi kịch bản "giảm một nửa" giảm đúng bằng nửa mức tăng của "gấp đôi" (`lab13.py` kiểm bằng assert).

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: **6.543 đ, +46,3%** [simulated], đúng bằng 5,6% + 40,7% vì mô hình cộng tuyến tính.
- Xếp hạng ba yếu tố ảnh hưởng mạnh nhất: 1. **Số ca làm lại** (+51,8%) · 2. **Tỉ lệ xem lại** (+40,7%) · 3. **Lương nhân viên** (+23,1%) [simulated]. Giá token chỉ +5,6%.

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

Chi phí cả hệ thống = tổng chi phí trợ lý + 12.000 đ × số yêu cầu không thành công. Các cột chi phí: simulated.

| Giới hạn | Tổng chi phí trợ lý [simulated] | Số yêu cầu không thành công | Chi phí cả hệ thống [simulated] | Chi phí mỗi việc thành công [simulated] |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ | 319 | 7.449.781 đ | **4.111 đ** (thấp nhất) |
| 2 lần | 4.093.220 đ | 234 | **6.901.220 đ** (rẻ nhất) | 4.237 đ |
| 3 lần | 4.373.585 đ | 222 | 7.037.585 đ | 4.472 đ |

- Giới hạn nào rẻ nhất cho công ty? Có trùng với giới hạn cho chi phí mỗi việc thành công thấp nhất không? **2 lần** rẻ nhất cho công ty (6.901.220 đ) [simulated].
  Không trùng: 1 lần có chi phí mỗi việc thành công thấp nhất (4.111 đ) nhưng đẩy thêm 85 yêu cầu sang nhân viên so với 2 lần, nên cả hệ thống đắt hơn 548.561 đ [simulated].

## B4 · Nếu phải xem lại tất cả

| Phút làm lại mỗi ca | Xem lại: 948 × 5 phút × 2.000 đ | Làm lại: 48 ca × phút × 2.000 đ | Token + tool | Tổng ÷ 900 việc thành công [simulated] | So với 12.000 đ [simulated] | Cộng cố định 1.185 đ/việc [simulated] |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 9 phút (đề bài cho) | 9.480.000 đ | 864.000 đ | 224.513 đ | **11.743 đ** | **0,98×** | 12.928 đ (1,08×) |
| 15,3 phút (trung bình trong dữ liệu, simulated) | 9.480.000 đ | 1.468.800 đ | 224.513 đ | **12.415 đ** | **1,03×** | 13.600 đ (1,13×) |

- Chi phí mỗi việc thành công khi xem lại 100% (`noi_dia` + `hang_nang`), so với 12.000 đ: **11.743 đ = 0,98×** [simulated], gần như không tiết kiệm.
  Với 15,3 phút làm lại như dữ liệu thì **12.415 đ = 1,03×**; cộng chi phí cố định thì cả hai trường hợp đều đắt hơn nhân viên tự làm (1,08× và 1,13×) [simulated].
- Kết quả này nói gì về thứ pilot cần học được? Tiền xem lại chiếm 90% chi phí [simulated], nên pilot phải tìm **tỉ lệ xem lại thấp nhất vẫn an toàn** và đo số phút xem lại thật.
  Nếu vẫn xem lại 100%, mỗi lần phải ≤ 5,1 phút (làm lại 9 phút) hoặc ≤ 4,8 phút (làm lại 15,3 phút) mới hoà vốn, chưa tính cố định [simulated].
