def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def get_ucln_input():
    while True:
        try:
            num1 = int(input("Nhập số nguyên thứ nhất: "))
            num2 = int(input("Nhập số nguyên thứ hai: "))
            result = ucln(num1, num2)
            print(f"Ước chung lớn nhất của {num1} và {num2} là: {result}")
            break
        except ValueError:
            print("Vui lòng nhập số nguyên hợp lệ.")

get_ucln_input()
