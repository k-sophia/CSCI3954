"""
Name: Kelly Camacho
Email: kelly.camacho02@myhunter.cuny.edu
Resources: w3resource.com for Group By
"""

import pandas as pd
import pandasql as psql

inputFile = input("Enter first input file name: ") #mta_trunc_staten_island.csv
outputFile = input("Enter output file name: ") #results.csv

readFile = pd.read_csv(inputFile)

selected = '''
SELECT "date", SUM("entries") as "entries", SUM("exits") as "exits"
FROM readFile
Group By "date"
'''
df = psql.sqldf(selected)
df.to_csv(outputFile, index=False)