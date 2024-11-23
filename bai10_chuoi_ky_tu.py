input_str = input("Nhap vao chuoi ky tu: ")
numbers = ""
letters = ""
for char in input_str:
    if char.isdigit():
        numbers = numbers + char
    else:
        letters = letters + char
result = numbers + letters
print("Ket qua sau khi tat ca so sang ben trai la:", result)
