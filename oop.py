class sinhvien:
    def __init__(self, hoten = ' ' ,masinhvien = 2502,email = '',address = 'Hanoi',lop = 'Cs2'):
        self.hoten = hoten
        self.masinhvien = masinhvien
        self.email = email
        self.address = address
        self.lop = lop

    def show_infor(self):
        print(self.hoten)
        print(self.masinhvien)
        print(self.email)
        print(self.address)
        print(self.lop)

    def __str__(self):
        return self.hoten

    def change_infor(self,address ='Hanoi',lop = 'Cs2'):
        self.address = address
        self.lop = lop


print("---khai bao thong tin---")
sv1 = sinhvien('Nguyen Hai Anh',25020000,'Haianh.0106@gmal.com','Hanoi','cs2')
sv2 = sinhvien('Hello moi nguoi','20029999','test@gmail.com','Hanoi','Cs2')

sv1.show_infor()
print("\n")
sv2.show_infor()

print("\n")
#phuong thuc dac biet trong py cua __str__
print(sv1)
print(sv2)
print("\n")
#thay doi thong tin
sv1.change_infor('Tp.HCM','Cs5')
sv2.change_infor('Danang','Cs6')

sv1.show_infor()
print("\n")
sv2.show_infor()



