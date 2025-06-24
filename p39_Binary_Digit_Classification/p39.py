"""
Resources: No Resources Used
"""

import pandas as pd
import numpy as np
from sklearn import datasets, svm, metrics
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

'''
four inputs:
    data: a numpy array that includes rows of equal size flattend arrays
    target a numpy array that takes values 0 or 1 corresponding to the rows of data
    test_size: the size of the test set created when the data is divided into test and training sets with train_test_split
        default value is 0.25.
    random_state: the random seed used when the data is divided into test and training sets with train_test_split
        default value is 21.

The function confusion matrix that results.
'''
def binary_digit_clf(data, target, test_size = 0.25, random_state = 21):
    X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=test_size, random_state=random_state)
    clf = LogisticRegression()
    clf.fit(X_train, y_train)

    predict = clf.predict(X_test)
    matrix = metrics.confusion_matrix(y_test, predict, labels=[1,0])

    return matrix