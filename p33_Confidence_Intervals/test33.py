"""
Test driver for Program 33
"""

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import p33

'''
Expected output:
intervals: [(0.0843959275632028, 1.3323778628928307), (-0.146668094360358, 1.5546642787617675), (-1.029505009635772, 0.5272177024225991), (-0.5702633299624739, 0.5144718024588405), (-0.3979475729570697, 1.1005279531825056), (-0.9894141075519297, 0.8070447535623141), (-1.0433450932702595, 0.7059405804735273), (-0.8902508132395719, 0.3772852944801963), (-1.1068858052695578, 0.0816760750250739), (-0.3661920360152307, 1.003198126280235)]
successes: [0.0, 50.0, 66.66666666666667, 75.0, 80.0, 83.33333333333333, 85.71428571428571, 87.5, 88.88888888888889, 90.0]
'''
intervals, successes = p33.ciRuns(trials = 20)
print(f"intervals: {intervals}")
print(f"successes: {successes}")


intervals, successes = p33.ciRuns(mu=500, sigma=100, alpha = .90, trials = 1000)
xes = np.linspace(1,1000,1000)
yes = 90*np.ones(1000)
plt.scatter(xes,successes)
plt.plot(xes,yes,color='red')
plt.title('alpha=90, mu = 500, sigma=100, & trials=1000')
# expected plot shown in ciRun_alpha_90.png
plt.show()