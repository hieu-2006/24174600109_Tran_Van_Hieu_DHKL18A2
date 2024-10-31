a = float(input("Nhập số thứ nhất: "))
b = float(input("Nhập số thứ hai: "))
c = float(input("Nhập số thứ ba: "))
max_so = a  # Giả sử a là số lớn nhất
if b > max_so:
    max_so = b
if c > max_so:
    max_so = c
print(f"Số lớn nhất trong 3 số là: {max_so}")
