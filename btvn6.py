print("Chào mừng bạn đến rạp chiếu phim ABC!")
print("Các thể loại phim hiện đang có:")
print("1. Phim tình cảm")
print("2. Phim kinh dị")
print("3. Phim hoạt hình")
print("4. Phim khoa học viễn tưởng")
lua_chon = input("Vui lòng nhập số tương ứng với thể loại phim bạn muốn xem (1-4): ")
if lua_chon == '1':
    print("Bạn đã chọn thể loại: Phim tình cảm.")
elif lua_chon == '2':
    print("Bạn đã chọn thể loại: Phim kinh dị.")
elif lua_chon == '3':
    print("Bạn đã chọn thể loại: Phim hoạt hình.")
elif lua_chon == '4':
    print("Bạn đã chọn thể loại: Phim khoa học viễn tưởng.")
else:
    print("Lựa chọn không hợp lệ. Vui lòng nhập lại từ 1 đến 4.")
