"""
Test driver for Program 34
"""

import numpy as np
import pandas as pd
import p34

'''
Expected output:

Starting df:
    sweetness  overall
0        4.1      3.9
1        6.9      5.4
2        8.3      5.8
3        8.0      6.0
4        9.1      6.5
5        9.8      6.1
6       11.0      5.9
7       11.7      5.5
8       11.9      5.4
For epsilon = 0.5, poly has degree 1.
'''
df = pd.read_csv('icecream.csv')
print(f'Starting df:\n {df}')
eps = 0.5
deg = p34.fitPoly(df,'sweetness','overall',epsilon=eps)
print(f'For epsilon = {eps}, poly has degree {deg}.')


# Expected output:
# For epsilon = 0.1, poly has degree: 2.
eps= 0.1
deg = p34.fitPoly(df,'sweetness','overall',epsilon=eps)
print(f'For epsilon = {eps}, poly has degree: {deg}.')


# Expected output:
# For default epsilon, poly has degree: 8.
eps= 0.01
deg = p34.fitPoly(df,'sweetness','overall')
print(f'For epsilon = {eps}, poly has degree: {deg}.')