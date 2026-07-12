from abc import ABC
from db import _poiter

class mathang:
    def __init__(self,mahang,tenhang,nguongoc,giatien,soluong):
        self._mahang = mahang
        self.tenhang = tenhang
        self.nguongoc = nguongoc
        self.giatien = giatien
        self.soluong = soluong

    def get_mahang(self): #ghi de
        return self._mahang

    def get_tenhang(self):
        return self._tenhang

    def get_nguongoc(self):
        return self._nguongoc

    def get_giatien(self):
        return self._giatien

    def get_soluong(self):
        return self._soluong

    def set_tenhang(self, tenhang):
        self._tenhang = tenhang

    def set_nguongoc(self, nguongoc):
        self._nguongoc = nguongoc

    def set_giatien(self, giatien):
        self._giatien = giatien

    def set_soluong(self, soluong):
        self._soluong = soluong

    def to_tuple(self):
        return (self._mahang , self.tenhang , self.nguongoc , self.giatien , self.soluong)

    def __str__(self):
        return f'{self._mahang} | {self.tenhang} | {self.nguongoc} | {self.giatien} | {self.soluong}'

class KhachHang:
    def __init__(self, makh, tenkh, diachi, sdt):
        self._makh = makh
        self.tenkh = tenkh
        self._diachi = diachi
        self._sdt = sdt

    def get_makh(self):
        return self._makh

    def get_tenkh(self):
        return self.tenkh

    def get_diachi(self):
        return self._diachi

    def get_sdt(self):
        return self._sdt

    def set_tenkh(self, tenkh):
        self._tenkh = tenkh

    def set_diachi(self, diachi):
        self._diachi = diachi

    def set_sdt(self, sdt):
        self._sdt = sdt

    def to_tuple(self):
        return (self._makh, self._tenkh, self._diachi, self._sdt)

    def __str__(self):
        return f"{self._makh} | {self._tenkh} | {self._diachi} | {self._sdt}"

class DonHang:
    def __init__(self, madh, makh, ngaylap, tongtien):
        self._madh = madh
        self._makh = makh
        self._ngaylap = ngaylap
        self._tongtien = tongtien

    def get_madh(self):
        return self._madh

    def get_makh(self):
        return self._makh

    def get_ngaylap(self):
        return self._ngaylap

    def get_tongtien(self):
        return self._tongtien

    def set_makh(self, makh):
        self._makh = makh

    def set_ngaylap(self, ngaylap):
        self._ngaylap = ngaylap

    def set_tongtien(self, tongtien):
        self._tongtien = tongtien

    def to_tuple(self):
        return (self._madh, self._makh, self._ngaylap, self._tongtien)

    def __str__(self):
        return f"{self._madh} | {self._makh} | {self._ngaylap} | {self._tongtien}"

class ChiTietDonHang:
    def __init__(self, mactdh, madh, mahang, soluong, dongia):
        self._mactdh = mactdh
        self._madh = madh
        self._mahang = mahang
        self._soluong = soluong
        self._dongia = dongia
        self._thanhtien = soluong * dongia

    def get_mactdh(self):
        return self._mactdh

    def get_madh(self):
        return self._madh

    def get_mahang(self):
        return self._mahang

    def get_soluong(self):
        return self._soluong

    def get_dongia(self):
        return self._dongia

    def get_thanhtien(self):
        return self._thanhtien

    def set_soluong(self, soluong):
        self._soluong = soluong
        self._thanhtien = self._soluong * self._dongia

    def set_dongia(self, dongia):
        self._dongia = dongia
        self._thanhtien = self._soluong * self._dongia

    def to_tuple(self):
        return (self._mactdh, self._madh, self._mahang, self._soluong, self._dongia, self._thanhtien)

    def __str__(self):
        return f"{self._mactdh} | {self._madh} | {self._mahang} | {self._soluong} | {self._dongia} | {self._thanhtien}"


def hien_thi_mathang():
    cursor = _poiter.cursor()
    cursor.execute("SELECT mahang, tenhang, nguongoc, giatien, soluong FROM mathang")
    rows = cursor.fetchall()

    if not rows:
        print("Chưa có mặt hàng nào.")
        return

    for row in rows:
        print(row)

