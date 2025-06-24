"""
Resources: No Resources Used
"""

import pandas as pd
import numpy as np


def sampleMeans(df, colName, k=10, n=1000):
    data = []

    for i in range(0, n):
        temp = []
        temp = df[colName].sample(n = k)
        avg = temp.mean()
        data.append(avg)
    
    return data


"""
nd = [np.random.normal() for i in range(1000)]
ed = [np.random.exponential() for i in range(1000)]
df = pd.DataFrame({ "nd" : nd, "ed" : ed})
print(sampleMeans(df, 'nd', k = 5, n=5))
print(sampleMeans(df, 'nd', k = 10, n=5))
"""
