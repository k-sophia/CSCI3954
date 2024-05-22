"""
Name: Kelly Camacho
Email: kelly.camacho02@myhunter.cuny.edu
Resources: textbook.ds100.org for re
           newbedev.com for re.findall
"""

import pandas as pd
import re

inputFile = input("Enter input file name: ") #url.html
outputFileName = input("Enter output file name: ") #results.csv

f= open(inputFile)
read = f.read()

url_temp = re.findall(r'\:\/\/(.+?)\"\>', read)

url = []

for u in url_temp:
    if u[-1] == '/':
        url.append(u[:-1])
    else:
        url.append(u)

data = {
    "Title": re.findall(r'">(.+?)</a>', read),
    "URL": url
}

df = pd.DataFrame(data, columns= ['Title', 'URL'])
df.to_csv(outputFileName, index=False)

print(df)


