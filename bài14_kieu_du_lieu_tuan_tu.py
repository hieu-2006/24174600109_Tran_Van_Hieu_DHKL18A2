n = int(input("Nhap so luong sinh vien: "))

sinh_vien = []

for i in range(n):
    print(f"Nhap thong tin cho sinh vien {i + 1}:")
    ten = input("Ten sinh vien: ")
    diem = float(input("Diem tong ket: "))
    sinh_vien.append({"Ten": ten, "Diem tong ket": diem})

print("\nDanh sach sinh vien hien tai:")
for sv in sinh_vien:
    print(f"Ten: {sv['Ten']}, Diem tong ket: {sv['Diem tong ket']}")

ten_sua = input("\nNhap ten sinh vien can sua thong tin: ")

sinh_vien_tim_thay = False
for sv in sinh_vien:
    if sv['Ten'] == ten_sua:
        sinh_vien_tim_thay = True
        diem_moi = float(input(f"Nhap diem moi cho sinh vien {ten_sua}: "))
        sv['Diem tong ket'] = diem_moi
        print(f"Da cap nhap diem cho sinh vien {ten_sua}")
        break

if not sinh_vien_tim_thay:
    print(f"Sinh vien co ten {ten_sua} khong ton tai")

print("\nDanh sach sinh vien sau khi sua:")
for sv in sinh_vien:
    print(f"Ten: {sv['Ten']}, diem tong ket: {sv['Diem tong ket']}")