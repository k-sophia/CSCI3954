"""
Test driver for Program 41
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import p41

#Import datasets, classifiers and performance metrics:
from sklearn import datasets, svm, metrics
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
#Using the digits data set from sklearn:
from sklearn import datasets


digits = datasets.load_digits()
n_samples = len(digits.images)
data = digits.images.reshape((n_samples, -1))
X_train, X_test, y_train, y_test = train_test_split(data, digits.target,random_state=42, test_size=.75)
clf = LogisticRegression(max_iter=2000)
clf.fit(X_train,y_train)
y_predict = clf.predict(X_test)
confuse_mx = metrics.confusion_matrix(y_test,y_predict)

# Expected output:
# The most misclassified class is 3.
print(f'The most misclassified class is {p41.clf_misses(confuse_mx)}.')

disp = metrics.ConfusionMatrixDisplay(confusion_matrix=confuse_mx)
disp.plot(cmap = "Purples")
plt.title("Logistic Regression Classifier for Digits")
# expected plot shown in mnist_confuse_mx_75_test.png
plt.show()
