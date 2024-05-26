"""
Name: Kelly Camacho
Email: kelly.camacho02@myhunter.cuny.edu
Resources: No Resources Used
"""

import pandas as pd
import pandasql as psql

inputFile = input("Enter first input file name: ") #taxi_new_years_day_2020.csv
outputFile = input("Enter output file name: ") #results.csv

readFile = pd.read_csv(inputFile)

readFile['percent_tip'] = round(100*readFile['tip_amount']/readFile['fare_amount'], 1)
readFile['percent_fare'] = round(100*readFile['fare_amount']/readFile['total_amount'], 1)

df = pd.DataFrame(readFile)
df.to_csv(outputFile, index=False)