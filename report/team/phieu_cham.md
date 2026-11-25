# Phiếu chấm hội đồng Gate 2a

**Trạng thái: Đã duyệt chéo ngày 25/11/2026.** Điểm và quyết định do nhóm chốt; lý do do AI (Claude Code) soạn từ hồ sơ của nhóm được chấm. Câu trả lời của đội trình ghi theo lời họ.

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm (hội đồng): DatTanhHai · L3B
- Nhóm được chấm: Nhom4Nguoi · L3B

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | 10 | Nêu xem lại 100% là 12.414,79 đ, vượt 12.000 đ [simulated], và power 0,6417 nếu tác động thật 5 điểm; `chi_so.md` có hướng giảm xem lại theo bậc. Góp ý: hồ sơ chưa cộng chi phí cố định vào con số xem lại 100% |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | 10 | Nhãn simulated trong `bang_chi_phi.md` và hồ sơ; loại quoc_te 1,876× và doi_tac 0,851× [simulated]. Góp ý: ghi hai số này và nhãn ngay trong hồ sơ, `group_report.md` |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | 10 | 20 + 20 nhân viên bốc thăm, 859 hiệu dụng mỗi nhóm, ít nhất 299 yêu cầu mỗi người, 5 luật dừng. Góp ý: thiếu tỉ lệ xem lại ở bước 10%, và lịch mở 25% ngày 07/12 chưa khớp luật cần 100 yêu cầu đủ 7 ngày mỗi nhóm |
| **Tổng** | | | | **30 / 30** | |

**Quyết định của hội đồng:** Go có điều kiện

**Lý do:** Thiết kế 20 + 20 nhân viên, 859 hiệu dụng mỗi nhóm, nêu rõ power 0,6417 nếu tác động thật 5 điểm và xem lại 100% là 12.414,79 đ, vượt 12.000 đ [simulated]. Điều kiện: ghi tỉ lệ xem lại ở bước 10%, sửa lịch mở 25% ngày 07/12 cho khớp luật cần 100 yêu cầu đủ 7 ngày mỗi nhóm, và nêu ngưỡng 8.000 đ áp từ bước nào, trước khi bắt đầu 30/11/2026.

**Một câu hỏi cho đội trình:** Ở bước 10% (30/11–06/12) nhóm xem lại bao nhiêu phần trăm câu trả lời? Nếu 100% thì chi phí là 11.742,79 đ [simulated], vượt ngưỡng dừng 8.000 đ của chính nhóm; nếu ít hơn thì cái gì chặn lỗi tới khách, khi luật mở lại chưa có yêu cầu nào đủ 7 ngày trong tuần đó?

**Câu trả lời của đội trình (ghi lại tại buổi):** Hồ sơ đang thiếu tỉ lệ xem lại ở bước 10%; nhóm sẽ bổ sung duyệt 100% trước khi gửi khách hoặc hoàn tiền. Tuần đầu chấp nhận chi phí cao để kiểm chứng an toàn. Ngưỡng 8.000 đ hiện chỉ kích hoạt sau hai tuần vượt liên tiếp, nhưng nhóm cần bổ sung rõ ngân sách giai đoạn đầu và thời điểm áp dụng ngưỡng. Khi chưa đủ dữ liệu mở lại 7 ngày, nhóm dùng duyệt trước, khóa chống trùng và đối soát sổ cái để chặn lỗi; chưa đủ bằng chứng thì chưa giảm xem lại hoặc tăng rollout.
