tu = int(input("Nhap tu so: "))
mau = int(input("Nhap mau so: "))
snn = min(tu,mau)
ucln = 1
for i in range(1,snn+1):
    if tu%i == 0 and mau%i == 0:
        ucln = i
tu_toi_gian = tu // ucln 
mau_toi_gian = mau // ucln
print(f"Vay phan so toi gian la: {tu_toi_gian}/{mau_toi_gian}")