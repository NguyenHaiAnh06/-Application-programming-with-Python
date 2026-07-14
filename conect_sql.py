from db import dtb


class Mathang:
    def __init__(self, mahang, tenhang, mota, dongia, nguongoc):
        self._mahang = mahang
        self._tenhang = tenhang
        self._mota = mota
        self._dongia = dongia
        self._nguongoc = nguongoc

    def get_mahang(self):
        return self._mahang
    def get_tenhang(self):
        return self._tenhang
    def get_mota(self):
        return self._mota
    def get_dongia(self):
        return self._dongia
    def get_nguongoc(self):
        return self._nguongoc

    def set_tenhang(self, tenhang):
        self._tenhang = tenhang
    def set_mota(self, mota):
        self._mota = mota
    def set_dongia(self, dongia):
        self._dongia = dongia
    def set_nguongoc(self, nguongoc):
        self._nguongoc = nguongoc

    def to_tuple(self):
        return (self._mahang, self._tenhang, self._mota, self._dongia, self._nguongoc)

    def __str__(self):
        return f'{self._mahang} | {self._tenhang} | {self._mota} | {self._dongia} | {self._nguongoc}'


class KhachHang:
    def __init__(self, makhach, tenkhach, tuoi, gioitinh, sodienthoai, diachi):
        self._makhach = makhach
        self._tenkhach = tenkhach
        self._tuoi = tuoi
        self._gioitinh = gioitinh
        self._sodienthoai = sodienthoai
        self._diachi = diachi

    def get_makhach(self):
        return self._makhach
    def get_tenkhach(self):
        return self._tenkhach
    def get_tuoi(self):
        return self._tuoi
    def get_gioitinh(self):
        return self._gioitinh
    def get_sodienthoai(self):
        return self._sodienthoai
    def get_diachi(self):
        return self._diachi

    def to_tuple(self):
        return (self._makhach, self._tenkhach, self._tuoi, self._gioitinh, self._sodienthoai, self._diachi)

    def __str__(self):
        return f"{self._makhach} | {self._tenkhach} | {self._tuoi} | {self._gioitinh} | {self._sodienthoai} | {self._diachi}"


class DonHang:
    def __init__(self, madonhang, makhach, ngaymua, tinhtrang):
        self._madonhang = madonhang
        self._makhach = makhach
        self._ngaymua = ngaymua
        self._tinhtrang = tinhtrang

    def get_madonhang(self):
        return self._madonhang
    def get_makhach(self):
        return self._makhach
    def get_ngaymua(self):
        return self._ngaymua
    def get_tinhtrang(self):
        return self._tinhtrang

    def to_tuple(self):
        return (self._madonhang, self._makhach, self._ngaymua, self._tinhtrang)

    def __str__(self):
        return f"{self._madonhang} | {self._makhach} | {self._ngaymua} | {self._tinhtrang}"


class ChiTietDonHang:
    def __init__(self, machitiet, madonhang, mahang, soluong, dongia):
        self._machitiet = machitiet
        self._madonhang = madonhang
        self._mahang = mahang
        self._soluong = soluong
        self._dongia = dongia

    def get_machitiet(self):
        return self._machitiet
    def get_madonhang(self):
        return self._madonhang
    def get_mahang(self):
        return self._mahang
    def get_soluong(self):
        return self._soluong
    def get_dongia(self):
        return self._dongia

    def to_tuple(self):
        return (self._machitiet, self._madonhang, self._mahang, self._soluong, self._dongia) #cho truyen data

#hien thi phuong thuc
    def __str__(self):
        return f"{self._machitiet} | {self._madonhang} | {self._mahang} | {self._soluong} | {self._dongia}"


def hien_thi_mathang():
    cursor = dtb.cursor()
    cursor.execute("SELECT mahang, tenhang, mota, dongia, nguongoc FROM tbmathang")
    rows = cursor.fetchall()
    cursor.close()
    if not rows:
        print("Chưa có mặt hàng nào.")
        return
    for row in rows:
        print(row)

