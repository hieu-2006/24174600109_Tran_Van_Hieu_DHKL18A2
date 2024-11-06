a = int(input("Nhap so a: "))
b = int(input("Nhap so b: "))
snn = min(a,b)
ucln = 1
for i in range(1,snn+1):
    if a%i == 0 and b%i == 0:
        ucln = i
print(f"Uoc chung lon nhat cua a va b la: {ucln}")