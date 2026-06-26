# Nhập vào một danh sách các số nguyên
# Loại bỏ các số lẻ trong danh sách ban đầu
# Tách riêng thành danh sách số dương (L1) và danh sách số âm (L2)
# Sắp xếp danh sách L1 tăng dần, danh sách L2 giảm dần
# Thêm số 0 vào đầu danh sách L1 và vào cuối danh sách L2
# Nối L1 và L2 theo thứ tự L2 trước, L1 sau
#Tìm các số nguyên tố trong _t2(viết function riêng để kiểm tra số nguyên tố)

#Nhập vào 1 danh sách
n = int(input("nhập vào số lượng phần tử: "))
_danhsach = []
for i in range(0,n):
    x = int(input(f'phần tử {i}: '))
    _danhsach.append(x)

print("danh sách đã nhập: ", _danhsach)

#chuyển thành tuple _t1
_t1 = tuple(_danhsach)

#Loại bỏ các số lẻ trong tuple _t1 ban đầu
_dsChan = [x for x in _t1 if x%2==0]

print("danh sách chẵn: ", _dsChan)

#Tách riêng thành danh sách số dương (L1) và danh sách số âm (L2)
_l1 = [x for x in _t1 if x>0]
_l2 = [x for x in _t1 if x<0]

print("danh sách số dương: ", _l1)
print("danh sách số âm: ", _l2)

#Sắp xếp danh sách L1 tăng dần, danh sách L2 giảm dần
_l1.sort()
_l2.sort(reverse=True)

print("sắp xếp danh sách số dương: ", _l1)
print("sắp xếp danh sách số âm: ", _l2)


_l1.insert(0,0)
_l2.insert(0,0)

print("sau khi nối 0 vào đầu list _l1",_l1)
print("sau khi nối 0 vào đầu list _l2",_l2)
