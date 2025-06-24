"""
Resources: No Resources Used
"""

import pandas as pd
import datetime

'''
takes three inputs:
    df: a DataFrame that including the specified column
    colName: a column name of the specified DataFrame
    datetime: a Boolean variable that indicates if the column contains a datetime string. 
                default value is False and that the column contains numeric values. 
                when set to True, inteprets the column values as datestring objects.

Computes the range of the values in the Series df[colName] and returns a numeric answer. 
If the datetime flag is set, the total number of seconds between the minimum and maximum values is returned.
'''
def colRange(df, colName, datetime = False):
    if(datetime):
         diff = pd.to_datetime(max(df[colName])) - pd.to_datetime(min(df[colName]))
         return diff.total_seconds()
    else:
        getMax = df[colName].max()
        getMin = df[colName].min()
        return getMax - getMin