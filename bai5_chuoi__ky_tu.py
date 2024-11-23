input_string = input("Nhap vao chuoi ky tu: ")
count_upper = 0
count_lower = 0
for char in input_string:
    if char.isupper():
        count_upper += 1
    elif char.islower():
        count_lower += 1
print("So chu cai viet hoa la:", count_upper)
print("So chu cai viet thuong la:", count_lower)
