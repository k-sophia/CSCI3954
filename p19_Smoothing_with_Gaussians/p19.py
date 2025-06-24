"""
Resources: w3schools.com for numpy array  
           docs.scripy.org for scipy.norm.pdf
"""

import pandas as pd
import numpy as np
from scipy.stats import norm

def computeSmoothing(xes,points):
    data = np.zeros(xes.size)

    for p in points:
        data += norm.pdf(xes, loc=p, scale=0.5)

    return data