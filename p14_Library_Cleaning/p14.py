"""
Name: Kelly Camacho
Email: kelly.camacho02@myhunter.cuny.edu
Resources: No resources
"""

import pandas as pd
import re

#function 1
def extractLatLon(row):
    latlon = row['the_geom'][7:-1].split()

    data = (
        float(latlon[0]),
        float(latlon[1])
    )

    return data


#function 2
def extractTitle(row):
    return row['NAME'] + ', ' + row['CITY'] + ', ' + str(row['ZIP'])