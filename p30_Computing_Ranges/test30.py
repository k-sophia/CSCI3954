"""
Test driver for Program 30
"""

import numpy as np
import pandas as pd
import seaborn as sns
import p30

'''
Expected outpu:
Testing colRange(simpleDF,'id'): 3
Testing colRange(simpleDF,'checkin',datetime=True): 114011.0
'''
simpleDF = pd.DataFrame({'id': [1,2,3,4],\
    'checkin': ["2019-03-23 20:21:09","2019-03-23 20:27:24",\
                "2019-03-22 12:47:13","2019-03-22 12:58:17"],\
    'total': [32.51,19.99,1.05,20.50]})
print(f"Testing colRange(simpleDF,'id'): {p30.colRange(simpleDF,'id')}")
print(f"Testing colRange(simpleDF,'checkin',datetime=True): {p30.colRange(simpleDF,'checkin',datetime=True)}")


'''
Expected output:
Testing colRange(taxis,'distance'): 7.21
Testing colRange(taxis,'dropoff',datetime=True): 2236694.0
'''
taxis = sns.load_dataset('tips').dropna().loc[:10]
print(f"Testing colRange(taxis,'total'): {p30.colRange(taxis,'total')}")
print(f"Testing colRange(taxis,'dropoff',datetime=True): {p30.colRange(taxis,'dropoff',datetime=True):}")