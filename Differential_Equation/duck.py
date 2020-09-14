'''
Author: zhuohoudeputao
LastEditors: zhuohoudeputao
LastEditTime: 2020-09-05 11:41:28
Description: file content
'''
# %% [markdown]
# Set the opposite shore point of the river point O is the point A.
# River width OA=h. The two banks are parallel lines, and the velocity of the water is 0.5 meters per second.
# There is a duck swimming from point A to point O.
# Set the swimming speed of the duck in still water is 1 meters per second, and the duck's swimming direction is always towards the point O.
# Find the equation of the trace line that the duck swims through. Solve it and draw it.

# %%
import numpy as np
from numpy.lib.scimath import sqrt
from matplotlib.pyplot import plot
from scipy.integrate import solve_ivp
h = 6
# %%
def swim_odefun(t, y):
    s = sqrt(y[0] ** 2+y[1] ** 2)
    return [0.5-1*y[0]/s, -1*y[1]/s]


# %%
t_span = [0, 1.4*h]
t_eval = np.linspace(0, 1.4*h, 100)
sol = solve_ivp(swim_odefun, t_span, y0=[0, h], t_eval=t_eval)
# print(sol)
plot(sol.y[0], sol.y[1])
# %%
