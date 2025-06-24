"""
Resources: w3schools.com for OR statements
"""

import pandas as pd
import pandasql as psql

inputFile = input("Enter input file name: ") #restaurants30July.csv
prefix = input("Enter output file name: ") #results

read = pd.read_csv(inputFile)

gradeSearch = 'SELECT * FROM read WHERE GRADE == "A"'
grade = psql.sqldf(gradeSearch)
grade.to_csv(prefix + 'A.csv', index=False)

scoreSearch = 'SELECT * FROM read WHERE SCORE > "70"'
score = psql.sqldf(scoreSearch)
score.to_csv(prefix + '70.csv', index=False)

zipcodeSearch = 'SELECT * FROM read WHERE ZIPCODE == "10002" OR ZIPCODE == "10027" OR ZIPCODE == "10036"'
zipcode = psql.sqldf(zipcodeSearch)
zipcode.to_csv(prefix + 'ZIP.csv', index=False)

allSearch = 'SELECT "DBA", "CUISINE DESCRIPTION", "BORO", "GRADE" FROM read WHERE GRADE == "A" AND (ZIPCODE == "10002" OR ZIPCODE == "10027" OR ZIPCODE == "10036")'
allAbove = psql.sqldf(allSearch)

data = {
    "restaurant_name" : allAbove["DBA"],
    "cuisine_description" : allAbove["CUISINE DESCRIPTION"],
    "borough" : allAbove["BORO"],
    "GRADE": allAbove["GRADE"]
}

df = pd.DataFrame(data)
df.to_csv(prefix + 'All.csv', index=False)