"""
Test driver for Program 42
"""

import pandas as pd
import numpy as np
import p42
import p38_Ticket_Prep.p38 as p38

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv('Parking_Q1_2021_Lexington.csv')
#Focus on features about vehicles:
df = df[['Plate ID','Plate Type','Registration State','Issue Date','Vehicle Color']]
#Drop rows that are missing info:
df = df.dropna()
print(f'Your file contains {len(df)} parking violations.')
#Clean the data, using the functions written for P38:
df['Plate Type'] = df['Plate Type'].apply(p38.cleanReg)
df['Vehicle Color'] = df['Vehicle Color'].apply(p38.cleanColor)
#Count tickets for each vehicle:
newDF =  df.groupby('Plate ID').agg(NumTickets =
    pd.NamedAgg(column = 'Plate ID', aggfunc = 'count'),
    Registration = pd.NamedAgg(column = 'Plate Type', aggfunc = 'first'),
    State = pd.NamedAgg(column = 'Registration State', aggfunc = 'first'),
    Color = pd.NamedAgg(column = 'Vehicle Color', aggfunc = 'first')
)

'''
Expected output:
Your file contains 20589 parking violations.
          NumTickets Registration State  Color
Plate ID
00356R2            1          PAS    TX  WHITE
004LSM             1          PAS    TN  OTHER
00574R7            1          PAS    TX  WHITE
0064NQD            1          PAS    DP  BLACK
0107NQD            1          PAS    DP   GRAY
...              ...          ...   ...    ...
ZRB1864            1          PAS    PA  WHITE
ZSA6859            1          PAS    PA   GRAY
ZSE1922            1          PAS    PA  WHITE
ZWF62E             1          PAS    NJ  OTHER
ZWZ35J             1          PAS    NJ  OTHER
'''
print(newDF)


'''
Expected output:
          NumTickets  Registration_OTHER  ...  State_WI  State_WV
Plate ID                                  ...
00356R2            1                   0  ...         0         0
004LSM             1                   0  ...         0         0
00574R7            1                   0  ...         0         0
0064NQD            1                   0  ...         0         0
0107NQD            1                   0  ...         0         0
...              ...                 ...  ...       ...       ...
ZRB1864            1                   0  ...         0         0
ZSA6859            1                   0  ...         0         0
ZSE1922            1                   0  ...         0         0
ZWF62E             1                   0  ...         0         0
ZWZ35J             1                   0  ...         0         0
'''
newDF = p42.addIndicators(newDF)
print(newDF)


'''
Expected output:
Score is 0.04310334739677757.
NY state, white commercial vehicle (encoded as: [1,0,0,0,0,1])
	will get 2.48 tickets.
NY state, gray passenger vehicle (encoded as: [1,0,1,1,0,0])
	will get 1.16 tickets.
'''
xes = ['State_NY','Registration_OTHER', 'Registration_PAS', 'Color_GRAY', 'Color_OTHER', 'Color_WHITE']
y_col = 'NumTickets'
sc,clf = p42.build_clf(newDF, xes)
print(f'Score is {sc}.')
predicted = clf.predict([[1,0,0,0,0,1]])[0]
print(f'NY state, white commercial vehicle (encoded as: [1,0,0,0,0,1])\n\twill get {predicted:.2f} tickets.')
predicted = clf.predict([[1,0,1,1,0,0]])[0]
print(f'NY state, gray passenger vehicle (encoded as: [1,0,1,1,0,0])\n\twill get {predicted:.2f} tickets.')