def them_mathang():
    try:
        mahang = input("Nhập mã hàng: ")
        tenhang = input("Nhập tên hàng: ")
        nguongoc = input("Nhập nguồn gốc: ")
        giatien = float(input("Nhập giá tiền: "))
        soluong = int(input("Nhập số lượng: "))

        mh = mathang(mahang, tenhang, nguongoc, giatien, soluong)

        cursor = _poiter.cursor()
        sql = """
            INSERT INTO mathang (mahang, tenhang, nguongoc, giatien, soluong)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(sql, mh.to_tuple())
        _poiter.commit()

        print("Thêm mặt hàng thành công!")

    except Exception as e:
        print("Lỗi khi thêm mặt hàng:", e)

def sua_mathang():
    try:
        mahang = input("Nhập mã hàng cần sửa: ")

        tenhang = input("Nhập tên hàng mới: ")
        nguongoc = input("Nhập nguồn gốc mới: ")
        giatien = float(input("Nhập giá tiền mới: "))
        soluong = int(input("Nhập số lượng mới: "))

        cursor = _poiter.cursor()
        sql = """
            UPDATE mathang
            SET tenhang = %s, nguongoc = %s, giatien = %s, soluong = %s
            WHERE mahang = %s
        """
        cursor.execute(sql, (tenhang, nguongoc, giatien, soluong, mahang))
        _poiter.commit()

        if cursor.rowcount > 0:
            print("Sửa mặt hàng thành công!")
        else:
            print("Không tìm thấy mã hàng cần sửa.")

    except Exception as e:
        print("Lỗi khi sửa mặt hàng:", e)

def xoa_mathang():
    try:
        mahang = input("Nhập mã hàng cần xoá: ")

        cursor = _poiter.cursor()
        cursor.execute("DELETE FROM mathang WHERE mahang = %s", (mahang,))
        _poiter.commit()

        if cursor.rowcount > 0:
            print("Xoá mặt hàng thành công!")
        else:
            print("Không tìm thấy mã hàng cần xoá.")

    except Exception as e:
        print("Lỗi khi xoá mặt hàng:", e)

def tim_kiem_mathang():
    try:
        tu_khoa = input("Nhập mã/tên/nguồn gốc cần tìm: ")

        cursor = _poiter.cursor()
        sql = """
            SELECT mahang, tenhang, nguongoc, giatien, soluong
            FROM mathang
            WHERE mahang LIKE %s
               OR tenhang LIKE %s
               OR nguongoc LIKE %s
        """
        key = f"%{tu_khoa}%"
        cursor.execute(sql, (key, key, key))
        rows = cursor.fetchall()

        if not rows:
            print("Không tìm thấy mặt hàng.")
            return

        for row in rows:
            print(row)

    except Exception as e:
        print("Lỗi khi tìm kiếm mặt hàng:", e)

def hien_thi_donhang():
    cursor = _poiter.cursor()
    cursor.execute("SELECT madh, makh, ngaylap, tongtien FROM donhang")
    rows = cursor.fetchall()

    if not rows:
        print("Chưa có đơn hàng nào.")
        return

    for row in rows:
        print(row)

def them_donhang():
    try:
        madh = input("Nhập mã đơn hàng: ")
        makh = input("Nhập mã khách hàng: ")
        ngaylap = input("Nhập ngày lập (YYYY-MM-DD): ")
        tongtien = float(input("Nhập tổng tiền: "))

        dh = DonHang(madh, makh, ngaylap, tongtien)

        cursor = _poiter.cursor()
        sql = """
            INSERT INTO donhang (madh, makh, ngaylap, tongtien)
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(sql, dh.to_tuple())
        _poiter.commit()

        print("Thêm đơn hàng thành công!")

    except Exception as e:
        print("Lỗi khi thêm đơn hàng:", e)

def sua_donhang():
    try:
        madh = input("Nhập mã đơn hàng cần sửa: ")
        makh = input("Nhập mã khách hàng mới: ")
        ngaylap = input("Nhập ngày lập mới (YYYY-MM-DD): ")
        tongtien = float(input("Nhập tổng tiền mới: "))

        cursor = _poiter.cursor()
        sql = """
            UPDATE donhang
            SET makh = %s, ngaylap = %s, tongtien = %s
            WHERE madh = %s
        """
        cursor.execute(sql, (makh, ngaylap, tongtien, madh))
        _poiter.commit()

        if cursor.rowcount > 0:
            print("Sửa đơn hàng thành công!")
        else:
            print("Không tìm thấy mã đơn hàng cần sửa.")

    except Exception as e:
        print("Lỗi khi sửa đơn hàng:", e)

