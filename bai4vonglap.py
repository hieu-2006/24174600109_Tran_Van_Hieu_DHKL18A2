n = int(input("Nhập một số: "))
if n < 2:
    print(f"{n} không phải là số nguyên tố.")
else:
    sng = True
    for i in range(2, int(n**0.5) + 1):
        if n%i == 0:
            sng = False
            break
    if sng:
        print(f"{n} là số nguyên tố.")
    else:
        print(f"{n} không phải là số nguyên tố.")
