import math
x = input("Nhap gia tri x: ")
x = float(x)
if x > 0:
    f_x = math.log(x, 4) + math.log(x, 2)
    print(f"Gia tri cua f(x) = {f_x:.2f}")
else:
    print("Gia tri x phai lon hon 0 ")    