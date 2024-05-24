"""
Name: Kelly Camacho
Email: kelly.camacho02@myhunter.cuny.edu
Resources: No resources
"""

import pandas as pd

#function 1
def cumulativeAverage(column):
    data = []
    temp = 0
    num = 1

    for c in column:
        data.append(float((temp + float(c))/num))
        temp += float(c)
        num += 1

    newSeries = pd.Series(data)            
    return newSeries


#function 2
def cyclicAverage(column):
    offset1 = False
    offset2 = False
    index = 0
    data = []

    for c in column:
        if ((index - 7) > 0):
            offset1 = True

        if ((index - 14) > 0):
            offset2 = True


        if(offset1 & offset2):
            data.append(float((float(c) + float(column[index - 7]) + float(column[index - 14]))/3))
            offset1 = False
            offset2 = False
            index += 1

        elif(offset1):
            data.append(float((float(c) + float(column[index - 7]))/2))
            offset1 = False
            index += 1

        else:
            data.append(c)
            index += 1
            
    newSeries = pd.Series(data)            
    return newSeries
    

#function 3
def exponentialSmoothing(column):
    data = []
    index = 0

    for c in column:
        if(index == 0):
            data.append(c)
            index += 1
        else:
            add = 0.5*(float(column[index])) + 0.5*(float(data[index - 1]))
            data.append(add)
            index += 1

    newSeries = pd.Series(data)            
    return newSeries