def them_mathang():
    try:
        mahang = input("Nhập mã hàng: ")
        tenhang = input("Nhập tên hàng: ")
        mota = input("Nhập mô tả: ")
        dongia = float(input("Nhập đơn giá: "))
        nguongoc = input("Nhập nguồn gốc: ")

        mh = Mathang(mahang, tenhang, mota, dongia, nguongoc)

        cursor = dtb.cursor()
        sql = """
            INSERT INTO tbmathang (mahang, tenhang, mota, dongia, nguongoc)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(sql, mh.to_tuple())
        dtb.commit()
        cursor.close()
        print("Thêm mặt hàng thành công!")
    except Exception as e:
        print("Lỗi khi thêm mặt hàng:", e)

def sua_mathang():
    try:
        mahang = input("Nhập mã hàng cần sửa: ")
        tenhang = input("Nhập tên hàng mới: ")
        mota = input("Nhập mô tả mới: ")
        dongia = float(input("Nhập đơn giá mới: "))
        nguongoc = input("Nhập nguồn gốc mới: ")

        cursor = dtb.cursor()
        sql = """
            UPDATE tbmathang
            SET tenhang = %s, mota = %s, dongia = %s, nguongoc = %s
            WHERE mahang = %s
        """
        cursor.execute(sql, (tenhang, mota, dongia, nguongoc, mahang))
        dtb.commit()
        if cursor.rowcount > 0:
            print("Sửa mặt hàng thành công!")
        else:
            print("Không tìm thấy mã hàng cần sửa.")
        cursor.close()
    except Exception as e:
        print("Lỗi khi sửa mặt hàng:", e)

def xoa_mathang():
    try:
        mahang = input("Nhập mã hàng cần xoá: ")
        cursor = dtb.cursor()
        cursor.execute("DELETE FROM tbmathang WHERE mahang = %s", (mahang,))
        dtb.commit()
        if cursor.rowcount > 0:
            print("Xoá mặt hàng thành công!")
        else:
            print("Không tìm thấy mã hàng cần xoá.")
        cursor.close()
    except Exception as e:
        print("Lỗi khi xoá mặt hàng:", e)

def tim_kiem_mathang():
    try:
        tu_khoa = input("Nhập mã/tên/nguồn gốc cần tìm: ")
        cursor = dtb.cursor()
        sql = """
            SELECT mahang, tenhang, mota, dongia, nguongoc
            FROM tbmathang
            WHERE mahang LIKE %s OR tenhang LIKE %s OR nguongoc LIKE %s
        """
        key = f"%{tu_khoa}%"
        cursor.execute(sql, (key, key, key))
        rows = cursor.fetchall()
        cursor.close()
        if not rows:
            print("Không tìm thấy mặt hàng.")
            return
        for row in rows:
            print(row)
    except Exception as e:
        print("Lỗi khi tìm kiếm mặt hàng:", e)


def hien_thi_khachhang():
    cursor = dtb.cursor()
    cursor.execute("SELECT makhach, tenkhach, tuoi, gioitinh, sodienthoai, diachi FROM tbkhachhang")
    rows = cursor.fetchall()
    cursor.close()
    if not rows:
        print("Chưa có khách hàng nào.")
        return
    for row in rows:
        print(row)

def them_khachhang():
    try:
        makhach = input("Nhập mã khách hàng: ")
        tenkhach = input("Nhập tên khách hàng: ")
        tuoi = int(input("Nhập tuổi: "))
        gioitinh = input("Nhập giới tính: ")
        sodienthoai = input("Nhập số điện thoại: ")
        diachi = input("Nhập địa chi: ")

        kh = KhachHang(makhach, tenkhach, tuoi, gioitinh, sodienthoai, diachi)

        cursor = dtb.cursor()
        sql = """
            INSERT INTO tbkhachhang (makhach, tenkhach, tuoi, gioitinh, sodienthoai, diachi)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(sql, kh.to_tuple())
        dtb.commit()
        cursor.close()
        print("Thêm khách hàng thành công!")
    except Exception as e:
        print("Lỗi khi thêm khách hàng:", e)

