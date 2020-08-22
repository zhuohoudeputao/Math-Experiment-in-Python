'''
@Author: zhuohoudeputao
LastEditors: zhuohoudeputao
LastEditTime: 2020-08-22 15:06:00
@Description: file content
'''

# %%[markdown]
# In the experimental research of agricultural production, the relationship between the yeild of potatoes and fertilizers in a region is studied.
# The corresponding relationship of the amount of nitrogen fertilizer, phosphorus fertilizer and potato yield is given in the following table.
# Try to give the relationship between them and make a resonable ferilization program, and
# %%
import numpy as np
import matplotlib.pyplot as plt

# %% original data
nitrogen_fertilizer = np.array([0, 34, 67, 101, 135, 202, 259, 336, 404, 471])
potatoes_yield_n = np.array([15.18, 21.36, 25.72, 32.29,
                             34.03, 39.45, 43.15, 43.46, 40.83, 30.75])
phosphorus_fertilizer = np.array([0, 24, 49, 73, 98, 147, 169, 245, 294, 342])
potatoes_yield_p = np.array([33.46, 32.47, 36.06, 37.96,
                             41.04, 40.09, 41.26, 42.27, 40.36, 42.73])

# %% show their original graph
plt.plot(nitrogen_fertilizer, potatoes_yield_n)
plt.show() # this one looks like a quadratic function

plt.plot(phosphorus_fertilizer, potatoes_yield_p)
plt.show() # this one looks like two linear parts
# %% fitting the nitrogen_fertilizer to yield
nitrogen_p=np.polyfit(nitrogen_fertilizer, potatoes_yield_n, 2)
plt.plot(nitrogen_fertilizer, potatoes_yield_n, "g.", label="before fitting")
plt.plot(np.arange(0,500), np.polyval(nitrogen_p, np.arange(0,500)), "b--", label="after fitting")
plt.show()
# %% fitting the phosphorus_fertilizer to yield
phosphorus_p1 = np.polyfit(phosphorus_fertilizer[0:5], potatoes_yield_p[0:5], 1)
phosphorus_p2 = np.polyfit(phosphorus_fertilizer[5:], potatoes_yield_p[5:], 1)
plt.plot(phosphorus_fertilizer, potatoes_yield_p, 'g.', label="before fitting")
med = (phosphorus_p2[1]-phosphorus_p1[1])/(phosphorus_p1[0]-phosphorus_p2[0]) # the medium
plt.plot(np.arange(0,med), np.polyval(phosphorus_p1, np.arange(0,med)))
plt.plot(np.arange(med,350), np.polyval(phosphorus_p2, np.arange(med,350)), 'b--', label="after fitting")
plt.show()
# %% most suitable nitrogen_fertilizer amount
x = -nitrogen_p[1]/(2*nitrogen_p[0]) 
nitrogen_fertilizer_amount = np.polyval(nitrogen_p, x)
plt.plot(np.arange(0,500), np.polyval(nitrogen_p, np.arange(0,500)))
plt.plot(x, nitrogen_fertilizer_amount, 'ro')
print(x, nitrogen_fertilizer_amount)
plt.show()
# %% most suitable phosphorus_fertilizer amount
x = med 
phosphorus_fertilizer_amount = np.polyval(phosphorus_p2, x)
plt.plot(np.arange(0,med), np.polyval(phosphorus_p1, np.arange(0,med)))
plt.plot(np.arange(med,350), np.polyval(phosphorus_p2, np.arange(med,350)))
plt.plot(x, phosphorus_fertilizer_amount, 'ro')
print(x, phosphorus_fertilizer_amount)
plt.show()
# %%
