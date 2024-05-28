"""
Test driver for Program 36
"""

import pandas as pd
import numpy as np
import p36

'''
Expected output:
                                        Num_Submissions                                          Locations
Restaurant Name
BLUESPOON COFFEE                                      1                [76 CHAMBERS STREET, Manhattan, NY]
Black Fox Coffee                                      2  [45 East 45th, Manhattan, NY, 70 Pine Street, ...
Black Press Coffee                                    1                  [274 Columbus Ave, Manhattan, NY]
Blackstone Coffee Roasters                            1                 [502 Hudson Street, Manhattan, NY]
Blank Slate Coffee + Kitchen (Midtown)                1                    [941 2nd Avenue, Manhattan, NY]
Blank Slate Coffee + Kitchen (NoMad)                  1                [121 Madison Avenue, Manhattan, NY]
Blue Bottle Coffee                                    1              [450 West 15th street, Manhattan, NY]
Blue Bottle Coffee Gramercy                           1                    [257 Park Ave S, Manhattan, NY]
Daniels Coffee and more                               1                     [1050  3rd ave, Manhattan, NY]
FOREVER COFFEE BAR                                    1              [714 WEST  181 STREET, Manhattan, NY]
GREGORY'S COFFEE                                      1                   [80 BROAD STREET, Manhattan, NY]
GREGORYS COFFEE                                       2  [551 FASHION AVENUE, Manhattan, NY, 485 LEXING...
GROUND CENTRAL COFFEE COMPANY                         1                      [888 8 AVENUE, Manhattan, NY]
Gregorys Coffee                                      18  [58 West 44th, Manhattan, NY, 649 Broadway, Ma...
JOE: THE ART OF COFFEE                                1              [405 WEST   23 STREET, Manhattan, NY]
Kuro Kuma Espresso & Coffee                           1               [121 La Salle Street, Manhattan, NY]
Lenox Coffee                                          1             [60  West 129th street, Manhattan, NY]
Partners Coffee                                       1                 [44 Charles Street, Manhattan, NY]
Patent Coffee / Patent Pending                        1               [49 West 27th Street, Manhattan, NY]
Ralph's Coffee                                        1                [888 Madison Avenue, Manhattan, NY]
STUMPTOWN COFFEE ROASTERS                             1               [30 WEST    8 STREET, Manhattan, NY]
Starbucks Coffee                                      2                     [605 Third Ave, Manhattan, NY]
Starbucks Coffee Company                              1                     [684  6th ave , Manhattan, NY]
THINK COFFEE                                          1              [500 WEST   30 STREET, Manhattan, NY]
jacks stir brew coffee                                1             [10  10 downing street, Manhattan, NY]
le cafe coffee                                        5  [1440 broadway, Manhattan, NY, 7  east 14 st, ...
'''
df = pd.read_csv('applications_coffee_truncated.csv')
newDF = p36.restaurantLocs(df)
print(newDF)