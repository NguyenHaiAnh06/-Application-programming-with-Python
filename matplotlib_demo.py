from cProfile import label
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import markers, colors
from matplotlib.lines import lineStyles

# Dữ liệu trục X và Y
x = np.arange(1,10,1)
y = x**2

# Vẽ biểu đồ đường
plt.subplot(1,2,1)
plt.xlabel('cot x')
plt.ylabel('hang y')
plt.plot(x,y,label='y = x^2',marker = 'o',color = 'b',linestyle = '-')
plt.legend() # hien thi lable
# Hiển thị lưới
plt.grid(True)

plt.show()
