from abc import ABC, abstractmethod


class Nhanvien(ABC):
    def __init__(self, mnv, hoten, luongcoban):
        self.manhanvien = mnv
        self.name = hoten
        self.__luong = luongcoban

    @abstractmethod
    def tinh_luong(self):
        pass

    def xemluong(self):
        return self.__luong


class luong_van_phong(Nhanvien):
    def __init__(self, mnv, hoten, luongcoban, songaycong):
        super().__init__(mnv, hoten, luongcoban)
        self.songaycong = songaycong

    def tinh_luong(self):
        return self.xemluong() + (self.songaycong * 200000)


class nhan_vien_ban_hang(Nhanvien):
    def __init__(self, mnv, hoten, luongcoban, doanh_so, tl_hoahong):
        super().__init__(mnv, hoten, luongcoban)
        self.doanhso = doanh_so
        self.tilehoahong = tl_hoahong

    def tinh_luong(self):
        return self.xemluong() + (self.doanhso * self.tilehoahong)


def main():
    n = int(input())
    a = []
    for i in range(n):
        print("Nhap ma nhan vien va ho ten + luong co ban")
        mnv = input()
        hoten = input()
        luongcoban = int(input())

        try:
            print('1 de chon nvvp , 2 de chon nv ban hang')
            choice = input()

            if choice == '1':
                print("Da chon nvvp nhap vao so ngay cong")
                songaycong = int(input())
                nv = luong_van_phong(mnv, hoten, luongcoban, songaycong)
                a.append(nv)

            elif choice == '2':
                print("Da chon nvbh nhap vao doanh so va ti le hoa hong")
                doanhso = float(input())
                tilehoahong = float(input())
                nv = nhan_vien_ban_hang(mnv, hoten, luongcoban, doanhso, tilehoahong)
                a.append(nv)

            else:
                raise ValueError

        except ValueError as e:
            print(f" lỗi: Khách hàng nhập sai kiểu dữ liệu số hoặc {e}")

        finally:
            print(f"lượt nhập thứ {i + 1}\n")

    for duyetnv in a:
        print(f'{duyetnv.manhanvien}\n{duyetnv.name}\n{duyetnv.xemluong()}\n{duyetnv.tinh_luong()}\n')

    for ktrluong in a:
        okk = ktrluong.tinh_luong()
        if 10000000 <= okk <= 20000000:
            print(f'Thỏa mãn\n{ktrluong.manhanvien}\n{ktrluong.name}\n{okk}\n')

if __name__ == "__main__":
    main()