chuoi_ki_tu = input("Yeu cau nhap chuoi ki tu: ") #Input luôn trả về kiểu dữ liệu là chuôi kí tự
# print("In ra man hinh", 123, "va", chuoi_ki_tu)
print(f"In ra man hinh {chuoi_ki_tu}")


gia_tri_nhap = input("Yeu cau nhap vao so tu nhien: ") #mang kiểu kí tự
bien_so_nguyen = int(gia_tri_nhap) #ép kiểu số nguyên int
bien_so_thuc = float(gia_tri_nhap) #ép kiểu số thực float
bien_chuoi_ki_tu = str(gia_tri_nhap) #ép kiểu kí tự
bien_boolean = bool(gia_tri_nhap) #ép kiểu boolean
print(bien_boolean) #Khi ép kiểu boolean cho kiểu kí tự luôn trả về true
#0 -> False
#1 -> True
bien_boolean = bool(int(input("Yeu cau nhap vao so tu nhien: ")))



#Câu lệnh điều kiện 
#3 kiểu viêt câu lệnh đièu kiện
#Câu lệnh if
#Câu lệnh if...else
#Câu lệnh if...else...else
#Câu lệnh if...elif...else(sử dụng vs nhiều điều kiện còn xét)

#Xử lý xoay quannh boolean (True, False)
1 > 2
1 < 2
1 >= 2
1 <= 2
1 == 2
1 != 2
"abc" == "123"
#=> trả về kết quả True hoặc False
#Đối với if khi xét điều kiện
#Nếu điều kiện đúng (True) thì câu lệnh của if sẽ hoạt động
#Nếu điều kiện sai (False) thì câu lệnh của if sẽ bị bỏ qua
a = 10
if a > 5:
    print("Gia tri a thoa man dieu kien")
    b = a + 1
print("Ket thuc chuong trinh")

