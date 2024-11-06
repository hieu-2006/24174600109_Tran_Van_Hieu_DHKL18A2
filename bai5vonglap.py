n = int(input("Nhap vao 1 so nguyen: "))
if n < 2:
    print(f"{n} khong phai la so hoan hao")
else:
    sum = 0
    for i in range(1,n):
        if n%i == 0:
            sum = sum + i
    if sum == n:
        print(f"{n} la so hoan hao")
    else:
        print(f"{n} khong phai la so hoan hao")