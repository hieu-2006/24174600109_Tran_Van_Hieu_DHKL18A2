n = int(input("Nhap so nguyen duong n: "))
A = [i for i in range(n) if i % 2 != 0]
B = [i for i in range(n) if i % 2 == 0]
A.sort(reverse=True)
B.sort(reverse=True)
print("Danh sach A (so le):", A)
print("Danh sach B (so chan):", B)
