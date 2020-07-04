'''
@Author: zhuohoudeputao
@LastEditors: zhuohoudeputao
@LastEditTime: 2020-07-04 23:05:41
@Description: Use subplot to plot curves
'''
import matplotlib.pyplot as plt
import numpy as np

# %% [markdown]
# # Use subplot to plot curves
# 1. $f(x)=x^3+2x^2-3x+4$ <br>
# 2. $r=cos2\theta$ <br>
# 3. $x=(1+sint-2cos4t)cost,~y=(1+sint-2cos4t)sint$ <br>
# 4. $y=sinx+sin2x$ <br>

# %%
x = np.arange(-5, 5, 0.01)
y = np.power(x, 3) + 2 * np.power(x, 2) - 3 * x + 4
plt.subplot(221)
plt.plot(x, y)
plt.title("$f(x)=x^3+2x^2-3x+4$")

theta = np.arange(0, 4*np.pi, 0.01)
r = np.cos(2 * theta)
plt.subplot(222, projection="polar")
plt.polar(theta, r)
plt.title("$r=cos2\\theta$")

t = np.arange(0, 2 * np.pi, 0.01)
x = (1 + np.sin(t) - 2 * np.cos(4 * t)) * np.cos(t)
y = (1 + np.sin(t) - 2 * np.cos(4 * t)) * np.sin(t)
plt.subplot(223)
plt.plot(x, y)
plt.title("$x=(1+sint-2cos4t)cost, y=(1+sint-2cos4t)sint$")

x = np.arange(-5, 5, 0.01)
y = np.sin(x) + np.sin(2 * x)
plt.subplot(224)
plt.plot(x, y)
plt.title("$y=sinx+sin2x$")
plt.show()
# %%
