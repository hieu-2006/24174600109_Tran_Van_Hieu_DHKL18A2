a = 0
b = 1
print("50 so dau tien trong day Fibonacci")
print(a)
for i in range(1,50):
    print(b)
    next_number = a + b
    a = b
    b = next_number
    
    
    
# Số lượng số Fibonacci cần in ra
n = 50

# Khởi tạo hai số đầu tiên của dãy Fibonacci
a, b = 0, 1

# Sử dụng vòng lặp for để in ra 50 số đầu tiên
for i in range(n):
    print(a, end=" ")  # In ra số a, không xuống dòng
    a, b = b, a + b  # Cập nhật a và b cho số tiếp theo trong dãy
