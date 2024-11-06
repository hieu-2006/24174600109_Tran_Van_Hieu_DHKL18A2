n = int(input("Nhap 1 so: "))
print(f"Cac thua so nguyen to cua {n} la: ")
for i in range(2,n+1):
    while n%i == 0:
        print(i)
        n = n // i