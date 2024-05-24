"""
Name: Kelly Camacho
Email: kelly.camacho02@myhunter.cuny.edu
Resources: w3resource for row count, w3schools.com for LEFT JOIN
"""

import pandas as pd
import pandasql as psql

inputFile1 = input("Enter first input file name: ") #restaurants30July.csv
inputFile2 = input("Enter second input file name: ") #nta.csv
prefix = input("Enter output file name: ") #results

readFile1 = pd.read_csv(inputFile1)
readFile2 = pd.read_csv(inputFile2)


#1 NTA col
select1 = 'SELECT "NTA" FROM readFile1'
nta = psql.sqldf(select1)
nta.to_csv(prefix + '1.csv', index=False)


#2 COUNT DISTINCT NTA
select2 = '''
SELECT COUNT(DISTINCT("NTA")) as "count(distinct NTA)"
FROM readFile1
'''
ntaUnique = psql.sqldf(select2)
ntaUnique.to_csv(prefix + '2.csv', index=False)


#3 NTA & COUNT DISTINCT DBA
select3 = '''
SELECT "NTA", COUNT(DISTINCT("DBA")) as cnt_restaurants
FROM readFile1
GROUP BY "NTA"
'''
nta_dba = psql.sqldf(select3)
nta_dba.to_csv(prefix + '3.csv', index=False)


#4 COUNT ROWS & DISTINCT NTA
select4 = '''
SELECT COUNT(*) as num_rows, COUNT(DISTINCT("NTA")) as num_ntas
FROM readFile2
'''
row_nta = psql.sqldf(select4)
row_nta.to_csv(prefix + '4.csv', index=False)


#5 DBA & NTA from file1 & file2
select5 = '''
SELECT readFile1.NTA, readFile2.NTA_NAME
FROM readFile1
LEFT JOIN readFile2
ON readFile1.NTA = readFile2.NTA
'''
dba_ntaBOTH = psql.sqldf(select5)
dba_ntaBOTH.to_csv(prefix + '5.csv', index=False)


#6 addFrom5 DISTINCT NTA, DISTINCT NTA DESCRIPTION, COUNT DISTINCT DBA
select6 = '''
SELECT readFile1.NTA, readFile2.NTA_NAME, COUNT(DISTINCT(readFile1.DBA)) as num_restaurants
FROM readFile1
LEFT JOIN readFile2
ON readFile1.NTA = readFile2.NTA
GROUP BY readFile1.NTA
'''
aggregation = psql.sqldf(select6)
aggregation.to_csv(prefix + '6.csv', index=False)