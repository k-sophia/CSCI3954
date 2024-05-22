"""
Name: Kelly Camacho
Email: kelly.camacho02@myhunter.cuny.edu
Resources: pandas.pydata.org for loc and stackabuse.com for writing csv file
"""

import pandas as pd

inputFile = input("Enter input file name: ") #legislators-current.csv
outputFileName = input("Enter output file name: ") #results.csv

read = pd.read_csv(inputFile)
senateClass = read.loc[read['senate_class'] >= 1]

data = {'first_name': senateClass["first_name"],
                   'last_name': senateClass["last_name"]}

df = pd.DataFrame(data, columns= ['first_name', 'last_name'])
df.to_csv(outputFileName, index=False)

print(df)
