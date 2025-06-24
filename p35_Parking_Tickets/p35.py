"""
Resources: No Resources Used
"""

import pandas as pd
import numpy as np

'''
takes three inputs:
    df: a DataFrame that including the specified column.
    colName: a column name of the specified DataFrame; default value is 'Registration State'
    indicator: the value used for the indicator as well as the new column created. The default value is NY.

return DataFrame with a new column, indicator to the DataFrame that takes values 
    1 when indicator is in df[colName]
    0 if it has a different value and nanotherwise
'''
def addIndicator(df, colName = "Registration State", indicator = "NY"):
    df[indicator] = df[colName].apply(lambda x: 1 if indicator == x else 0)
    return df