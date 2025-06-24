"""
Resources: Example code from program description
"""

import pandas as pd
from sklearn import linear_model

csv = input("Enter name of CSV: ") #mpg.csv
first_ind_var = input("Enter name of first independent variable: ") #displacement
second_ind_var = input("Enter name of second independent variable: ") #acceleration
dep_var = input("Enter name of the dependent variable: ") #mpg
first_var_pred = input("Enter value for first variable for prediction: ") # 100
second_var_pred = input("Enter value for second variable for prediction: ") #12.0

read = pd.read_csv(csv)

regr = linear_model.LinearRegression()
regr.fit( read[[first_ind_var, second_ind_var]], read[dep_var] )

# Expected output:
# Predicted mpg:  29.400598924519038
print(f'Predicted value: {regr.predict([[first_var_pred,second_var_pred]])[0]}')