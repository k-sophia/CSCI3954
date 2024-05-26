"""
Name: Kelly Camacho
Email: kelly.camacho02@myhunter.cuny.edu
Resources: textbook and class slides
"""

import pandas as pd
import numpy as np
import math

'''
takes two iterables of numeric values:
    thetas: estimates for the population parameter for the percent tips in values, and
    tips: the tips observed, assumed to be a positive percentage, ranging from 0 to 100.
'''
def mse_estimates(thetas,tips):
    data = []

    for t in thetas:
        add = np.mean( (tips - t) **2 )
        data.append(add)

    return data

'''
takes two iterables of numeric values:
    thetas: estimates for the population parameter for the percent tips in values, and
    tips: the tips observed, assumed to be a positive percentage, ranging from 0 to 100.
'''
def mae_estimates(thetas,tips):
    data = []

    for th in thetas:
        temp = []

        for ti in tips:
            temp.append( abs(float(ti - th)) )
            
        add = np.mean(temp)
        data.append(add)

    return data