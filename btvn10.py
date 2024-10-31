luong = float(input("Nhập lương của nhân viên (đồng): "))
thue = 0
luong_rong = 0
if luong > 15000000:
    thue = luong * 0.30  
elif luong >= 7000000:
    thue = luong * 0.20  
else:
    thue = luong * 0.10  
luong_rong = luong - thue
print(f"Lương trước thuế: {luong:.2f} đồng")
print(f"Thuế thu nhập: {thue:.2f} đồng")
print(f"Lương ròng (lương thực nhận): {luong_rong:.2f} đồng")
