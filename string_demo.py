# Bài 1: Nhập vào một chuỗi gồm các chữ số cách nhau bằng dấu phẩy (vd: “1,2,3,4,5,6,7”)
# sau đó tìm các số nguyên tố trong danh sách các chữ số đã nhập
import math
import os
from os import read


def checksont(n):
    for i in range(2,int(math.sqrt(n) + 1)):
        if(n % i == 0):
            return False
    return True

f_read = open("test_file.txt", "r")
_string1 = f_read.read()
f_read.close()

tachchuoi = _string1.split(",")

temp = []
for i in tachchuoi:
    if checksont(int(i)):
        temp.append(int(i))

f_write = open("checksonguyento.txt", "w")

inradanhsach = ",".join(map(str, temp))
f_write.write(inradanhsach)
f_write.close()

