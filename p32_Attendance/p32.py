"""
Resources: No Resources Used
"""

import pandas as pd
import numpy as np
import datetime as dt

'''
takes a DataFrame df, with columns School DBN, Date, Enrolled, Absent, and Present.
computes the attendance as a percentage of students present over students enrolled, and calculates the day of the week for each date
returns the correlation coefficient of the two
'''
def attendCorr(df):
    x = df["Present"]/df["Enrolled"]
    y = pd.to_datetime(df["Date"]).dt.dayofweek

    pd.to_numeric(x, errors='coerce')
    pd.to_numeric(y, errors='coerce')

    return x.corr(y)