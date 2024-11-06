n = int(input("Nhap vao 1 so nguyen n: "))
print(f"Cac so nguyen to nho hon {n} la: ")
for num in range(2,n):
    sng = True
    for i in range(2,num):
        if num%i == 0:
            sng = False
            break
    if sng:
        print(num)