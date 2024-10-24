import math

def thoi_gian_dung(a):
    # Tính hằng số log4(5)
    log4_5 = math.log(5, 4)

    # Tính thời gian dừng t
    # Giải phương trình: 0 = -t * log4(5) + a^4
    # => t = a^4 / log4(5)
    t = a**4 / log4_5

    return round(t, 2)

# Nhập vận tốc a từ người dùng
a = float(input("Nhập vận tốc của xe ô tô (m/s): "))
result = thoi_gian_dung(a)

# In kết quả
print(f"Thời gian ô tô đi được cho đến lúc dừng là: {result} giây")



#