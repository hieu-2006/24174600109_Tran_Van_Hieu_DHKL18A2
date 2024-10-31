ky_tu = input("Nhập một ký tự: ")
if ky_tu.isalpha() and ky_tu != "":
    ky_tu = ky_tu.lower()
    if ky_tu in 'euoai':
        print(f"Ký tự '{ky_tu}' là nguyên âm.")
    else:
        print(f"Ký tự '{ky_tu}' là phụ âm.")
else:
    print("Vui lòng nhập một ký tự chữ cái hợp lệ.")
