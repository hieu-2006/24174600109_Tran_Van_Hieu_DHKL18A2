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

ten_xoa = input("\nNhap ten sinh vien can xoa: ")

sinh_vien = [sv for sv in sinh_vien if sv['Ten'] != ten_xoa]
print("\nDanh sach sinh vien sau khi xoa:")
for sv in sinh_vien:
    print(f"Ten: {sv['Ten']}, Diem tong ket: {sv['Diem tong ket']}")
