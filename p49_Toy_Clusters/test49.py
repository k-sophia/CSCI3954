"""
Test driver for Program 49
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import datasets
import p49


'''
Expected output:
Iris:  The accuracy with no-preprocessing is 0.8933333333333333.
Iris: The accuracy with TSNE preprocessing is 0.9133333333333333.
Iris: The accuracy with MDS preprocessing is 0.9.
Wine:  The accuracy with no-preprocessing is 0.702247191011236.
Wine: The accuracy with TSNE preprocessing is 0.6797752808988764.
'''
iris = datasets.load_iris()
no_preproc = p49.clusterDemo(iris)
print(f'Iris:  The accuracy with no-preprocessing is {no_preproc}.')
tsne_proc = p49.clusterDemo(iris, method = "TSNE")
print(f'Iris: The accuracy with TSNE preprocessing is {tsne_proc}.')
mds_proc = p49.clusterDemo(iris, method = "MDS")
print(f'Iris: The accuracy with MDS preprocessing is {mds_proc}.')

wine = datasets.load_wine()
no_preproc = p49.clusterDemo(wine, n_components = 3, random_state=10)
print(f'Wine:  The accuracy with no-preprocessing is {no_preproc}.')
tsne_proc = p49.clusterDemo(wine, n_components = 3, method = "TSNE", random_state=10)
print(f'Wine: The accuracy with TSNE preprocessing is {tsne_proc}.')


'''
Expected output:
Digits: The accuracy with no-preprocessing is 0.7946577629382304.
Digits: The accuracy with TSNE preprocessing is 0.9432387312186978.
Digits: The accuracy with MDS preprocessing is 0.676126878130217.
'''
digits = datasets.load_digits()
no_preproc = p49.clusterDemo(digits, n_clusters = 10, method = "none", random_state=20)
print(f'Digits: The accuracy with no-preprocessing is {no_preproc}.')
tsne_proc = p49.clusterDemo(digits, n_clusters = 10, method = "TSNE", random_state=20)
print(f'Digits: The accuracy with TSNE preprocessing is {tsne_proc}.')
mds_proc = p49.clusterDemo(digits, n_clusters = 10, method = "MDS", random_state=20)
print(f'Digits: The accuracy with MDS preprocessing is {mds_proc}.')