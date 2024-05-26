"""
Test driver for Program 25
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import p25

'''
Expected output
The values are: (50, 52, 54)
The pmf is: (0.5, 0.25, 0.25)
The sum of the pmf is: 1.0.
'''
x, y = p25.pmf([50,50,52,54])
print(f'The values are: {x}')
print(f'The pmf is: {y}')
print(f'The sum of the pmf is: {sum(y)}.')

#expected plot shown in pmf_small_age.png
plt.bar(x,y)
plt.show()