def chia(a,b):
    try:
        x = int(a)
        y = int(b)
        z = x / y
        print(z)
    except ValueError as e1:
        print("Loi truyen du lieu")
    except ValueError as e2:
        print("loi chia cho 0")
    except ValueError as e3:
        print("Ctrinh co loi")
    finally:
        print("Ket thuc chuong trinh")


a = input()
b = input()
chia(a,b)
