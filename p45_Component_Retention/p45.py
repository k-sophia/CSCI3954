"""
Resources: No Resources Used
"""

import pandas as pd
import numpy as np

'''
arr: array (in decreasing order)

returns the number of elements needed to capture more than 85% of the variance
'''
def captures85(arr):
    cv = (arr**2)/sum(arr**2) #captured variance
    percent = 0.85
    count = 0

    for a in cv:
        if(percent > 0):
            percent -= a
            count += 1
    
    return count

'''
arr: array (in decreasing order)

returns the number of elements greater than avg
'''
def averageEigenvalue(arr):
    avg = sum(arr)/len(arr)

    count = 0
    for a in arr:
        if a > avg:
            count += 1
        else:
            break
        
    return count