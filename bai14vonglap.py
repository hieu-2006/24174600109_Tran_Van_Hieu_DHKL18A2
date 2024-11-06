n = int(input("Nhap so hang cua tam giac Pascal: "))
for i in range(n):
    print(" " * (n - i - 1), end="")
    C = 1  
    for j in range(i + 1):
        print(C, end=" ")
        C = C * (i - j) // (j + 1)
    
    print()



n = int(input("Nhap so hang cua tam giac Floyd: "))
current_num = 1  
for i in range(1,n+1):
    for j in range(i):
        print(current_num, end=" ")
        current_num = current_num + 1
    print()  
