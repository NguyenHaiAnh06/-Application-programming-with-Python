from abc import ABC,abstractmethod
import math

class Hinhhoc(ABC):
    def __init__(self,name):
        self.__name = name

    def chuvi(self):
        pass

    def dientich(self):
       pass

    def hienthi(self):
        return self.__name


class hinhtron(Hinhhoc):
    def __init__(self,name,r):
        super().__init__(name)
        self.bankinh = r

    def chuvi(self):
        return math.pi *  self.bankinh * 2

    def dientich(self):
        return  math.pi *  self.bankinh ** 2

class Hinh_chu_nhat(Hinhhoc):
    def __init__(self,name,chieudai, chieurong):
       super().__init__(name)
       self.chieudai = chieudai
       self.chieurong = chieurong

    def chuvi(self):
        return (self.chieudai + self.chieurong) * 2

    def dientich(self):
        return self.chieudai * self.chieurong

# _test = hinhtron("hinhtron",30)
# print(_test.chuvi(),_test.dientich())
# print("\n")
# _test2 = Hinh_chu_nhat("HCN",10,20)
# print(_test2.dientich(),_test2.chuvi(),_test2.hienthi())

class main:
    h1 = Hinh_chu_nhat("HCNhat",20 , 10)
    print(h1.hienthi(),h1.chuvi() , h1.dientich())

main()