m = int(input("Nhap so dong (m): "))
n = int(input("Nhap so cot (n): "))
A = []
print("Nhap cac phan tu cua ma tran A: ")
for i in range(m):
    row = []
    for j in range(n):
        element = int(input(f"A[{i+1}][{j+1}]: "))
        row.append(element)
    A.append(row)

print("Ma tran A vua nhap la: ")
for row in A:
    print(" ".join(map(str, row)))