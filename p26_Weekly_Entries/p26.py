"""
Resources: pandas.pydata.org for datetime
"""

import pandas as pd
import datetime

# takes two variables of type datetime
# returns the difference between them.
def tripTime(start, end):
    newStart = pd.to_datetime(start)
    newEnd = pd.to_datetime(end)
    
    return newEnd  - newStart

# takes a DataFrame, df, containing the column name, col
# returns a DataFrame containing only times that fall on a weekday
def weekdays(df, col):
    df = df.loc[pd.to_datetime(df[col]).dt.day_name() != "Saturday"]
    df = df.loc[pd.to_datetime(df[col]).dt.day_name() != "Sunday"]

    return df