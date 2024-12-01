n = int(input("Nhap so luong sinh vien: "))

sinh_vien = []
for i in range(n):
    print(f"Nhap thong tin cho sinh vien {i + 1}:")
    ten = input("Ten sinh vien: ")
    diem = float(input("Diem tong ket: "))
    sinh_vien.append({"Ten": ten, "Diem tong ket": diem})

ten_moi = input("\nNhap ten sinh vien can them: ")
diem_moi = float(input("Nhap điem tong ket caa sinh vien: "))

sinh_vien_ton_tai = False
for sv in sinh_vien:
    if sv['Ten'] == ten_moi:
        sinh_vien_ton_tai = True
        break

if sinh_vien_ton_tai:
    print("Thong tin sinh vien da ton tai")
else:
    sinh_vien.append({"Ten": ten_moi, "Diem tong ket": diem_moi})
    print("Da them sinh vien")

print("\nDanh sach sinh vien hien tai:")
for sv in sinh_vien:
    print(f"Ten: {sv['Ten']}, Diem tong ket: {sv['Diem tong ket']}")
