"""
Name: Kelly Camacho
Email: kelly.camacho02@myhunter.cuny.edu
Resources: textbook.ds100.org for sql keywords
"""

import pandas as pd
import pandasql as psql

inputFile = input("Enter input file name: ") #brooklynJuly2021.csv
prefix = input("Enter output file name: ") #results

read = pd.read_csv(inputFile)

#Restaurant
restaurantSearch = 'SELECT DISTINCT("DBA") FROM read GROUP BY "DBA"'
restaurant = psql.sqldf(restaurantSearch)
restaurant.to_csv(prefix + 'Restaurants.csv', index=False)
#print(restaurant)


#Cuisine
cuisineSearch = '''
SELECT DISTINCT("CUISINE DESCRIPTION") as cnt
FROM read
WHERE ZIPCODE == "11224"
GROUP BY "CUISINE DESCRIPTION"
'''
cuisine = psql.sqldf(cuisineSearch)
cuisine.to_csv(prefix + 'Cuisines11224.csv', index=False)

#Counts
countSearch = '''
SELECT "CUISINE DESCRIPTION", COUNT(DISTINCT("DBA")) as "COUNT(DISTINCT DBA)"
FROM read
WHERE ZIPCODE == "11224"
GROUP BY "CUISINE DESCRIPTION"
'''
count = psql.sqldf(countSearch)
count.to_csv(prefix + 'Counts11224.csv', index=False)

#Boro
boroSearch = '''
SELECT "BORO" as borough, COUNT(DISTINCT("CUISINE DESCRIPTION")) as cnt_cuisine, COUNT(DISTINCT("DBA")) as cnt_restaurants
FROM read
GROUP BY "BORO"
'''
boro = psql.sqldf(boroSearch)
boro.to_csv(prefix + 'Boro.csv', index=False)