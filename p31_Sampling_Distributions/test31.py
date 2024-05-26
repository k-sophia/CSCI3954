"""
Test driver for Program 31
"""

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import p31

nd = [np.random.normal() for i in range(1000)]
ed = [np.random.exponential() for i in range(1000)]
df = pd.DataFrame({ "nd" : nd, "ed" : ed})

'''
Expected output:
nd = [np.random.normal() for i in range(1000)]
ed = [np.random.exponential() for i in range(1000)]
df = pd.DataFrame({ "nd" : nd, "ed" : ed})
print(p31.sampleMeans(df, 'nd', k = 5, n=5))
print(p31.sampleMeans(df, 'nd', k = 10, n=5))
'''
print(p31.sampleMeans(df, 'nd', k = 5, n=5))
print(p31.sampleMeans(df, 'nd', k = 10, n=5))


k_10 = p31.sampleMeans(df, 'ed', k = 10)
k_20 = p31.sampleMeans(df, 'ed', k = 20)
k_30 = p31.sampleMeans(df, 'ed', k = 30)
sns.histplot([ed,k_10,k_20,k_30],element="poly")
plt.title('Means of 1000 samples of an exponential distribution')
# expected plot shown in sample_means.png
plt.show()