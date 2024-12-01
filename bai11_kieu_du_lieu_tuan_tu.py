n = int(input("Nhap so luong sinh vien: "))

sinh_vien = []

for i in range(n):
    print(f"Nhap thong tin cho sinh vien {i + 1}:")
    ten = input("Ten sinh vien: ")
    diem = float(input("Diem tong ket: "))
    sinh_vien.append({"Ten": ten, "Diem tong ket": diem})

print(f"\n{'Ten':<10} {'Diem':>5}")

for sv in sinh_vien:
    print(f"{sv['Ten']:<10} {sv['Diem tong ket']:>5.1f}")
