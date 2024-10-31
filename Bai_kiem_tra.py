import math
x1, x2, x3, x4, y1, y2, y3, y4, z1, z2, z3, z4 <- function
#Nhập tọa độ 3 điểm
A = float(input(x1 ,y1 ,z1 ))
B = float(input(x2 ,y2 ,z2 ))
C = float(input(x3 ,y2 ,z3 ))
A1 = float(input(x4 ,y4 ,z4 ))
#Tọa độ đoạn thẳng
AB = ((x2 - x1)*2 + (y2 - y1)*2 +(z2 - z1)*2)
AA1 = ((x4 - x1)*2 + (y4 - y1)*2 + (z4 - z1)*2)
#Thể tích hình hộp vuông
V = AB * AA1
#In ra kết quả
print("Thể tích hình hộp vuông là: ")