def sua_khachhang():
    try:
        makhach = input("Nhập mã khách hàng cần sửa: ")
        tenkhach = input("Nhập tên khách hàng mới: ")
        tuoi = int(input("Nhập tuổi mới: "))
        gioitinh = input("Nhập giới tính mới: ")
        sodienthoai = input("Nhập số điện thoại mới: ")
        diachi = input("Nhập địa chỉ mới: ")

        cursor = dtb.cursor()
        sql = """
            UPDATE tbkhachhang
            SET tenkhach = %s, tuoi = %s, gioitinh = %s, sodienthoai = %s, diachi = %s
            WHERE makhach = %s
        """
        cursor.execute(sql, (tenkhach, tuoi, gioitinh, sodienthoai, diachi, makhach))
        dtb.commit()
        if cursor.rowcount > 0:
            print("Sửa khách hàng thành công!")
        else:
            print("Không tìm thấy mã khách hàng cần sửa.")
        cursor.close()
    except Exception as e:
        print("Lỗi khi sửa khách hàng:", e)

def xoa_khachhang():
    try:
        makhach = input("Nhập mã khách hàng cần xóa: ")
        cursor = dtb.cursor()
        cursor.execute("DELETE FROM tbkhachhang WHERE makhach = %s", (makhach,))
        dtb.commit()
        if cursor.rowcount > 0:
            print("Xóa khách hàng thành công!")
        else:
            print("Không tìm thấy mã khách hàng cần xóa.")
        cursor.close()
    except Exception as e:
        print("Lỗi khi xóa khách hàng:", e)

def tim_kiem_khachhang():
    try:
        tu_khoa = input("Nhập mã/tên/địa chỉ/sđt cần tìm: ")
        key = f"%{tu_khoa}%"
        cursor = dtb.cursor()
        sql = """
            SELECT makhach, tenkhach, tuoi, gioitinh, sodienthoai, diachi
            FROM tbkhachhang
            WHERE makhach LIKE %s OR tenkhach LIKE %s OR diachi LIKE %s OR sodienthoai LIKE %s
        """
        cursor.execute(sql, (key, key, key, key))
        rows = cursor.fetchall()
        cursor.close()
        if not rows:
            print("Không tìm thấy khách hàng.")
            return
        for row in rows:
            print(row)
    except Exception as e:
        print("Lỗi khi tìm kiếm khách hàng:", e)


def hien_thi_donhang():
    cursor = dtb.cursor()
    cursor.execute("SELECT madonhang, makhach, ngaymua, tinhtrang FROM tbdonhang")
    rows = cursor.fetchall()
    cursor.close()
    if not rows:
        print("Chưa có đơn hàng nào.")
        return
    for row in rows:
        print(row)

