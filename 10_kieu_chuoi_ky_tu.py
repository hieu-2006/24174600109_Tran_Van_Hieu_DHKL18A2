# print("Hello world")

# a = "Hello world"
# b = "Hello world"

# c = 'Bạn A nói: "Abcd"'
# d = "Bạn A nói: 'Abcd'"

#Kiểu dữ liệu tuần tự là kiểu dữ liệu có thể truy cập vào các phần tử ở trong nó
#Truy cập sử dụng index (danh mục)

# print(a[4])

#[start:stop:step]
#start: vị trí bắt đầu
#stop: vị trí kết thúc
#step: koảng cách giữa các bước
#print(a[1:7]) #Lấy các giá trị từ start đến stop - 1 
#print(a[:7])
#print(a[1:])
#print(a[:])
#Mặc định step = 1
#print(a[1:7:2])
#print(a[:7:2])
#print(a[1::2])
#print(a[::2])
#print(a[::])
#print(a[1:7:-1]

#print(range(5)) # 0,1,2,3,4

#range cũng sử dụng start, stop, step
# range(1,5)
# range(1,5,2)

# for item in a:
#     print(item)

#Hàm đo độ dài kiểu dữ liệu tuần tự : len
# print(len(a))
# range(len(a)) # thu được chỉ mục chạy từ 0 đến len(a)-1 = 10

# for i in range(len(a)):
#     print(a[i])

# Tính chất của kiểu dữ liệu chuỗi ký tự:
# - Có thể truy cập
# - Không thể chỉnh sửa
# - Không thể sắp xếp

# b = "Hello" + "world"
# print(b)

# n = int(input("nhap vao so nguyen duong: "))
# if n > 0:
#     print("Da nhap dung so nguyen duong")

# c = ""
# for i in range(len(a)):
#     if a[i] == "a":
#         c = c + i

# for i in a:
#     print(i)

#Các phương thức trong xử lý chuỗi ký tự
# a = "Hellworld"
#Các phương thức kiểm tra (trả về cho mình True hoặc False)
#Các phương thức này thường bắt đầu bằng chữ "is"

#Kiểm tra chuỗi có phải alphanumeric (chỉ có ký tự số và chữ hay không)
#print(a.isalnum())
#Kiểm tra chuỗi có toàn số hay không (numeric)
# print(a.isnumeric())
#Kiểm tra chuỗi có toàn chữ hay không (character)
# print(a.isalpha())
#Kiểm tra chuỗi có nằm trong bảng mã ascii hay không
# print(a.isascii())
#Kiểm tra chuỗi có phải kiểu số hay không
# a = "123"
#print(a.isdigit()) # Số thông thường
# print(a.isdecimal()) # Số thập phân

a = "                    "
#Kiểm tra xem chuỗi có khoảng trống hay không
# print(a.isspace())
#Kiểm tra in hoa, in  thường
# print(a.isupper())
# print(a.islower())

a = "hello world"
#Kiểm tra ký tự tồn tại trong chuỗi
#print(a.find("llo"))
# # print(a.count("l"))
# print(a.index("s"))


#Phương thức biển đổi (các phương thức này trả về chuỗi ký tự mới, không tay đổi chuỗi ký tự ban đầu)
a = "Hello world"
# Xóa ký tự đầu cuối của chuỗi
a.strip("d")
a.lstrip()
a.rstrip()
