a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))
if a + b <= c or a + c <= b or b + c <= a:
    print("Không phải là bộ ba cạnh của tam giác.")
else:
    if a == b == c:
        print("Đây là tam giác đều.")
    elif a == b or a == c or b == c:
        if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            print("Đây là tam giác vuông cân.")
        else:
            print("Đây là tam giác cân.")
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("Đây là tam giác vuông.")
    else:
        print("Đây là tam giác thường.")
