input_string = input("Nhap mot chuoi ky tu: ")
if input_string.startswith('-') and input_string[1:].isdigit():
    print("Chuoi nay la so am ")
else:
    print("Chuoi nay khong phai la so am")
