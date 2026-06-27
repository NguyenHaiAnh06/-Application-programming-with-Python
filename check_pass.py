# Bài 3: Nhập vào một chuỗi và kiểm tra chuỗi đó đáp ứng đủ các tiêu chí của mật khẩu mạnh
# không, gồm:
# qÍt nhất 1 ký tự nằm trong [a-z, A-Z]
# qKhông chứa ký tự cách
# qÍt nhất 1 số nằm trong [0-9]
# qÍt nhất 1 ký tự đặc biệt nằm trong tập (){}!@#$%
# qĐộ dài mật khẩu tối thiểu: 8
# qĐộ dài mật khẩu tối đa: 12

def check_Ky_tu_cach(password):
    return " " not in password #tra ve ki tu cach ko nam trong chuoi password , neu co lat return co ki tu cach


def check_length(password):
    return 8 <= len(password) <= 12


def check_ky_tu_dac_biet(password):
    for char in password:
        if char in "(){}!@#$%":
            return True
    return False


def check_chu_va_so(password):
    co_chu = False
    co_so = False
    for char in password:
        if char.isalpha(): #cac ham trong tai lieu string
            co_chu = True
        if char.isdigit():
            co_so = True
    return co_chu and co_so

def check_password_hop_le(password):
    if not check_length(password):
        return "Thất bại: Độ dài phải từ 8-12 ký tự"
    if not check_Ky_tu_cach(password):
        return "Thất bại: Mật khẩu có chứa khoảng trắng"
    if not check_ky_tu_dac_biet(password):
        return "Thất bại: Thiếu ký tự đặc biệt"
    if not check_chu_va_so(password):
        return "Thất bại: Phải có ít nhất 1 chữ và 1 số"

    return "Thành công: Mật khẩu mạnh!"

test_1 = input()
oktest = check_password_hop_le(test_1)
print(oktest)