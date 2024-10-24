def nhap_vector(n):
    vector = []
    print(f"Nhập vào {n} phần tử của vector:")
    for i in range(n):
        gia_tri = float(input(f"Phần tử {i + 1}: "))
        vector.append(gia_tri)
    return vector

def tich_vo_huong(a, b):
    return sum(x * y for x, y in zip(a, b))

# Nhập kích thước của vector
n = int(input("Nhập kích thước của vector a và b: "))

# Nhập các vector a và b
vector_a = nhap_vector(n)
vector_b = nhap_vector(n)

# Tính tích vô hướng
result = tich_vo_huong(vector_a, vector_b)

# In kết quả
print(f"Tích vô hướng của 2 vector a và b là: {result}")
