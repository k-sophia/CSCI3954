"""
Resources: textbook.ds100.org for re
"""

import pandas as pd
import re

inputFile = input("Enter input file name: ") #restaurants30July.csv
outputFile = input("Enter output file name: ") #results.csv

read = pd.read_csv(inputFile)

#change phone numbers format
def formatPhoneNumber(string):
    digits = r"[0-9]{10}"
    
    if re.search(digits, string) is None:
        return ""

    if re.search(digits, string) is not None:
        firstPart = string[:3]
        secondPart = string[3:6]
        thirdPart = string[6:10]
        newNumber = re.sub(digits, "+1-" + firstPart + "-" + secondPart + "-" + thirdPart, string)
        return newNumber

#change inspection date format
def formatInspectionDate(string):
    dateFormat = r"[0-9]{1,2}/[0-9]{1,2}/[0-9]{4}"
    
    if re.search(dateFormat, string) is None:
        return ""

    if re.search(dateFormat, string) is not None:
        date = re.split(r'(\/)', string)
        year = date[4] 
        month = date[0] if len(date[0]) == 2 else '0' + date[0]
        day = date[2] if len(date[2]) == 2 else '0' + date[2]
        newDate = re.sub(dateFormat, year + "/" + month + "/" + day, string)
        return newDate

#set new data
data = read
data['PHONE'] = read['PHONE'].apply(formatPhoneNumber)
data['INSPECTION DATE'] = read['INSPECTION DATE'].apply(formatInspectionDate)
data['restaurant_name'] = read['DBA'].str.title()
data['thai_boolean'] = data['restaurant_name'].str.contains(r'Thai')

df = pd.DataFrame(data)
df.to_csv(outputFile, index=False)