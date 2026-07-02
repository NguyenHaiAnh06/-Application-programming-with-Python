from my_module import _fibonaci
from my_module import _factorial

n = int(input())
for i in range(n):
    print(_fibonaci.fibonaci(i))

print(_factorial.factorial(n))
