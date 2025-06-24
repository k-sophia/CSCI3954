"""
Resources: textbook.ds.100.org
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# helper function
def getDegree(df, xes, yes,deg):
    first_X = PolynomialFeatures(degree=deg).fit_transform(df[[xes]])
    
    transformer = PolynomialFeatures(degree=deg)
    X = transformer.fit_transform(df[[xes]])

    clf = LinearRegression(fit_intercept=False)
    clf.fit(X, df[yes])
    
    pred_linear = (
        LinearRegression(fit_intercept=False).fit(first_X, df[yes]).predict(first_X)
    )

    return pred_linear

'''
takes four inputs:
    df: a DataFrame that including the specified columns.
    xes: a column name of the specified DataFrame,
    yes: a column name of the specified DataFrame.
    epsilon: the size of the sample. It has a default value of 0.01.

returns the smallest integer degree >= 1 for which the model yields a MSE of < the specified epsilon.
'''
def fitPoly(df,xes,yes,epsilon=0.01):
    degree = 1
    for i in range(1, len(df) + 1):
        pred_linear = getDegree(df, xes, yes, i)
        temp = np.mean((pred_linear - df[yes]) ** 2)
        if(temp > epsilon):
            degree += 1
        else:
            return degree

    return degree