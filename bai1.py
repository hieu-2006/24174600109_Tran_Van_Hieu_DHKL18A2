#bai1
#bán kính = r
#chiều cao = h
#dtxp = 2*pi*r*h
#dttp = dtxp + 2*pi*r**2
r = float(input("Nhap vao ban kinh: "))
h = float(input("Nap vao chieuu cao: "))
if h> 0 and r > 0:
    pi = 3.14
    dtxp = 2*pi*r*h
    dttp = dtxp + 2*pi*r**2
    print(f"Dien tich xung quanh: {dtxp:.2f}")
    print(f"Dien tich toan phan: {dttp:.2f}")
else:
    print("gia tri nhap khong thoa man")
print("ket thuc chuong trinh.")