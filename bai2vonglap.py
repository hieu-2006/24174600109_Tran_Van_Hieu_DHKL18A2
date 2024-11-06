#S1
n = int(input("Nhap n cua S1: "))
sum = 0
for i in range(1,n+1):
    sum = sum + i
print(f"Vay gia tri cua S1 la: {sum}")
#S2
n = int(input("Nhap n cua S2: "))
factorial = 1 #Giai thừa
for i in range(1,n):
    factorial = factorial*i
print(f"Vay gia tri của S2 là: {factorial}")
#S3
n = int(input("Nhap n cua S3: "))
sum = 0
for i in range(1,n+1):
    if i%2 == 0:
        sum = sum - 1/i
    else:
        sum = sum + 1/i
print(f"Vay gia tri cua S3 la: {sum}")
#S4
n = int(input("Nhap n cua S4: "))
sum = 0
for k in range(1,n+1):
    sum = sum + k/(k+2)
print(f"Vay gia tri cua S4 la: {sum}")
