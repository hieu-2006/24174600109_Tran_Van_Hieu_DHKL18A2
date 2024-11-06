#Vòng lặp trong python
#Vòng lặp có giới hạn (vòng lặp for)

#Các kiểu dữ liệu tuần tự: string, list, tuple, set, dictionary
# range()
for abc in range(10):
    print(abc)
#range(10) -> 0,1,2,3,4,5,6,7,8,9
#range khi truyền gía trị mặc định yêu cầu phải là giá trị nguyên dương
#Các giá trị trong range sẽ chạy từ 0 đến n-1

#Khi sử dụng vòng lặp nên kết hợp sử dụng với các câu lệnh điều kiện
#(Khi sử dụng vòng lặp nên có mục đích rõ ràng)

#Trong python vòng lặp cung cấp cho người dùng 3 công cụ: break, continue, else
#break: Dừng vòng lặp ngay lập tức tại lần lặp gặp break
for i in range(10):
    if i == 4:
        break
    print(i)
#continue: Vòng lặp sẽ bỏ qua lần lặp mà ở đấy xuất hiện continue
for i in range(10):
    if i == 4:
        continue
    print(i)
#else: Vòng lặp sẽ chạy các câu lệnh xử lý của else trong trường hợp vòng lặp không gặp break
for i in range(10):
    if i == 4:
        break
    print(i)
else:
    print("Chay cau lenh else")
#Vòng lặp không giới hạn (vòng lặp while)
n = 10
while n > 2:
    print("chay vong lap {n}")
    n = n - 1
    if n == 6:
        break
else:
    print("chay cau lenh else")
    
    
    
    
n = 10
while n > 2:
    print("chay vong lap {n}")
    n = n - 1
    if n == 6:
        continue
else:
    print("chay cau lenh else")

n = 10
while True:
    for i in range(1,n):
        if n%i==0 i!=1 and 1!=n:
            print("so nay khong phai so nguyen to")
            break
    else:
        break
        
    if n < 1:
        break
print(f"day la so nguyen to {n}")






n = 10
tong_n = 0
for k in range(1,n):
    tong_i = tong_i + (1 + i)
tong_n = tong_n + (tong_i/k)
print(f"ket qua: {tong_n}")
