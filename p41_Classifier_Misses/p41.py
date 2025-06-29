"""
Resources: stackoverflow for np.diag
"""

import pandas as pd
import numpy as np

'''
one input:
    mx: a matrix that has been generated by sklearn.metrics.confusion_matrix,

returns the label of the class that is most commonly misidentified. 
That is, the row which has the number of entries not on the diagonal of all rows. 
'''
def clf_misses(mx):
    rowSum = mx.sum(axis=1)
    sumNoDiag = rowSum - np.diag(mx)
    rowIndex= np.argmax(sumNoDiag)

    return rowIndex