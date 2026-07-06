from abc import ABC , abstractmethod

class Nhanvien(ABC):
    def __init__(self,mnv,hoten,luongcoban):
        self.manhanvien = mnv
        self.name = hoten
        self.__luong=luongcoban

    @abstractmethod
    def tinh_luong(self):
        pass

    def xemluong(self):
        return self.__luong


class luong_van_phong(Nhanvien):
    def __init__(self,songaycong,mnv,hoten,luongcoban):
        super().__init__(mnv,hoten,luongcoban)
        self.songaycong=songaycong

    def tinh_luong(self):
        return self.xemluong() + (self.songaycong * 200000)


class nhan_vien_ban_hang(Nhanvien):
    def __init__(self,doanh_so,tl_hoahong,mnv,hoten,luongcoban):
       super().__init__(mnv,hoten,luongcoban)
       self.doanhso = doanh_so
       self.tilehoahong = tl_hoahong

    def tinh_luong(self):
        return self.xemluong() + (self.doanhso * self.tilehoahong)

def main():
    n = int(input())
    a =[]
    for i in range(n):
        print("Nhap ma nhan vien va ho ten + luong co ban")
        mnv = input()
        hoten = input()
        luongcoban = int(input())
        print('1 de chon nvvp , 2 de chon nv ban hang')
        choice = input()
        if choice == '1':
            print("Da chon nvvp nhap vao so ngay cong")
            songaycong = int(input())
            nvvp = luong_van_phong(songaycong,mnv,hoten,luongcoban)
            a.append(nvvp)
        elif choice == '2':
            print("Da chon nvvp nhap vao doanh so va ti le hoa hong")
            doanhso = input()
            tilehoahong = input()
            nvbn = nhan_vien_ban_hang(doanhso,tilehoahong,mnv,hoten,luongcoban)
            a.append(nvbn)
        else:
            print('lua chon sai mac dinh nvvp so cong = 0')
            nvvp = luong_van_phong(0,mnv,hoten,luongcoban)
            a.append(nvvp)

    for duyetnv in a:
         print(f'{duyetnv.manhanvien}{duyetnv.name}{duyetnv.xemluong()}{duyetnv.tinh_luong()}')

main()
