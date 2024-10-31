# Nhập tọa độ các đỉnh
A, B, C = nhap_tam_giac()

# Tính trọng tâm
trong_tam = tinh_trong_tam(A, B, C)

# In kết quả
print(f"Tọa độ trọng tâm của tam giác là: ({trong_tam[0]}, {trong_tam[1]})")
