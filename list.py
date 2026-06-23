# List Comprehension
_list = [1,2,3,4,5,6,7,8,9]
even_list = [num for num in _list if num % 2 == 0]
add_list =  [num for num in _list if num % 2 != 0]
print(even_list)
print(add_list)

# Slicing (cắt list)
_list2 = ['red' , 'green' , 'white' ,'black','pink','yellow']
_new = _list2[2:4]
print(_new)

# insert
_list3 = ['zero' , 'three']
_new3 = _list3.copy()
_new3[1:1] = ['one', 'two']
print(_new3)