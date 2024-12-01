#Bài 1: Nhập vào số nguyên dương n. 
#In ra màn hình dãy số các số nguyên tố nhỏ hơn n theo thứ tự từ nhỏ đến lớn
# ds_nguyen_to = []
# while True:
#     n = input("Nhap vao so nguyen duong n: ")
#     if n.isdigit() == False:
#         print("Yeu cau nhap lai so nguyen duong!!")
#     else:
#         n = int(n)
#         break

# for i in range(1, n):
#     if i == 1:
#         ds_nguyen_to.append(i)
#         continue
#     for j in range(1, i):
#         if i%j == 0 and j != 1 and i != j:
#             break
#     else:
#         ds_nguyen_to.append(i)

# ds_nguyen_to.sort()
# print(ds_nguyen_to)
#Tính tổng các giá trị trong danh sách
# tong = sum(ds_nguyen_to)
# print(tong)




#Bài 2: Nhập vào dãy A gồm n phần tử từ bàn phím. 
#Tính tổng các phần tử trong dãy A
# ds_so = []

# while True:
#     n = input("Nhap vao so pan tu n trong danh sach: ")
#     if n.isdigit() == False:
#         print("Yeu cau nhap lai so nguyen duong!!")
#     else:
#         n = int(n)
#         break

# for i in range(n):
#     while True:
#         so = input(f"Nhap gia tri so thu {i + 1}: ")
#         if so.isdigit() == False:
#             print("Yeu cau nhap vao so!!")
#         else:
#             so = float(so)
#             break
#     ds_so.append
        
# tong = sum(ds_so)
# print(f"Tong cac so vua nhap: {tong}")


# ds_so = []
# while True:
#     n = input("Nhap vao so phan tu n trong danh sach: ")
#     if n.isdigit() == False:
#        print("Yeu cau nhap lai so nguyen duong!!")
        
#     else:
#          n = int(n)
#          break

# for i in range(n):
#     while True:
#         so = input(f"Nhap gia tri so thu {i + 1}: ")
#         if so.count('-') == 1 and so.replace('-','').isdigit():
#             so = float(so)
#             break
#         else:
#             print("Yeu cau nhap vao so!!")
            
#     ds_so.append(so)

# tong = sum(ds_so)
# print(f"Tong cac so vua nhap: {tong}")

#Bài 3: Nhập vào số nguyên dương n.
#In ra màn hình: 
# - Danh sách A gồm các số lẻ nhỏ hơn n
# - Danh sách B gồm các số chẵn nhỏ hơn n
#Sắp xếp dãy số theo thứ tự giảm dần
# n = int(input("Nhap so nguyen duong n: "))
# A = []
# B = []
# for i in range(n):
#     if i % 2 != 0:
#         A.append(i)
#     else:
#         B.append(i)

# A.sort(reverse=True)
# B.sort(reverse=True)
# print("Danh sach A (so le):", A)
# print("Danh sach B (so chan):", B)


#Bài 4: Viết chương trình sinh ra ma trận K kích cỡ m*n chỉ chứa số 0
# m = int(input("Nhap vao so cot cua ma tran m = "))
# n = int(input("Nhap vao so hang cua ma tran n = "))
# #0 ... 0
# #.     .
# #.     .
# #.     .
# #0 ... 0
# ma_tran_a = [[0,0,0],
#              [0,0,0],
#              [0,0,0]]
# for hang in range(n):
#     phan_tu_trong_hang = []
#     for cot in range(m):
#         phan_tu_trong_hang.append(0)
#     ma_tran_a.append(phan_tu_trong_hang)
# print(ma_tran_a)
# ma_tran_a = [[0]*m]*n #=> [[0,0,0,0,...,m],...]
# print(ma_tran_a)



#Bài 5: Viết chương trình nhập vào n. Sinh ra ma trận đơn vị I kích cỡ n*n
#1 0 0 0
#0 1 0 0
#0 0 1 0
#0 0 0 1
# n = int(input("Nhap vao n = "))
# ma_tran_don_vi = []
# for i in range(n):
#     phan_tu_trong_hang = [0]*i + [1] + [0]*(n-i)
#     ma_tran_don_vi.append(phan_tu_trong_hang)
# print(ma_tran_don_vi)

#Bài 7: Viết chương trình đảo vị trí hai hàng i, j của ma trận A kích cỡ m*n
#1 0 0 0
#0 1 0 0
#0 0 1 0
#0 0 0 1
# i = int(input("Nhap vao hang i: "))
# j = int(input("Nhap vao hang j: "))
# [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0],[0, 0, 0, 1]]
# temp = ma_tran_don_vi[i]
# ma_tran_don_vi[i] = ma_tran_don_vi[j]
# ma_tran_don_vi[j] = temp
# print(ma_tran_don_vi)































#Bài10: Lập một danh sách với n sinh viên bao gồm thông tin tên và điểm tổng kết cuối năm của các sinh viên đó
n = int(input("Nhap so luong sinh vien: "))
ds_sv = []
for i in range(n):
    print(f"Nhap thong tin cho sinh vien {i+1}:")
    ten = input("Ten sinh vien: ")
    diem = float(input("Điem tong ket cuoi nam: "))
    ttin_sv = {"Ten": ten, "Điem": diem}
    ds_sv.append(ttin_sv)

print("\nDanh sach sinh vien:")
for sv in ds_sv:
    print(f"Ten: {sv['Ten']}, Điem: {sv['Điem']}")
