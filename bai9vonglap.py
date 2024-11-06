n = int(input("Nhap vao 11 so nguyen n: "))
print(f"Cac so chinh phuong nho hon {n} la: ")
for num in range(1,n):
    if num*num < n:
        print(num*num)