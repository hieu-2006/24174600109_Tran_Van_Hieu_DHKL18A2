def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_prime_input():
    while True:
        user_input = input("Nhap so nguyen n: ")
        if user_input.isdigit():
            num = int(user_input)
            if is_prime(num):
                return num
            else:
                print(f"{num} khong phai la so nguyen to, hay nhap lai")
        else:
            print("Day khong phai so nguyen, hay nhap lai")

number = get_prime_input()
print(f"{number} la so nguyen to")
