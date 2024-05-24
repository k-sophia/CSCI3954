"""
Name: Kelly Camacho
Email: kelly.camacho02@myhunter.cuny.edu
Resources: geeksforgeeks.org for astype
"""

import pandas as pd

inputFile = input("Enter first input file name: ") #public-district-attendance-results-2014-2019.csv
outputFile = input("Enter output file name: ") #results.csv
grade = input("Enter grade: ") #3
year = input("Enter year: ") # 2018-19

readFile = pd.read_csv(inputFile)
readFile['Grade'] = readFile['Grade'].astype(str)

selected = readFile[readFile['Grade'] == grade]
selected = selected[selected['Year'] == year]

selected.to_csv(outputFile, index=False)