def xoa_donhang():
    try:
        madh = input("Nhập mã đơn hàng cần xoá: ")

        cursor = _poiter.cursor()
        cursor.execute("DELETE FROM donhang WHERE madh = %s", (madh,))
        _poiter.commit()

        if cursor.rowcount > 0:
            print("Xoá đơn hàng thành công!")
        else:
            print("Không tìm thấy mã đơn hàng cần xoá.")

    except Exception as e:
        print("Lỗi khi xoá đơn hàng:", e)

def tim_kiem_donhang():
    try:
        tu_khoa = input("Nhập mã đơn hàng hoặc mã khách hàng cần tìm: ")

        cursor = _poiter.cursor()
        sql = """
            SELECT madh, makh, ngaylap, tongtien
            FROM donhang
            WHERE madh LIKE %s
               OR makh LIKE %s
        """
        key = f"%{tu_khoa}%"
        cursor.execute(sql, (key, key))
        rows = cursor.fetchall()

        if not rows:
            print("Không tìm thấy đơn hàng.")
            return

        for row in rows:
            print(row)

    except Exception as e:
        print("Lỗi khi tìm kiếm đơn hàng:", e)

def hien_thi_khachhang():
    cursor =_poiter.cursor()
    cursor.execute("SELECT makh, tenkh, diachi, sdt FROM khachhang")
    rows = cursor.fetchall()

    if not rows:
        print("Chua co khach hang nao.")
        return

    for row in rows:
        print(row)


def them_khachhang():
    try:
        makh = input("Nhap ma khach hang: ")
        tenkh = input("Nhap ten khach hang: ")
        diachi = input("Nhap dia chi: ")
        sdt = input("Nhap so dien thoai: ")

        kh = KhachHang(makh, tenkh, diachi, sdt)

        cursor = _poiter.cursor()
        sql = """
            INSERT INTO khachhang (makh, tenkh, diachi, sdt)
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(sql, kh.to_tuple())
        _poiter.commit()

        print("Them khach hang thanh cong!")
    except Exception as e:
        print("Loi khi them khach hang:", e)


def sua_khachhang():
    try:
        makh = input("Nhap ma khach hang can sua: ")

        tenkh = input("Nhap ten khach hang moi: ")
        diachi = input("Nhap dia chi moi: ")
        sdt = input("Nhap so dien thoai moi: ")

        cursor = _poiter.cursor()
        sql = """
            UPDATE khachhang
            SET tenkh = %s, diachi = %s, sdt = %s
            WHERE makh = %s
        """
        cursor.execute(sql, (tenkh, diachi, sdt, makh))
        _poiter.commit()

        if cursor.rowcount > 0:
            print("Sua khach hang thanh cong!")
        else:
            print("Khong tim thay ma khach hang can sua.")
    except Exception as e:
        print("Loi khi sua khach hang:", e)


def xoa_khachhang():
    try:
        makh = input("Nhap ma khach hang can xoa: ")

        cursor = _poiter.cursor()
        cursor.execute("DELETE FROM khachhang WHERE makh = %s", (makh,))
        _poiter.commit()

        if cursor.rowcount > 0:
            print("Xoa khach hang thanh cong!")
        else:
            print("Khong tim thay ma khach hang can xoa.")
    except Exception as e:
        print("Loi khi xoa khach hang:", e)


def tim_kiem_khachhang():
    try:
        tu_khoa = input("Nhap ma/ten/dia chi/sdt can tim: ")
        key = f"%{tu_khoa}%"

        cursor = _poiter.cursor()
        sql = """
            SELECT makh, tenkh, diachi, sdt
            FROM khachhang
            WHERE makh LIKE %s
               OR tenkh LIKE %s
               OR diachi LIKE %s
               OR sdt LIKE %s
        """
        cursor.execute(sql, (key, key, key, key))
        rows = cursor.fetchall()

        if not rows:
            print("Khong tim thay khach hang.")
            return

        for row in rows:
            print(row)
    except Exception as e:
        print("Loi khi tim kiem khach hang:", e)

def hien_thi_chitietdonhang():
    cursor = _poiter.cursor()
    cursor.execute("""
        SELECT mactdh, madh, mahang, soluong, dongia, thanhtien
        FROM chitietdonhang
    """)
    rows = cursor.fetchall()

    if not rows:
        print("Chua co chi tiet don hang nao.")
        return

    for row in rows:
        print(row)


def them_chitietdonhang():
    try:
        mactdh = input("Nhap ma chi tiet don hang: ")
        madh = input("Nhap ma don hang: ")
        mahang = input("Nhap ma mat hang: ")
        soluong = int(input("Nhap so luong: "))
        dongia = float(input("Nhap don gia: "))

        ctdh = ChiTietDonHang(mactdh, madh, mahang, soluong, dongia)

        cursor = _poiter.cursor()
        sql = """
            INSERT INTO chitietdonhang
            (mactdh, madh, mahang, soluong, dongia, thanhtien)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(sql, ctdh.to_tuple())
        _poiter.commit()

        print("Them chi tiet don hang thanh cong!")
    except Exception as e:
        print("Loi khi them chi tiet don hang:", e)


