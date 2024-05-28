"""
Test driver for Program 44
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn import datasets
import p44


iris = datasets.load_iris()
l_40,s_40 = p44.compare_clf(iris.data,iris.target,test_size=.4)

'''
Expected output:
With a 40% test set, LogReg classifer has score 0.9833333333333333.
SVM classifier had score 0.9833333333333333.
'''
print(f'With a 40% test set, LogReg classifer has score {l_40}.\nSVM classifier had score {s_40}.')

xes = list(range(5,100,5))
runs = [p44.compare_clf(iris.data,iris.target,test_size=x/100) for x in xes]
lr_runs, svm_runs = zip(*runs)
plt.plot(xes, lr_runs, label="LogReg")
plt.plot(xes, svm_runs, label= "SVM")
plt.xlabel('Test Size (Percent)')
plt.ylabel('Score')
plt.title('Iris Dataset:  Test Size vs Score')
plt.legend()
# expected plot shown in iris_logR_svm.png
plt.show()

