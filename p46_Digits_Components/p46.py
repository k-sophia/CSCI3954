"""
Name: Kelly Camacho
Email: kelly.camacho02@myhunter.cuny.edu
Resources: No Resources Used
"""

import pandas as pd
import numpy as np
from sklearn.decomposition import PCA

def approxDigits(numComponents, coefficients, mean, components):
    data = mean

    for i in range(0, numComponents):
        data += coefficients[i] * components[i]
        
    return data