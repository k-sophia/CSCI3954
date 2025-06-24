"""
Resources: tectbook.ds100.org
"""

import pandas as pd
import numpy as np
from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

'''
six inputs:
    df: a DataFrame that including the specified columns
    columns: a list of column names of the specified DataFrame
    x_col: a column name of the specified DataFrame containing locations
        independent variables for the model (the other is from the list columns)
        default value is "shot_distance"
    y_col: a column name of the specified DataFrame containing locations
        dependent variable (what's being predicted) in the model
        default value is "shot_made"
    test_size: the size of the test set created when the data is divided into test and training sets with train_test_split
        default value is 40
    random_state: the random seed used when the data is divided into test and training sets with train_test_split
        default value is 42

returns the highest prediction accuracy found from the columns inputted, as well as the name of the column that increases prediction accuracy the most.
'''
def bestForPredict(df, columns, x_col = "shot_distance", y_col = "shot_made", test_size = 40, random_state = 42):
    accuracy = 0.0
    col_name = ""

    for c in columns:
        y = df[y_col]
        rows = df[[x_col, c]].to_dict('records')

        onehot = DictVectorizer(sparse=False).fit(rows)

        X = onehot.transform(rows)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = test_size, random_state = random_state)

        clf = LogisticRegression()
        clf.fit(X_train, y_train)
        temp = clf.score(X_test, y_test)

        if(temp > accuracy):
            accuracy = temp
            col_name = c

    return accuracy, col_name 