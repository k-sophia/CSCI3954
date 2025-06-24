"""
Resources: No Resources Used
"""

import pandas as pd
import numpy as np

def findHighestCorr(colName,colLst,df):
    num = 0.0
    name = ''
    
    for c in colLst:
        series1 = pd.Series(df[colName])
        series2 = pd.Series(df[c])
        temp = series1.corr(series2)
        
        if(abs(num) < abs(temp)):
            num = temp
            name = c
            
    return name, num