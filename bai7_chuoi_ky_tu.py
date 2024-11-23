chuoi = input("Nhap vao mot chuoi ky tu: ")
if '.' in chuoi:
    parts = chuoi.split('.')
    if len(parts) == 2 and parts[0].replace('-', '').isdigit() and parts[1].isdigit():
        print(f"'{chuoi}' la so thap phan.")
    else:
        print(f"'{chuoi}' khong phai la so thap phan.")
else:
    print(f"'{chuoi}' khong phai la so thap phan.")
