"""
Test driver for Program 43
"""

import pandas as pd
import numpy as np
import p43


t_mx = np.array([[.7, .07, .1],
         [.25,.9,.15],
         [.05,.03,.75]])

pop0 = np.array([20, 40, 25])

pop1 = t_mx @ pop0
# Expected output:
# Population of each state after 1 year: [19.3  44.75 20.95].
print(f'Population of each state after 1 year: {pop1}.')


'''
Expected output:
Population of each state after 1 year: [19.3  44.75 20.95]
Population of each state after 100 years: [16.91747573 57.76699029 10.31553398]
Steady state population: [16.91747573 57.76699029 10.31553398]
'''
pop1 = p43.moving(t_mx, pop0)
print(f'Population of each state after 1 year: {pop1}')
pop100 = p43.moving(t_mx, pop0, num_years=100)
print(f'Population of each state after 100 years: {pop1}')
pop_steady = p43.steadyState(t_mx, pop0)
print(f'Steady state population: {pop_steady}')