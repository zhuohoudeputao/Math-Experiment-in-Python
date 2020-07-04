'''
@Author: zhuohoudeputao
@LastEditors: zhuohoudeputao
@LastEditTime: 2020-07-04 23:26:59
@Description: a_{n+1}=a_{n}+1/a_{n}, a_0=1
'''

import numpy as np
import matplotlib.pyplot as plt
a = [1]
n = 100
for i in range(n):
    a.append(a[-1]+1/a[-1])
x = list(range(len(a)))
plt.plot(x, a)
plt.show()

a = np.array(a)
plt.plot(x, a ** 2)
plt.show()

y = a**2
p = np.polyfit(x, y, 1)
print(p)
plt.scatter(x, y, c='g', label="before fitting", linewidths=0.01)
plt.plot(x, np.polyval(p, x), "b--", label="after fitting")
plt.legend()
plt.show()
