"""
Test driver for Program 32
"""

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import p32

# Expected output:
# -0.014420727967150241
df = pd.read_csv('dailyAttendanceManHunt2018.csv')
print(p32.attendCorr(df))