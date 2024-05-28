"""
Test driver for Program 48
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import p48


'''
Expected output:
                          Name  ...  Hunter College
0        Empire State Building  ...         21 mins
1                    Bronx Zoo  ...   1 hour 2 mins
2   National Lighthouse Museum  ...  1 hour 21 mins
3  FDR Four Freedom State Park  ...         37 mins
4                   Citi Field  ...         35 mins
5                 Coney Island  ...  1 hour 10 mins
6               Hunter College  ...          0 mins

[7 rows x 9 columns]
[[  0  55  79  29  40  61  21]
 [ 55   0 105  72  70 106  62]
 [ 99 113   0  83  98 105  81]
 [ 29  71  92   0  41  84  37]
 [ 39  73 105  41   0  95  35]
 [ 59 123  91  83 102   0  70]
 [ 16  67  86  24  35  71   0]]
'''
transit = pd.read_csv('nyc_landmarks_transit.csv')
print(transit)
transit_mx = p48.extractMx(transit)
print(transit_mx)


'''
Expected output:
[[0.         1.         1.43636364 0.52727273 0.72727273 1.10909091 0.38181818]
 [1.         0.         1.90909091 1.30909091 1.27272727 1.92727273  1.12727273]
 [1.8        2.05454545 0.         1.50909091 1.78181818 1.90909091  1.47272727]
 [0.52727273 1.29090909 1.67272727 0.         0.74545455 1.52727273  0.67272727]
 [0.70909091 1.32727273 1.90909091 0.74545455 0.         1.72727273  0.63636364]
 [1.07272727 2.23636364 1.65454545 1.50909091 1.85454545 0.          1.27272727]
 [0.29090909 1.21818182 1.56363636 0.43636364 0.63636364 1.29090909  0.        ]]
'''
transit_normed = p48.scaleMx(transit_mx)
print(transit_normed)