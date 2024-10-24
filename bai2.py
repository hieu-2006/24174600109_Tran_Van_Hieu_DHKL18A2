import math
#Nhập giá trị x
x = input("Nhap gia tri x: ")
x = float(x)
#Kiểm tra điều kiện 
if x > 0:
    f_x = math.log(4, x) + math.log(2, x)
    print(f"Gia tri can tim f(x) = {f_x:.2f}")
else:
    print("Gia tri x phai lon hon 0")