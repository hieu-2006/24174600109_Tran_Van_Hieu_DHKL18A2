danh_sach_sinh_vien = []
while True:
    print("\nChuong trinh quan ly danh sach sinh vien")
    print("1. Xem danh sach sinh vien")
    print("2. Nhap thong tin sinh vien moi vao danh sach")
    print("3. Chinh sua thong tin sinh vien ung voi ma sinh vien")
    print("4. Xoa thong tin sinh vien ung voi ma sinh vien")
    print("5. Thoat chuong trinh")
    
    lua_chon = int(input("Chon chuc nang (1-5): "))

    if lua_chon == 1:
        if not danh_sach_sinh_vien:
            print("Danh sach sinh vien hien tai trong")
        else:
            print("\nDanh sach sinh vien: ")
            print(f"{'Ma SV':<10} {'Ho dem':<20} {'Ten':<15} {'Toan':<8} {'Ly':<8} {'Hoa':<8} {'TB':<6}")
            for sv in danh_sach_sinh_vien:
                print(f"{sv['Ma sinh vien']:<10} {sv['Ho dem']:<20} {sv['Ten']:<15} {sv['Diem toan']:<8} {sv['Diem ly']:<8} {sv['Diem hoa']:<8} {sv['Diem trung binh']:<6.2f}")
    
    elif lua_chon == 2:
        ma_sinh_vien = input("Nhap ma sinh vien: ")
        ho_dem = input("Nhap ho dem: ")
        ten = input("Nhap ten sinh vien: ")
        diem_toan = float(input("Nhap diem toan: "))
        diem_ly = float(input("Nhap diem ly: "))
        diem_hoa = float(input("Nhap diem hoa: "))
        diem_trung_binh = (diem_toan + diem_ly + diem_hoa) / 3
        sinh_vien = {
            "Ma sinh vien": ma_sinh_vien,
            "Ho dem": ho_dem,
            "Ten": ten,
            "Diem toan": diem_toan,
            "Diem ly": diem_ly,
            "Diem hoa": diem_hoa,
            "Diem trung binh": diem_trung_binh
        }
        
        danh_sach_sinh_vien.append(sinh_vien)
        print("Da them sinh vien vao danh sach")
    
    elif lua_chon == 3:
        ma_sinh_vien_can_sua = input("Nhap ma sinh vien can sua: ")
        sinh_vien_ton_tai = False
        for sv in danh_sach_sinh_vien:
            if sv['Mã sinh viên'] == ma_sinh_vien_can_sua:
                sinh_vien_ton_tai = True
                print("Thong tin sinh vien hien tai:")
                print(f"Ma sinh vien: {sv['Ma sinh vien']}")
                print(f"Ho đem: {sv['Ho dem']}")
                print(f"Ten: {sv['Ten']}")
                print(f"Diem toan: {sv['Diem toan']}")
                print(f"Diem ly: {sv['Diem ly']}")
                print(f"Diem hoa: {sv['Diem hoa']}")
        
                ho_dem_moi = input("Nhap ho dem moi: ")
                ten_moi = input("Nhap ten moi: ")
                diem_toan_moi = float(input("Nhap diem toan moi: "))
                diem_ly_moi = float(input("Nhap diem ly moi: "))
                diem_hoa_moi = float(input("Nhap diem hoa moi: "))
                
                diem_trung_binh_moi = (diem_toan_moi + diem_ly_moi + diem_hoa_moi) / 3
                sv['Ho dem'] = ho_dem_moi
                sv['Ten'] = ten_moi
                sv['Diem toan'] = diem_toan_moi
                sv['Diem ly'] = diem_ly_moi
                sv['Diem hoa'] = diem_hoa_moi
                sv['Diem trung binh'] = diem_trung_binh_moi
                
                print("Thong tin sinh vien da duoc cap nhap")
                break
        
        if not sinh_vien_ton_tai:
            print(f"Sinh vien voi ma {ma_sinh_vien_can_sua} khong ton tai")
    
    elif lua_chon == 4:
        ma_sinh_vien_can_xoa = input("Nhap ma sinh vien can xoa: ")
        sinh_vien_ton_tai = False
        for sv in danh_sach_sinh_vien:
            if sv['Ma sinh vien'] == ma_sinh_vien_can_xoa:
                sinh_vien_ton_tai = True
                danh_sach_sinh_vien.remove(sv)
                print("Sinh vien da duoc xoa khoi danh sach")
                break
        
        if not sinh_vien_ton_tai:
            print(f"Sinh vien voi ma {ma_sinh_vien_can_xoa} khong ton tai")
    
    elif lua_chon == 5:
        print("Thoat chuong trinh")
        break

    else:
        print("Lua chon khong hop le hay chon lai")

