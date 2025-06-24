
"""
Resources: No Resources Used
"""

import pandas as pd
import numpy as np
import random

"""
Input: the number of sides on die 1 (D1) and die2 (D2) and the number of trials
Return: an array with the percentage each possible sum of rolls occured.
"""
def diceSim(D1,D2,trials):
    sumOfDie = np.zeros(D1 + D2)

    for r in range(1, trials + 1):
        x = random.randrange(1, D1 + 1)
        y = random.randrange(1, D2 + 1)
        getSum = x + y

        sumOfDie[getSum - 1] += 1

    
    returnArr = [0.0]
    for s in sumOfDie:
        add = s/trials
        returnArr.append(add)

    return returnArr