def them_donhang():
    try:
        madonhang = input("Nhập mã đơn hàng: ")
        makhach = input("Nhập mã khách hàng: ")
        ngaymua = input("Nhập ngày mua (YYYY-MM-DD): ")
        tinhtrang = input("Nhập tình trạng đơn hàng: ")

        dh = DonHang(madonhang, makhach, ngaymua, tinhtrang)

        cursor = dtb.cursor()
        sql = """
            INSERT INTO tbdonhang (madonhang, makhach, ngaymua, tinhtrang)
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(sql, dh.to_tuple())
        dtb.commit()
        cursor.close()
        print("Thêm đơn hàng thành công!")
    except Exception as e:
        print("Lỗi khi thêm đơn hàng:", e)

def sua_donhang():
    try:
        madonhang = input("Nhập mã đơn hàng cần sửa: ")
        makhach = input("Nhập mã khách hàng mới: ")
        ngaymua = input("Nhập ngày mua mới (YYYY-MM-DD): ")
        tinhtrang = input("Nhập tình trạng mới: ")

        cursor = dtb.cursor()
        sql = """
            UPDATE tbdonhang
            SET makhach = %s, ngaymua = %s, tinhtrang = %s
            WHERE madonhang = %s
        """
        cursor.execute(sql, (makhach, ngaymua, tinhtrang, madonhang))
        dtb.commit()
        if cursor.rowcount > 0:
            print("Sửa đơn hàng thành công!")
        else:
            print("Không tìm thấy mã đơn hàng cần sửa.")
        cursor.close()
    except Exception as e:
        print("Lỗi khi sửa đơn hàng:", e)

def xoa_donhang():
    try:
        madonhang = input("Nhập mã đơn hàng cần xoá: ")
        cursor = dtb.cursor()
        cursor.execute("DELETE FROM tbdonhang WHERE madonhang = %s", (madonhang,))
        dtb.commit()
        if cursor.rowcount > 0:
            print("Xoá đơn hàng thành công!")
        else:
            print("Không tìm thấy mã đơn hàng cần xoá.")
        cursor.close()
    except Exception as e:
        print("Lỗi khi xoá đơn hàng:", e)

def tim_kiem_donhang():
    try:
        tu_khoa = input("Nhập mã đơn hàng hoặc mã khách hàng cần tìm: ")
        cursor = dtb.cursor()
        sql = """
            SELECT madonhang, makhach, ngaymua, tinhtrang
            FROM tbdonhang
            WHERE madonhang LIKE %s OR makhach LIKE %s
        """
        key = f"%{tu_khoa}%"
        cursor.execute(sql, (key, key))
        rows = cursor.fetchall()
        cursor.close()
        if not rows:
            print("Không tìm thấy đơn hàng.")
            return
        for row in rows:
            print(row)
    except Exception as e:
        print("Lỗi khi tìm kiếm đơn hàng:", e)


def hien_thi_chitietdonhang():
    cursor = dtb.cursor()
    cursor.execute("SELECT machitiet, madonhang, mahang, soluong, dongia FROM tbchitietdonhang")
    rows = cursor.fetchall()
    cursor.close()
    if not rows:
        print("Chưa có chi tiết đơn hàng nào.")
        return
    for row in rows:
        print(row)

def them_chitietdonhang():
    try:
        machitiet = input("Nhập mã chi tiết đơn hàng: ")
        madonhang = input("Nhập mã đơn hàng: ")
        mahang = input("Nhập mã mặt hàng: ")
        soluong = int(input("Nhập số lượng: "))
        dongia = float(input("Nhập đơn gia: "))

        ctdh = ChiTietDonHang(machitiet, madonhang, mahang, soluong, dongia)

        cursor = dtb.cursor()
        sql = """
            INSERT INTO tbchitietdonhang (machitiet, madonhang, mahang, soluong, dongia)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(sql, ctdh.to_tuple())
        dtb.commit()
        cursor.close()
        print("Thêm chi tiết đơn hàng thành công!")
    except Exception as e:
        print("Lỗi khi thêm chi tiết đơn hàng:", e)

def sua_chitietdonhang():
    try:
        machitiet = input("Nhập mã chi tiết đơn hàng cần sửa: ")
        madonhang = input("Nhập mã đơn hàng mới: ")
        mahang = input("Nhập mã mặt hàng mới: ")
        soluong = int(input("Nhập số lượng mới: "))
        dongia = float(input("Nhập đơn giá mới: "))

        cursor = dtb.cursor()
        sql = """
            UPDATE tbchitietdonhang
            SET madonhang = %s, mahang = %s, soluong = %s, dongia = %s
            WHERE machitiet = %s
        """
        cursor.execute(sql, (madonhang, mahang, soluong, dongia, machitiet))
        dtb.commit()
        if cursor.rowcount > 0:
            print("Sửa chi tiết đơn hàng thành công!")
        else:
            print("Không tìm thấy mã chi tiết đơn hàng cần sửa.")
        cursor.close()
    except Exception as e:
        print("Lỗi khi sửa chi tiết đơn hàng:", e)

def xoa_chitietdonhang():
    try:
        machitiet = input("Nhập mã chi tiết đơn hàng cần xóa: ")
        cursor = dtb.cursor()
        cursor.execute("DELETE FROM tbchitietdonhang WHERE machitiet = %s", (machitiet,))
        dtb.commit()
        if cursor.rowcount > 0:
            print("Xóa chi tiết đơn hàng thành công!")
        else:
            print("Không tìm thấy mã chi tiết đơn hàng cần xóa.")
        cursor.close()
    except Exception as e:
        print("Lỗi khi xóa chi tiết đơn hàng:", e)

