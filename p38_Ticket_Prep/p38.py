"""
Resources: No Resources Used
"""

import pandas as pd
import numpy as np

'''
If reg is coded as passenger 'PAS' or commercial 'COM', return those values. 
Otherwise, return 'OTHER'.
'''
def cleanReg(reg):
    if(reg == 'PAS' or reg == 'COM'):
        return reg

    return 'OTHER'


'''
Return the following for the values of c:
    'GRAY': for GY, GRAY, GREY,SILVE, SIL, SL,
    'WHITE': for WH, WHITE,
    'BLACK': for BK, BLACK, BL,
    'BLUE': for BLUE,
    'RED': for RED, RD,
    'GREEN': for GR, GREEN,
    'BROWN': for BROWN, TAN,
    Otherwise, return 'OTHER'.
'''
def cleanColor(c):
    if(c == 'GY' or c == 'GRAY' or c == 'GREY' or c == 'SILVE' or c == 'SIL' or c == 'SL'):
        return 'GRAY'

    if(c == 'WH' or c == 'WHITE'):
        return 'WHITE'

    if(c == 'BK' or c == 'BLACK' or c == 'BL'):
        return 'BLACK'

    if(c == 'BLUE'):
        return 'BLUE'

    if(c == 'RED' or c == 'RD'):
        return 'RED'

    if(c == 'GR' or c == 'GREEN'):
        return 'GREEN'

    if(c == 'BROWN' or c == 'TAN'):
        return 'BROWN'

    return 'OTHER'