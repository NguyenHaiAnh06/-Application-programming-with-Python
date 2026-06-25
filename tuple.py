# Tuple (bộ dữ liệu) là một dãy (sequence) các giá trị, nó chứa nhiều 
# phần tử (element), về cơ bản nó khá giống với List (danh sách).

# Bài tap: Viết chương trình loại bỏ các phần tử có giá trị giống nhau 
# trong một tuple, để tạo 1 tuple mới. Ví dụ: nhập vào _tuple = (‘ab’, 
# ‘b’, ‘e’, ‘c’, ‘d’, ‘e’, ‘ab’), thì thu được _new_tuple = (‘b’, ‘c’, ‘d’,'e','ab').

tuple1 = ('ab','b','e','c','d','e','ab')
update = list(tuple1)

for i in update:
      while i in update:
         if update.count(i) == 1:
            break
         else :
            update.remove(i)
epkieu = tuple(update)
print(epkieu)
