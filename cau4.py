#giải pt bậc 2 a*x**2 + b*x + c = 0 ( với a, b , c là kiểu số nguyên)
a = input("nhập giá trị a") 
b = input("nhập giá trị c")
c = input("nhập giá trị c")

a = int(a)
b = int(b)
c = int(c)

if a < 0 and b < 0 and c < 0:
    if a != 0:
        delta = b**2 - 4*a*c
        if delta > 0:
            x_1 = (-b + delta**(1/2))/(2*a)
            x_2 = (-b - delta**(1/2))/(2*a)
            print(f"Phuong trinh co 2 nghiem phan biet {x_1}, {x_2}")
        elif delta == 0:
            x_3 = -b/(2*a)
            print(f"Phuong trinh co nghiem kep {x_3}")
    else:
        if b != 0:
            x_0 = (-c)/b
            print(f"Phuong trinh co 1 nghiem duy nhat {x_0}")
        else:
            if c != 0:
                print("Phuong trinh vo nghiem")
            else:
                print("Phuong trinh co vo so nghiem")
#Print("Chuong trinh vo nghiem")
        