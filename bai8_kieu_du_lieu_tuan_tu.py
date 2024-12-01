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

i = int(input("Nhap chi so cot i (1 <= i <= n): ")) - 1
j = int(input("Nhap chi so cot j (1 <= j <= n): ")) - 1


for row in A:
    row[i], row[j] = row[j], row[i]

print("Ma tran sau khi đao vi tri hai cot i va j la: ")
for row in A:
    print(" ".join(map(str, row)))
