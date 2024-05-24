"""
Name: Kelly Camacho
Email: kelly.camacho02@myhunter.cuny.edu
Resources: geeksforgeeks for np.log and tuple
"""

import pandas as pd
import numpy as np

def dropNeg(xS,yS):
    temp = zip(xS, yS)
    tempX = []
    tempY = []

    for t in tuple(temp):
        if(t[0] > 0 and t[1] > 0):
            tempX.append(t[0])
            tempY.append(t[1])
            
    return tempX, tempY

def logScale(xS,yS):
    temp = zip(xS, yS)
    tempX = []
    tempY = []

    for t in tuple(temp):
        tempX.append(np.log(t[0]))
        tempY.append(np.log(t[1]))
        
    return tempX, tempY