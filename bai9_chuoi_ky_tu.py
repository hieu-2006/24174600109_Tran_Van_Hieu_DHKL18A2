bin_str = input("Nhap vao chuoi nhi phan: ")
if all(c in '01' for c in bin_str):
    decimal_value = int(bin_str, 2)
    print(f"'{bin_str}' la so nhi phan, chuyen sang thap phan: {decimal_value}")
else:
    print(f"'{bin_str}' khong phai la so nhi phan")
