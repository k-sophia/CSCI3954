"""
Test driver for Program 45
"""

import pandas as pd
import numpy as np
import p45


a = np.array([585.57, 261.06, 166.31,  57.14,  48.16,  39.79,  31.71,  28.91,
      24.23,  22.23,  20.51,  18.96,  17.01,  15.73,   7.72,   4.3 ,
      1.95,   0.04])

# Expect output: 2
cap = p45.captures85(a)
print(cap)

# Expected output: 3
avg = p45.averageEigenvalue(a)
print(avg)