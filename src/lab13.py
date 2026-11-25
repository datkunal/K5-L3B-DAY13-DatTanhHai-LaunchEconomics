"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
Cách chia hàm mo_hinh và các kịch bản B1 dựa theo docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md.
"""
import math
import sys
from pathlib import Path

import pandas as pd

if hasattr(sys.stdout, 'reconfigure'):      # cửa sổ lệnh Windows mặc định có thể không in được tiếng Việt
    sys.stdout.reconfigure(encoding='utf-8')

THU_MUC = Path(__file__).resolve().parent

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)
CO_DINH_THANG = 40_000_000      # đồng mỗi tháng: vận hành, giám sát, cập nhật chính sách
YEU_CAU_THANG = 45_000          # yêu cầu hoàn phí mỗi tháng của LogiX-VN
LOAI = ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']
PHAM_VI = ['noi_dia', 'hang_nang']      # phạm vi đề xuất cho pilot, lý do ở bảng A3
PHUT_XEM_LAI_B4 = 5             # phút xem lại mỗi yêu cầu chạy ok (đề bài B4)
PHUT_LAM_LAI_B4 = 9             # phút làm lại mỗi ca sai (đề bài B4)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    if k is None:
        return 1 / p
    return (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    if k is None:
        return 1.0
    return 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
def mo_hinh(runs, reqs, gia_vao=GIA_VAO, gia_ra=GIA_RA, gia_tool=GIA_TOOL, luong_phut=LUONG_PHUT,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    - chay_lai: phần token + tool của lần chạy thứ 2 và 3, đã nằm trong token và tool nên không cộng lại vào tong.
    - he_thong: tong + 12.000 đ cho mỗi yêu cầu không thành công, vì nhân viên phải làm thay (B3).
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])]    # để gọi được trên một phần của reqs (A3, A4, B4)
    if max_lan_chay is not None:
        runs = runs[runs['attempt'] <= max_lan_chay]
        bi_cat = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[bi_cat, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[bi_cat, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    token, tool = tien_token.sum(), tien_tool.sum()
    chay_lai = (tien_token + tien_tool)[runs['attempt'] > 1].sum()
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = token + tool + xem_lai + lam_lai

    so_yeu_cau = len(reqs)
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())
    he_thong = tong + BASELINE * (so_yeu_cau - thanh_cong)
    return dict(token=token, tool=tool, chay_lai=chay_lai, xem_lai=xem_lai, lam_lai=lam_lai, tong=tong,
                so_yeu_cau=so_yeu_cau, so_lan_chay=len(runs), thanh_cong=thanh_cong,
                cps=tong / thanh_cong, hoa_don_moi_yc=(token + tool) / so_yeu_cau,
                he_thong=he_thong, he_thong_moi_yc=he_thong / so_yeu_cau)


# ---------- In bảng nhiệm vụ A ----------
def tieu_de(ten):
    print(f'\n=== {ten} ===')


def bang_a1():
    tieu_de('A1 · Ba phép thử đáp án biết trước (p = 0,8)')
    print(f'Số lần chạy trung bình, tối đa 2 lần           {so_lan_chay_ky_vong(0.8, 2):.2f}')
    print(f'Số lần chạy trung bình, chạy đến khi đúng      {so_lan_chay_ky_vong(0.8):.2f}')
    print(f'Hệ số chi phí mỗi việc thành công, tối đa 3    {he_so_chi_phi_moi_viec_thanh_cong(0.8, 3):.2f}')
    kiem_tra_dap_an_biet_truoc()


def bang_a2(runs, reqs):
    tieu_de('A2 · Mô hình chi phí từ trace (1.200 yêu cầu)')
    kq = mo_hinh(runs, reqs)
    for ten, khoa, nhan in [
            ('Token (mọi lần chạy)', 'token', 'đo từ trace'),
            ('Tool (mọi lần chạy)', 'tool', 'đo từ trace'),
            ('  trong đó lần chạy thứ 2 và 3', 'chay_lai', 'đo từ trace'),
            ('Xem lại', 'xem_lai', 'simulated'),
            ('Làm lại', 'lam_lai', 'simulated'),
            ('Tổng chi phí', 'tong', 'simulated'),
            ('Số việc thành công', 'thanh_cong', 'đếm từ ket_qua'),
            ('Chi phí mỗi việc thành công', 'cps', 'simulated'),
            ('Hoá đơn token + tool / số yêu cầu', 'hoa_don_moi_yc', 'đo từ trace'),
            ('Cả hệ thống, gồm nhân viên làm thay', 'he_thong', 'simulated'),
            ('Cả hệ thống / yêu cầu', 'he_thong_moi_yc', 'simulated')]:
        print(f'{ten:38s} {kq[khoa]:>14,.1f}  {nhan}')
    print(f"Gấp {kq['cps'] / kq['hoa_don_moi_yc']:.1f} lần hoá đơn chia số yêu cầu [simulated] · "
          f"cả hệ thống {kq['he_thong_moi_yc'] / BASELINE:.2f}x của {BASELINE:,} đ [simulated]")
    print('Tỉ trọng [simulated]: ' + ' · '.join(
        f"{khoa} {kq[khoa] / kq['tong'] * 100:.1f}%" for khoa in ['token', 'tool', 'xem_lai', 'lam_lai']))
    print(f"Phút xem lại {reqs['phut_xem_lai_simulated'].sum():,} [simulated] · "
          f"phút làm lại {reqs['phut_lam_lai_simulated'].sum():,} [simulated] · lần gọi tool {runs['tool_calls'].sum():,}")


def bang_a3(runs, reqs):
    tieu_de('A3 · Tách theo loại yêu cầu (chi phí: simulated)')
    print(f"{'loai':10s} {'yêu cầu':>8s} {'t.công':>7s} {'tỉ lệ':>7s} {'chạy/yc':>8s} {'cps':>8s} {'x12.000':>8s} {'hệ thống/yc':>12s}")
    for loai in LOAI:
        kq = mo_hinh(runs, reqs[reqs['loai'] == loai])
        print(f"{loai:10s} {kq['so_yeu_cau']:8d} {kq['thanh_cong']:7d} {kq['thanh_cong'] / kq['so_yeu_cau'] * 100:6.1f}% "
              f"{kq['so_lan_chay'] / kq['so_yeu_cau']:8.2f} {kq['cps']:8,.0f} {kq['cps'] / BASELINE:7.2f}x "
              f"{kq['he_thong_moi_yc']:12,.0f}")

    print('Tỉ lệ lần chạy ok theo lần thử (đo từ trace):')
    noi = runs.merge(reqs[['request_id', 'loai']], on='request_id')
    noi['ok'] = noi['status'] == 'ok'
    for loai in LOAI:
        dong = []
        for lan in (1, 2, 3):
            ok = noi.loc[(noi['loai'] == loai) & (noi['attempt'] == lan), 'ok']
            dong.append(f'lần {lan}: {ok.mean() * 100:5.1f}% ({ok.sum()}/{len(ok)})')
        print(f'  {loai:10s} ' + ' · '.join(dong))

    print('quoc_te theo giới hạn chạy lại (chi phí: simulated):')
    for k in (1, 2, 3):
        kq = mo_hinh(runs, reqs[reqs['loai'] == 'quoc_te'], max_lan_chay=k)
        print(f"  tối đa {k} lần: thành công {kq['thanh_cong']}/{kq['so_yeu_cau']} · "
              f"token + tool {kq['token'] + kq['tool']:,.0f} đ · cps {kq['cps']:,.0f} đ")


def bang_a4(runs, reqs):
    tieu_de('A4 · Cộng chi phí cố định, phạm vi noi_dia + hang_nang (simulated)')
    kq = mo_hinh(runs, reqs[reqs['loai'].isin(PHAM_VI)])
    viec_moi_yc = kq['thanh_cong'] / len(reqs)              # việc thành công trong phạm vi / yêu cầu toàn công ty
    trong_pham_vi = kq['so_yeu_cau'] / len(reqs)            # phần yêu cầu thuộc phạm vi
    print(f"{kq['so_yeu_cau']} yêu cầu, {kq['thanh_cong']} thành công, tổng {kq['tong']:,.0f} đ, cps {kq['cps']:,.0f} đ, "
          f"cả hệ thống {kq['he_thong_moi_yc']:,.0f} đ/yêu cầu ({kq['he_thong_moi_yc'] / BASELINE:.2f}x)")
    for ten, khoi_luong in [('45.000 yêu cầu/tháng', YEU_CAU_THANG), ('Một nửa khối lượng', YEU_CAU_THANG / 2)]:
        viec = khoi_luong * viec_moi_yc
        co_dinh = CO_DINH_THANG / viec
        day_du = kq['cps'] + co_dinh
        he_thong = kq['he_thong_moi_yc'] + CO_DINH_THANG / (khoi_luong * trong_pham_vi)
        print(f'{ten:21s} việc/tháng {viec:,.0f} · cố định/việc {co_dinh:,.0f} đ · cps + cố định {day_du:,.0f} đ '
              f'({day_du / BASELINE:.2f}x) · cả hệ thống + cố định {he_thong:,.0f} đ/yêu cầu ({he_thong / BASELINE:.2f}x)')
    # Khối lượng mà cps + cố định vừa bằng 12.000 đ (tính theo cả hệ thống mỗi yêu cầu cũng ra đúng số này)
    hoa_von = CO_DINH_THANG / (BASELINE - kq['cps']) / viec_moi_yc
    print(f'Hoà vốn chi phí cố định: {hoa_von:,.0f} yêu cầu/tháng ({hoa_von / YEU_CAU_THANG * 100:.1f}% của 45.000)')


# ---------- Nhiệm vụ B · Độ nhạy ----------
KICH_BAN = {
    'Giá token gấp đôi': dict(gia_vao=GIA_VAO * 2, gia_ra=GIA_RA * 2),
    'Giá token giảm một nửa': dict(gia_vao=GIA_VAO / 2, gia_ra=GIA_RA / 2),
    'Tỉ lệ xem lại gấp đôi': dict(he_so_xem_lai=2),
    'Tỉ lệ xem lại giảm một nửa': dict(he_so_xem_lai=0.5),
    'Số ca làm lại gấp đôi': dict(he_so_lam_lai=2),
    'Số ca làm lại giảm một nửa': dict(he_so_lam_lai=0.5),
    'Lương nhân viên tăng 25%': dict(luong_phut=LUONG_PHUT * 1.25),
    'Chỉ cho chạy tối đa 2 lần': dict(max_lan_chay=2),
    'Chỉ cho chạy 1 lần': dict(max_lan_chay=1),
}


def bang_b1_b2(runs, reqs):
    tieu_de('B1 · Đổi từng yếu tố (simulated)')
    goc = mo_hinh(runs, reqs)['cps']
    print(f"{'Gốc (A2)':28s} {goc:8,.0f}")
    thay_doi = {}
    for ten, tham_so in KICH_BAN.items():
        kq = mo_hinh(runs, reqs, **tham_so)
        thay_doi[ten] = kq['cps'] / goc - 1
        print(f"{ten:28s} {kq['cps']:8,.0f} {thay_doi[ten] * 100:+7.1f}%   thành công {kq['thanh_cong']}")
    for yeu_to in ['Giá token', 'Tỉ lệ xem lại', 'Số ca làm lại']:
        tang, giam = thay_doi[f'{yeu_to} gấp đôi'], thay_doi[f'{yeu_to} giảm một nửa']
        assert abs(giam + tang / 2) < 1e-9, f'{yeu_to}: mức giảm phải bằng nửa mức tăng'
    print('Tự kiểm tra "giảm một nửa" bằng nửa mức tăng của "gấp đôi": ĐẠT')

    tieu_de('B2 · Đổi một cặp và xếp hạng (simulated)')
    cap = mo_hinh(runs, reqs, gia_vao=GIA_VAO * 2, gia_ra=GIA_RA * 2, he_so_xem_lai=2)['cps']
    tong_rieng = thay_doi['Giá token gấp đôi'] + thay_doi['Tỉ lệ xem lại gấp đôi']
    print(f'Giá token gấp đôi + xem lại gấp đôi: {cap:,.0f} đ ({(cap / goc - 1) * 100:+.1f}%), '
          f'tổng hai tác động riêng {tong_rieng * 100:+.1f}%')
    for hang, ten in enumerate(sorted(thay_doi, key=lambda t: -abs(thay_doi[t])), 1):
        print(f'  {hang}. {ten} ({thay_doi[ten] * 100:+.1f}%)')


def bang_b3(runs, reqs):
    tieu_de('B3 · Giới hạn chạy lại, chi phí cả hệ thống (simulated)')
    for k in (1, 2, 3):
        kq = mo_hinh(runs, reqs, max_lan_chay=k)
        print(f"{k} lần: trợ lý {kq['tong']:11,.0f} · không thành công {kq['so_yeu_cau'] - kq['thanh_cong']:4d} · "
              f"cả hệ thống {kq['he_thong']:11,.0f} · cps {kq['cps']:6,.0f}")


def bang_b4(runs, reqs):
    tieu_de('B4 · Xem lại 100%, phạm vi noi_dia + hang_nang (simulated)')
    pham_vi = reqs[reqs['loai'].isin(PHAM_VI)]
    kq = mo_hinh(runs, pham_vi)
    may = kq['token'] + kq['tool']
    co_lan_ok = runs.loc[runs['status'] == 'ok', 'request_id']
    n_ok = int(pham_vi['request_id'].isin(co_lan_ok).sum())
    n_lam_lai = int((pham_vi['ket_qua'] == 'lam_lai').sum())
    phut_tb = reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated'].mean()
    print(f"{len(pham_vi)} yêu cầu · {n_ok} có lần chạy ok · {n_lam_lai} ca làm lại · token + tool {may:,.0f} đ · {kq['thanh_cong']} thành công")
    print(f'Phút làm lại trung bình mỗi ca lam_lai trong dữ liệu: {phut_tb:.1f}')
    for phut in (PHUT_LAM_LAI_B4, round(phut_tb, 1)):
        tien_xem = n_ok * PHUT_XEM_LAI_B4 * LUONG_PHUT
        tien_lam = n_lam_lai * phut * LUONG_PHUT
        tong = tien_xem + tien_lam + may
        hoa_von = (BASELINE * kq['thanh_cong'] - tien_lam - may) / (n_ok * LUONG_PHUT)
        print(f'Làm lại {phut:4.1f} phút/ca: {tien_xem:,.0f} + {tien_lam:,.0f} + {may:,.0f} = {tong:,.0f} đ → '
              f"{tong / kq['thanh_cong']:,.0f} đ ({tong / kq['thanh_cong'] / BASELINE:.2f}x) · "
              f'xem lại chiếm {tien_xem / tong * 100:.0f}% · hoà vốn khi mỗi lần xem lại ≤ {hoa_von:.1f} phút')
        co_dinh = CO_DINH_THANG / (YEU_CAU_THANG * kq['thanh_cong'] / len(reqs))
        day_du = tong / kq['thanh_cong'] + co_dinh
        print(f'    cộng chi phí cố định {co_dinh:,.0f} đ/việc (45.000 yêu cầu/tháng): {day_du:,.0f} đ ({day_du / BASELINE:.2f}x)')


if __name__ == '__main__':
    runs = pd.read_csv(THU_MUC / 'logix_runs.csv')
    reqs = pd.read_csv(THU_MUC / 'logix_requests.csv', keep_default_na=False)
    bang_a1()
    bang_a2(runs, reqs)
    bang_a3(runs, reqs)
    bang_a4(runs, reqs)
    bang_b1_b2(runs, reqs)
    bang_b3(runs, reqs)
    bang_b4(runs, reqs)
    # TODO CP4 · Nhiệm vụ D: cỡ mẫu.
    #   from statsmodels.stats.proportion import proportion_effectsize
    #   from statsmodels.stats.power import NormalIndPower
