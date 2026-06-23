import math
#bai tap lam quen voi python
def _sum(a,b):
    return a + b

def check_so_nguyen_to(n):
    for i in range(2,int(math.sqrt(n)+1)):
        if(n % i == 0):
            return False
    
    return True

def check_trong_khoang(a,b):
    for i in range(a,b+1):
        if check_so_nguyen_to(i):
          print(f'{i} la so nguyen to')

def so_hoan_hao(x):
    tong_uoc = 0
    for i in range(1,x):
        if x % i == 0:
            tong_uoc += i
    return tong_uoc == x

print("1: tinh tong")
print("2:check so nguyen to")
print("3:check so nguyen to trong khoang a-b")
print("4:ktr xem co phai so hoan hao ko")

choice = int(input())

if choice == 1:
    print("nhap a va b de tinh tong")
    a = int(input())
    b = int(input())
    print(_sum(a,b))
elif choice == 2:
    print("nhap so can check")
    x = int(input())
    test = check_so_nguyen_to(x)
    if test == True:
        print("la so nguyen to")
    else:
        print("Ko phai la so nguyen to")
elif choice == 3:
    print("check trong khoang a->b")
    a = int(input())
    b = int(input())
    c = check_trong_khoang(a,b)
    print(c)
elif choice == 4:
    print("check so hoan hao")
    x = int(input())
    z = so_hoan_hao(x)
    if z == True:
        print("la so hoan hao")
    else:
        print("ko phai so hoan hao roi")
exit