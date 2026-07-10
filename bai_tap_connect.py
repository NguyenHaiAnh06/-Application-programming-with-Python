import sqlite3

def priketqua(x):
    for item in x:
        print(item)

ketnoi = "/Users/nguyenhaianh/Documents/dattabase.db"
taoketnoi = sqlite3.connect(ketnoi)

_lay = taoketnoi.cursor()

_lay.execute("drop table if exists lop_hoc")

data ="""
create table lop_hoc(
    ma_lop text(50) not null primary key,
    ten_lop text(50) null default null
);
"""
them = """
insert into lop_hoc(ma_lop,ten_lop)
values("Python","lập trình python mobile"),
      ("Java","lập trình nâng cao");
"""

_lay.execute(data)
_lay.execute(them)

taoketnoi.commit() # update cho database
_lay.close()
taoketnoi.close()