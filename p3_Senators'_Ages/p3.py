"""
Resources: pandas.pydate.org for datetime
"""

import pandas as pd

inputFile = input("Enter input file name: ") #legislators-current.csv
outputFileName = input("Enter output file name: ") #results.csv

read = pd.read_csv(inputFile)
senateClass = read.loc[read['senate_class'] >= 1]

ages = []
currentDate = pd.to_datetime('2021-01-01')

for b in senateClass["birthday"]:
    birthDate = pd.to_datetime(b)
    addAge = currentDate.year - birthDate.year - (
        (currentDate.month, currentDate.day) < (birthDate.month, birthDate.day))
    ages.append(addAge)
    

data = {'first_name': senateClass["first_name"],
                   'age': ages}

df = pd.DataFrame(data, columns= ['first_name', 'age'])
df.to_csv(outputFileName, index=False)