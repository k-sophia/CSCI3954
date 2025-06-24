"""
Resources: Example code from Homework 7
"""

import pandas as pd
import pandasql as psql

inputFile = input("Enter input file name: ") #nynta.csv
outputFileName = input("Enter output file name: ") #results.csv

read = pd.read_csv(inputFile)

selected = 'SELECT NTACode,NTAName FROM read'

NTA_columns = psql.sqldf(selected)

data = {
    'NTA' : NTA_columns['NTACode'],
    'NTA_Name': NTA_columns['NTAName']
}

df = pd.DataFrame(data)
df.to_csv(outputFileName, index=False)