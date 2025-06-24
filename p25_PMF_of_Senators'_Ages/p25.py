"""
Resources: tutorialspoint.com for Counter
"""

import pandas as pd
from collections import Counter

#return two iterables of positive numbers
#uniqueVals: a sorted list of the unique values from the input parameter vals, and
#mass: the fraction that each uniqueVals occurs in vals.
def pmf(vals):
    uniqueVals = []
    mass = []
    data = Counter(vals)

    for d in data:
        uniqueVals.append(d)
        mass.append(data[d]/len(vals))

    return uniqueVals,mass


def sum(mass):
    count = 0.0

    for m in mass:
        count += m

    return count