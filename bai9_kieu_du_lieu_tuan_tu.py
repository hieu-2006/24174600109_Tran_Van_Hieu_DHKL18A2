m = int(input("Nhap so dong cua ma tran A va B: "))
n = int(input("Nhap so cot cua ma tran A va B: "))
A = []
B = []
print("Nhap ma tran A: ")
for i in range(m):
    row = []
    for j in range(n):
        element = int(input(f"A[{i+1}][{j+1}]: "))
        row.append(element)
    A.append(row)

print("Nhap ma tran B: ")
for i in range(m):
    row = []
    for j in range(n):
        element = int(input(f"B[{i+1}][{j+1}]: "))
        row.append(element)
    B.append(row)

# Tổng hai ma trận A + B
C = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(A[i][j] + B[i][j])
    C.append(row)

print("\nTong hai ma tran A va B la: ")
for row in C:
    print(" ".join(map(str, row)))

# Hiệu hai ma trận A - B
C = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(A[i][j] - B[i][j])
    C.append(row)

print("\nHieu hai ma tran A va B la: ")
for row in C:
    print(" ".join(map(str, row)))

# Tích ma trận A với số k
k = int(input("\nNhap so k đe nhan voi ma tran A: "))
C = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(A[i][j] * k)
    C.append(row)

print(f"\nTich cua ma tran A voi so {k} la: ")
for row in C:
    print(" ".join(map(str, row)))

# Tích của hai ma trận A và B
if len(A[0]) == len(B):
    C = []
    for i in range(m):
        row = []
        for j in range(n):
            sum = 0
            for k in range(len(B)):
                sum = sum + A[i][k] * B[k][j]
            row.append(sum)
        C.append(row)
    print("\nTich hai ma tran A va B la: ")
    for row in C:
        print(" ".join(map(str, row)))
else:
    print("\nKhong the nhan hai ma tran nay")

# Ma trận đối xứng của A 
if m == n:
    C = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(A[j][i])
        C.append(row)
    print("\nMa tran đoi xung cua A la: ")
    for row in C:
        print(" ".join(map(str, row)))
else:
    print("\nMa tran A khong phai la ma tran vuong, khong the tinh ma tran đoi xung")