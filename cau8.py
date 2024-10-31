diem_chuyen_can = float(input("Nhập điểm chuyên cần: "))
diem_giua_ky = float(input("Nhập điểm giữa kỳ: "))
diem_cuoi_ky = float(input("Nhập điểm cuối kỳ: "))

if diem_chuyen_can < 0 or diem_chuyen_can > 10 or diem_giua_ky < 0 or diem_giua_ky > 10 or diem_cuoi_ky < 0 or diem_cuoi_ky > 10:
    print("Điểm phải nằm trong khoảng từ 0 đến 10.")
else:
    diem_trung_binh = (diem_chuyen_can + diem_giua_ky + diem_cuoi_ky) / 3
    if diem_trung_binh >= 9:
        loai = 'A'
    elif diem_trung_binh >= 7:
        loai = 'B'
    elif diem_trung_binh >= 5:
        loai = 'C'
    else:
        loai = 'D'
    print(f"Điểm trung bình: {diem_trung_binh:.2f}")
    print(f"Xếp loại: {loai}")
