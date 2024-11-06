n = int(input("Nhap vao 1 so nguyen n: "))
print(f"Cac so hoan hao nho hon {n} la: ")
for num in range(2,n):
    sum = 0
    for i in range(1,num):
        if num%i == 0:
            sum = sum + i
    if sum == num:
        print(num)