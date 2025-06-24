"""
Resources: pandas.pydata.org for drop
"""

import pandas as pd

def countCourses(df):
    return df.count(' ') + 1

def countCS(df):
    return df.count('csci')

def computeEnrollments(df):
    df['NumCourses'] = df['Current Courses'].apply(countCourses)
    df['CS'] = df['Current Courses'].apply(countCS)
    df['Other'] = df['NumCourses'] - df['CS']
    df = df.loc[df['NumCourses'] > 2]
    df = df.drop(columns = 'Current Courses')
    return df