"""
Test driver for Program 27
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import p27

s1 = [1,2,3,4,5,6,7,8,9,10]
s2 = [0,1,1,2,2,3,3,4,4,5,]
m, b = p27.compute_r_line(s1,s2)
print(m,b)
xes = np.array([0,10])
yes = m*xes + b
plt.scatter(s1,s2)
plt.plot(xes,yes)
plt.title(f'Regression line with m = {m:{4}.{2}} and y-intercept = {b:{4}.{2}}')
# expected plot shown in rline_simple.png
plt.show()


taxi = sns.load_dataset('taxis')
m, b = p27.compute_r_line(taxi['total'],taxi['tip'])
print(m,b)
xes = np.array([0,175])
yes = m*xes + b
plt.scatter(taxi['total'],taxi['tip'])
plt.plot(xes,yes,color='red')
plt.title(f'Regression line for total vs. tips with m = {m:{4}.{2}} and y-intercept = {b:{4}.{2}}')
plt.xlabel('Total Paid')
plt.ylabel('Tip')
# expected plot shown in rline_taxi.png
plt.show()
