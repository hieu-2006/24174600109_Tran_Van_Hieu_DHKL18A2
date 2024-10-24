def nhap_tam_giac():
    A = list(map(float, input("Nhập tọa độ điểm A (x, y): ").split(',')))
    B = list(map(float, input("Nhập tọa độ điểm B (x, y): ").split(',')))
    C = list(map(float, input("Nhập tọa độ điểm C (x, y): ").split(',')))
    return A, B, C

def tinh_trong_tam(A, B, C):
    x_trong_tam = (A[0] + B[0] + C[0]) / 3
    y_trong_tam = (A[1] + B[1] + C[1]) / 3
    return (round(x_trong_tam, 2), round(y_trong_tam, 2))

# Nhập tọa độ các đỉnh
A, B, C = nhap_tam_giac()

# Tính trọng tâm
trong_tam = tinh_trong_tam(A, B, C)

# In kết quả
print(f"Tọa độ trọng tâm của tam giác là: ({trong_tam[0]}, {trong_tam[1]})")
