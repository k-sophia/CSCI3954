"""
Name: Kelly Camacho
Email: kelly.camacho02@myhunter.cuny.edu
Resources: kite.com for multiple loc conditions
"""

import pandas as pd

inputFile = input("Enter input file name: ") #school_ELA_2013_2019.csv
outputFileName = input("Enter output file name: ") #results.csv

read = pd.read_csv(inputFile)

selectedRows = read.loc[(read['Grade'] == '3') & (read['Year'] == 2019)]
selectedRows.to_csv(outputFileName, index=False)

print(selectedRows)

