"""
Name: Kelly Camacho
Email: kelly.camacho02@myhunter.cuny.edu
Resources: inferentialthinking.com for regression
            geeks for geeks stat.stdev and pearsonr
"""

import pandas as pd
import statistics as stat
from scipy.stats import pearsonr

# takes two iterables of numeric values:
    # xes: independent variable
    # yes: dependent variable
# computes the slope and y-intercept of the linear regression line using ordinary least squares
def compute_r_line(xes, yes):
    #computer the standard deviation of the xes and yes
    sd_x = stat.stdev(xes)
    sd_y = stat.stdev(yes)

    #Compute the correlation, r, of the xes and yes.
    r, _ = pearsonr(xes, yes)
    
    #Compute the slope, m
    m = r * sd_y / sd_x
    
    #Compute the y-intercept, b
    b = yes[0] - m * xes[0]

    #round m, b
    m = round(m, 2)
    b = round(b, 2)

    #Return m and b.
    return m, b