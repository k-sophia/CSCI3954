"""
Resources: No Resources Used
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

def compare_clf(xes, y, test_size = 0.20, random_state=66,max_iter=500):
    X_train, X_test, y_train, y_test = train_test_split(xes, y, test_size = test_size, random_state = random_state)

    clf = LogisticRegression(max_iter = max_iter)
    clf.fit(X_train, y_train)
    LogReg = clf.score(X_test, y_test)

    clf = SVC(max_iter = max_iter)
    clf.fit(X_train, y_train)
    SVM = clf.score(X_test, y_test)

    return LogReg, SVM


"""
iris = datasets.load_iris()
l_40,s_40 = compare_clf(iris.data,iris.target,test_size=.4)
print(f'With a 40% test set, LogReg classifer has score {l_40}.\nSVM classifier had score {s_40}.')
"""
