loai_xe = int(input("Nhập loại xe (4 hoặc 7 chỗ): "))
km = float(input("Nhập quãng đường di chuyển (km): "))
thoi_gian_cho = float(input("Nhập thời gian chờ (phút): "))
cuoc_phi = 0

if loai_xe == 4:
    cuoc_phi = 11000 / 0.8  
    if km <= 0.8:
        cuoc_phi += 0  
    elif km <= 20:
        cuoc_phi += (km - 0.8) * 12100
    else:
        cuoc_phi += (20 - 0.8) * 12100 + (km - 20) * 10000
elif loai_xe == 7:
    cuoc_phi = 13000 / 0.8  
    if km <= 0.8:
        cuoc_phi += 0  
    elif km <= 30:
        cuoc_phi += (km - 0.8) * 14100
    else:
        cuoc_phi += (30 - 0.8) * 14100 + (km - 30) * 12000
else:
    print("Loại xe không hợp lệ. Vui lòng nhập 4 hoặc 7.")
    exit()
if thoi_gian_cho > 5:
    thoi_gian_chiu_phi = thoi_gian_cho - 5
    cuoc_phi += thoi_gian_chiu_phi * 800
print(f"Cước taxi phải trả: {cuoc_phi:.0f} đồng")
