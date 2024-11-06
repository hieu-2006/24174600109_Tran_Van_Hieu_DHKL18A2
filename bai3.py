# Nhập kích thước của vector
n = int(input("Nhập kích thước của vector a và b: "))

# Nhập các vector a và b
vector_a = nhap_vector(n)
vector_b = nhap_vector(n)

# Tính tích vô hướng
result = tich_vo_huong(vector_a, vector_b)

# In kết quả
print(f"Tích vô hướng của 2 vector a và b là: {result}")
