#In dãy số các soó lẻ nhỏ hơn n
n = int(input("nhap vao so nguyen duong n: "))
for i in range(n): #-> chuỗi chạy từ 0 đến n-1
    if i%2 == 1:
        print(i)
#In n các số Fibonacci
a = 0
b = 1
n = int(input("nhap vao so nguyen duong n: "))
for i in range(n):
    print(a)
    sum_a_b = a + b 
    a =b
    b = sum_a_b
    


#S = 1 + 2 + 3 + 4 + ... + n
#Nhập vào số n tính tổng n số hạng dựa theo S
#S = 1 - 1/2 + 1/3 - 1/4 + 1/5 - ...
# 1/1 + (-1)*1/2 + (1)*1/3 + (-1)*1/4 +...
# ((-1)**n)*(1/n)
# E((-1)**n)*(1/n)
# #Tính tổng các số hạng từ 1 đến n
tong_s = 0
n = int(input("Nhap vao gia tri guyen duong n: "))
for i in range(n + 1):
    tong_s = tong_s + i
    print(f"tong_s = {tong_s}")
    
print(f"Tong cac so tu 1 den n {tong_s}")

#Tính giai thừa của số n (n!)
tich_s = 1
n = int(input("Nhap vao gia tri guyen duong n: "))
for i in range(n + 1):
    if i == 0:
        continue
    tich_s = tich_s*i
    
print(f"Tich cac giai thua cua so n {tich_s}")

# Nhập vào 2 số a, b. Tìm ước chung lớn nhất của 2 số này
a = int(input("Nhap vao so nguyen duong a: "))
b = int(input("Nhap vao so nguyen duong b: "))
so_nho_nhat = a
if b <= a:
    so_nho_nhat = b
k = so_nho_nhat
for i in range(so_nho_nhat):
    if a % k == 0 and b % k == 0:
        print(f"{k} la uoc chung lon nhat")
        break
    k = k - 1
    
#Kiểm tra số n có phải số nguyên tố hay không
# số nguyên tố là số nguyên dương lớn hơn 1 và chỉ chia hết cho 1 và chính nó

n = int(input("Nhap vao so nguyen duong can kiem tra: "))
if n < 1:
    print("So nay khong phai la so nguyen to")
else:
    k = n
    for i in range(n):
        if n % k == 0 and k != n and k != 1:
            print("So nay khong phai la so nguyen to")
            break
        k = k - 1
    else:
        print("So nay la so nguyen to")
            



n = int(input("Nhap so nguuyen duong n: "))
tong_n = 0
for k in range(1,n+1):
    tong_l = 0
    for l in range(1, k+1):
        tong_l = tong_l + (l +1)

    giai_thua_k = 1
    for i in range(1,k+1):
        giai_thua_k = giai_thua_k*i
    tong_n = tong_l/giai_thua_k
    
print(f"ket qua: {tong_n}")
        