#bai4
#Đề bài cho
U = 220
I = 2.7
gia_tien_dien = 7000
#CT Tính công suất
P = U * I
#Thời gian sử dụng bóng đèn
t = float(input("Nhap thoi gian su dung bong den (s): "))
#Chuyển đơn vị thơi gian
T = t / 3600
#Số tiền phải trả là
if T > 0:
    so_tien_phai_tra = (P / 1000) * T * gia_tien_dien
    print(f"So tien phai tra la: {so_tien_phai_tra:.2f}")
else:
    print("Thoi gian su dung phai lon hon 0. ")    