n = int(input("Nhap vao 1 so nguyen: "))
if n <= 0:
    print(f"{n} khong la so chinh phuong")
else:
    sbp = False
    for i in range(1,n+1):
        if i*i == n:
            sbp = True
            break
    
    if sbp:
        print(f"{n} la so chinh phuong")
    else:
        print(f"{n} khong la so chinh phuong")