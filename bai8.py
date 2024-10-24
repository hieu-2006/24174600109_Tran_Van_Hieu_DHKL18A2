import math

def f(x):
    if x <= 0:
        return "Giá trị của x phải lớn hơn 0."
    if x == 1:
        return "Biểu thức không xác định vì log(1) bằng 0."

    log4_x = math.log(x, 4)  # log4(x)
    logx_2 = math.log(2, x)   # log_x(2)
    return log4_x + logx_2

# Nhập giá trị x từ người dùng
x = float(input("Nhập giá trị của x (x > 0): "))
result = f(x)

# In kết quả đã làm tròn đến 2 chữ số thập phân
if isinstance(result, str):
    print(result)
else:
    print(f"Giá trị của f(x) là: {result:.2f}")



import math
x = input("Nhap gia tri x: ")
x = float(x)
f_x = math.log(x,4) + math.log(2,x)
print(f"Gia tri can tim f(x) = {f_x:.2f}")
