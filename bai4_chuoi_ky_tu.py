input_string = input("Nhap vao chuoi ky tu: ")
count_letters = 0
count_digits = 0
count_special = 0
for char in input_string:
    if char.isalpha():  
        count_letters = count_letters + 1
    elif char.isdigit():
        count_digits = count_digits + 1
    elif not char.isspace():
        count_special = count_special + 1
print("So ky tu la chu: ", count_letters)
print("So ky tu la so: ", count_digits)
print("So ky tu đac biet la: ", count_special)
