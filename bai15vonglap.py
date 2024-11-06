print("Chon loai chuyen đoi:")
print("1. Chuyen tu he thap phan sang he nhi phan")
print("2. Chuyen tu he nhi phan sang he thap phan")

choice = int(input("Nhap lua chon (1 hoac 2): "))

if choice == 1:
    decimal = int(input("Nhap so trong he thap phan: "))

    if decimal == 0:
        print("So trong he nhi phan la: 0")
    else:
        binary = ""  
        while decimal > 0:
            binary = str(decimal % 2) + binary  
            decimal = decimal // 2  
        
        print("So trong he nhi phan la:", binary)

elif choice == 2:
    binary = input("Nhap so trong he nhi phan: ")
    
    decimal = 0  
    length = len(binary)  
    for i in range(length):
        decimal = decimal + int(binary[length - i - 1]) * (2 ** i)
    
    print("So trong he thap phan la:", decimal)

else:
    print("Lua chon khong hop le. Vui long chon 1 hoac 2.")