def tim_kiem_chitietdonhang():
    try:
        tu_khoa = input("Nhập mã chi tiết / mã đơn / mã hàng cần tìm: ")
        key = f"%{tu_khoa}%"
        cursor = dtb.cursor()
        sql = """
            SELECT machitiet, madonhang, mahang, soluong, dongia
            FROM tbchitietdonhang
            WHERE machitiet LIKE %s OR madonhang LIKE %s OR mahang LIKE %s
        """
        cursor.execute(sql, (key, key, key))
        rows = cursor.fetchall()
        cursor.close()
        if not rows:
            print("Không tìm thấy chi tiết đơn hàng.")
            return
        for row in rows:
            print(row)
    except Exception as e:
        print("Lỗi khi tìm kiếm chi tiết đơn hàng:", e)


def menu_mathang():
    while True:
        print("\n=== QUAN LY MAT HANG ===")
        print("1. Hien thi | 2. Them | 3. Sua | 4. Xoa | 5. Tim kiem | 0. Quay lai")
        choice = input("Nhap lua chon: ")
        if choice == "1":
            hien_thi_mathang()
        elif choice == "2":
            them_mathang()
        elif choice == "3":
            sua_mathang()
        elif choice == "4":
            xoa_mathang()
        elif choice == "5":
            tim_kiem_mathang()
        elif choice == "0":
            break
        else:
            print("Lua chon khong hop le.")

def menu_khachhang():
    while True:
        print("\n=== QUAN LY KHACH HANG ===")
        print("1. Hien thi | 2. Them | 3. Sua | 4. Xoa | 5. Tim kiem | 0. Quay lai")
        choice = input("Nhap lua chon: ")
        if choice == "1":
            hien_thi_khachhang()
        elif choice == "2":
            them_khachhang()
        elif choice == "3":
            sua_khachhang()
        elif choice == "4":
            xoa_khachhang()
        elif choice == "5":
            tim_kiem_khachhang()
        elif choice == "0":
            break
        else:
            print("Lua chon khong hop le.")

def menu_donhang():
    while True:
        print("\n=== QUAN LY DON HANG ===")
        print("1. Hien thi | 2. Them | 3. Sua | 4. Xoa | 5. Tim kiem | 0. Quay lai")
        choice = input("Nhap lua chon: ")
        if choice == "1":
            hien_thi_donhang()
        elif choice == "2":
            them_donhang()
        elif choice == "3":
            sua_donhang()
        elif choice == "4":
            xoa_donhang()
        elif choice == "5":
            tim_kiem_donhang()
        elif choice == "0":
            break
        else:
            print("Lua chon khong hop le.")

def menu_chitietdonhang():
    while True:
        print("\n=== QUAN LY CHI TIET DON HANG ===")
        print("1. Hien thi | 2. Them | 3. Sua | 4. Xoa | 5. Tim kiem | 0. Quay lai")
        choice = input("Nhap lua chon: ")
        if choice == "1":
            hien_thi_chitietdonhang()
        elif choice == "2":
            them_chitietdonhang()
        elif choice == "3":
            sua_chitietdonhang()
        elif choice == "4":
            xoa_chitietdonhang()
        elif choice == "5":
            tim_kiem_chitietdonhang()
        elif choice == "0":
            break
        else: print("Lua chon khong hop le.")

def main():
    while True:
        print("\n========== MENU CHINH ==========")
        print("1. Quan ly mat hang\n2. Quan ly khach hang\n3. Quan ly don hang\n4. Quan ly chi tiet don hang\n0. Thoat")
        choice = input("Nhap lua chon: ")
        if choice == "1":
            menu_mathang()
        elif choice == "2":
            menu_khachhang()
        elif choice == "3":
            menu_donhang()
        elif choice == "4":
            menu_chitietdonhang()
        elif choice == "0":
            print("Tam biet!")
            break
        else:
            print("Lua chon khong hop le.")

if __name__ == "__main__":
    main()