"""
Resources: No Resources Used
"""

import pandas as pd
import numpy as np

def convert(data):
    arr = []
    for d in data:
        temp = d.split(' ')
        if 'hour' in d:
            value = (int(temp[0]) * 60) + int(temp[2])
            arr.append(value)
        else:
            arr.append(int(temp[0]))

    return arr

def extractMx(df, dropCols = ['Name','Position']):
    df = df.drop(columns=dropCols)
    arr = df.apply(convert)
    return arr.to_numpy()

def scaleMx(distMx, i=0,j=1):
    return distMx / distMx[i][j]