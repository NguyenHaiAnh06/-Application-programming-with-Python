# Bài 1: Đọc vào một file văn bản, tính tần suất xuất hiện của mỗi
# từ trong văn bản đó (kết quả trả về là 1 từ điển gồm Key là các
# từ và Value là tần suất xuất hiện của từ đó)

import os

f_read = open("test_file.txt")
_write = f_read.read()
f_read.close()

khoi_tao = {}

temp = _write.lower().split()
for i in temp:
    if i in  khoi_tao:
        khoi_tao[i] = khoi_tao[i] + 1
    else:
        khoi_tao[i] = 1

for i in khoi_tao:
    print(f'"{i}" : "{khoi_tao[i]}"')
