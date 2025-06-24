"""
Resources: Lecture Slides and geeksforgeeks.com for concat
"""

import pandas as pd

def extractDistrict(string):
    return string[:2]


ELA_File = input("Enter file containing ELA scores: ") #ela_trunc.csv
MATH_File = input("Enter file containing MATH scores: ") #math_trunc.csv

elaFile = pd.read_csv(ELA_File)
mathFile = pd.read_csv(MATH_File)

#Get District Number
mathFile['District'] = mathFile['DBN'].apply(extractDistrict)
elaFile['District'] = elaFile['DBN'].apply(extractDistrict)

mathFile['Subject'] = "MATH"
elaFile['Subject'] = "ELA"

#remove some
mathFile = mathFile[mathFile["Number Tested"] > 20]
elaFile = elaFile[elaFile["Number Tested"] > 20]

#Rename Level to Num Prof
mathFile.rename(columns = {"# Level 3+4":"Number Proficient"}, inplace= True)
elaFile.rename(columns = {"# Level 3+4":"Number Proficient"}, inplace= True)

#Get Percentage
mathFile['Proficiency'] = (mathFile['Number Proficient']/mathFile['Number Tested'])*100
elaFile['Proficiency'] = (elaFile['Number Proficient']/elaFile['Number Tested'])*100

mathFile = mathFile.loc[ mathFile.groupby('District')['Proficiency'].idxmax() ]
elaFile = elaFile.loc[ elaFile.groupby('District')['Proficiency'].idxmax() ]

combine = [mathFile, elaFile]
df = pd.concat(combine, axis=0, join="inner")

#make pivot table
pivot = pd.pivot_table(
    df,
    index = ["District","Subject"],
    values = ["Proficiency","School Name"],
    aggfunc = "max"
)