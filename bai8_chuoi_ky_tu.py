str_1 = input("Nhap chuoi 1 (str_1): ")
str_2 = input("Nhap chuoi 2 (str_2): ")
if str_2 in str_1:
    print(f"'{str_2}' co trong '{str_1}'")
else:
    print(f"'{str_2}' khong co trong '{str_1}'")
if str_1 in str_2:
        print(f"'{str_1}' co trong '{str_2}'")
else:
        print(f"'{str_1}' khong co trong '{str_2}'")