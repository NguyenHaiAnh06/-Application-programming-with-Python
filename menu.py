# Tạo class tương đương struct TIVI
class TIVI:
    def __init__(self, ten="", hang="", nam=0):
        self.tenTIVI = ten
        self.hangSanXuat = hang
        self.namsanxuat = nam


def main():
    n = 3
    tv = [TIVI() for _ in range(n)]

    while True:
        print("========== Menu ===============")
        print("1. Nhap cac thong tin tivi")
        print("2. In cac thong tin cac tivi")
        print("3. Cac tivi san xuat truoc 2020")
        print("4. Cac tivi san xuat nam 2020 tro len")
        print("0. Thoat")

        choice = int(input("Lua chon cua ban: "))

        if choice == 1:
            for i in range(n):
                print(f"Tivi thu {i+1} la:")
                tv[i].tenTIVI = input("Ten tivi: ")
                tv[i].hangSanXuat = input("Hang san xuat: ")
                tv[i].namsanxuat = int(input("Nam san xuat: "))

        elif choice == 2:
            print("\nThong tin cua cac tivi la:")
            for i in range(n):
                print(f"\nTen tivi: {tv[i].tenTIVI}")
                print(f"Hang san xuat: {tv[i].hangSanXuat}")
                print(f"Nam san xuat: {tv[i].namsanxuat}")

        elif choice == 3:
            print("\nCac tivi san xuat truoc 2020:")
            for i in range(n):
                if tv[i].namsanxuat < 2020:
                    print(f"\nTen tivi: {tv[i].tenTIVI}")
                    print(f"Hang san xuat: {tv[i].hangSanXuat}")
                    print(f"Nam san xuat: {tv[i].namsanxuat}")

        elif choice == 4:
            print("\nCac tivi san xuat tu 2020 tro len:")
            for i in range(n):
                if tv[i].namsanxuat >= 2020:
                    print(f"\nTen tivi: {tv[i].tenTIVI}")
                    print(f"Hang san xuat: {tv[i].hangSanXuat}")
                    print(f"Nam san xuat: {tv[i].namsanxuat}")

        elif choice == 0:
            print("Chuong trinh ket thuc")
            break

        else:
            print("Vui long chon so hop le!")


if __name__ == "__main__":
    main()