def sua_chitietdonhang():
    try:
        mactdh = input("Nhap ma chi tiet don hang can sua: ")

        madh = input("Nhap ma don hang moi: ")
        mahang = input("Nhap ma mat hang moi: ")
        soluong = int(input("Nhap so luong moi: "))
        dongia = float(input("Nhap don gia moi: "))
        thanhtien = soluong * dongia

        cursor = _poiter.cursor()
        sql = """
            UPDATE chitietdonhang
            SET madh = %s, mahang = %s, soluong = %s, dongia = %s, thanhtien = %s
            WHERE mactdh = %s
        """
        cursor.execute(sql, (madh, mahang, soluong, dongia, thanhtien, mactdh))
        _poiter.commit()

        if cursor.rowcount > 0:
            print("Sua chi tiet don hang thanh cong!")
        else:
            print("Khong tim thay ma chi tiet don hang can sua.")
    except Exception as e:
        print("Loi khi sua chi tiet don hang:", e)


def xoa_chitietdonhang():
    try:
        mactdh = input("Nhap ma chi tiet don hang can xoa: ")

        cursor = _poiter.cursor()
        cursor.execute("DELETE FROM chitietdonhang WHERE mactdh = %s", (mactdh,))
        _poiter.commit()

        if cursor.rowcount > 0:
            print("Xoa chi tiet don hang thanh cong!")
        else:
            print("Khong tim thay ma chi tiet don hang can xoa.")
    except Exception as e:
        print("Loi khi xoa chi tiet don hang:", e)


def tim_kiem_chitietdonhang():
    try:
        tu_khoa = input("Nhap ma chi tiet / ma don / ma hang can tim: ")
        key = f"%{tu_khoa}%"

        cursor = _poiter.cursor()
        sql = """
            SELECT mactdh, madh, mahang, soluong, dongia, thanhtien
            FROM chitietdonhang
            WHERE mactdh LIKE %s
               OR madh LIKE %s
               OR mahang LIKE %s
        """
        cursor.execute(sql, (key, key, key))
        rows = cursor.fetchall()

        if not rows:
            print("Khong tim thay chi tiet don hang.")
            return

        for row in rows:
            print(row)
    except Exception as e:
        print("Loi khi tim kiem chi tiet don hang:", e)

def menu_mathang():
    while True:
        print("\n=== QUAN LY MAT HANG ===")
        print("1. Hien thi")
        print("2. Them")
        print("3. Sua")
        print("4. Xoa")
        print("5. Tim kiem")
        print("0. Quay lai")

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
        print("1. Hien thi")
        print("2. Them")
        print("3. Sua")
        print("4. Xoa")
        print("5. Tim kiem")
        print("0. Quay lai")

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
        print("1. Hien thi")
        print("2. Them")
        print("3. Sua")
        print("4. Xoa")
        print("5. Tim kiem")
        print("0. Quay lai")

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
        print("1. Hien thi")
        print("2. Them")
        print("3. Sua")
        print("4. Xoa")
        print("5. Tim kiem")
        print("0. Quay lai")

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
        else:
            print("Lua chon khong hop le.")


def main():
    while True:
        print("\n========== MENU CHINH ==========")
        print("1. Quan ly mat hang")
        print("2. Quan ly khach hang")
        print("3. Quan ly don hang")
        print("4. Quan ly chi tiet don hang")
        print("0. Thoat")

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