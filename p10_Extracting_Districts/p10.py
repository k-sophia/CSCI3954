"""
Resources: Provided Code in HW10 Description
"""

import pandas as pd

#function
def extractDistrict(name):
    return int(name[:2])

inputFile = input("Enter input file name: ") #school_ELA_2013_2019.csv
outputFile = input("Enter output file name: ") #results.csv

read = pd.read_csv(inputFile)

read['District'] = read['DBN'].apply(extractDistrict)
read.to_csv(outputFile, index=False)