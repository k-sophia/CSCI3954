"""
Test driver for Program 23
"""

import pandas as pd
import numpy as np
import p23

simpleDF = pd.DataFrame({'c1': [1,2,3,4],\
                         'c2': [0,1,0,1],\
                         'c3': [1,10,3,20],\
                         'c4': [-10,-20,-30,-40],})
'''
Expected Output:
Testing with c1 and [c3,c4]:
('c4', -1.0)
c1 has highest absolute r with ('c1', 1.0)
'''
print('Testing with c1 and [c3,c4]:')
print(p23.findHighestCorr('c1',['c3','c4'],simpleDF))
print(f'c1 has highest absolute r with {p23.findHighestCorr("c1",simpleDF.columns, simpleDF)}.')