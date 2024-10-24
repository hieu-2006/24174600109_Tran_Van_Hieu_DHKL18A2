def tinh_tien_dien(thoi_gian):
    # Các thông số
    hieu_dien_the = 220  # V
    cuong_do_dong = 2.7  # A
    gia_dien = 7000  # đồng/kWh

    # Tính công suất (P = U * I)
    cong_suat = hieu_dien_the * cuong_do_dong  # W

    # Chuyển đổi công suất sang kW
    cong_suat_kw = cong_suat / 1000  # kW

    # Tính số giờ sử dụng
    thoi_gian_gio = thoi_gian / 3600  # chuyển giây sang giờ

    # Tính tiền điện
    tien_dien = cong_suat_kw * thoi_gian_gio * gia_dien  # đồng

    return tien_dien

# Nhập thời gian sử dụng bóng đèn
thoi_gian = float(input("Nhập thời gian sử dụng bóng đèn (giây): "))
tien = tinh_tien_dien(thoi_gian)

# In kết quả
print(f"Tiền điện phải trả là: {tien:.2f} đồng")



#bai4
# U = 220
I = 2.7
# P = U*I*(3600*1000)
# tien_phai_tra = P * 7000

t = float(input("Nhap thoi gian su dung bong den (s): "))
U = 220
I = 2.7
P = (t*U*I)/(3600*1000)
tien_phai_tra = P * 7000
print("So tien phai tra la: ")