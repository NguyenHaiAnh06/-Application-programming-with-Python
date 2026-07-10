import sqlite3
from os.path import curdir

check = "/Users/nguyenhaianh/Documents/dattabase.db"
_conect = sqlite3.connect(check)

# tao doi tuong ket noi
pointer = _conect.cursor()

# cau lenh sql
sql = "select * from sinhvien"
pointer.execute(sql) # lenh thuc thi


test = "update sinhvien set scoreTb =scoreTb + 1"
pointer.execute(test)
_conect.commit()
pointer.close()

# _result = pointer.fetchall()
# print(f'{_result}\n')