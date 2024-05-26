"""
Test driver for Program 24
"""

import pandas as pd
import numpy as np
import p24

classDF = pd.DataFrame({'Name': ["Ana","Bao","Cara","Dara","Ella","Fatima"],\
                      '# Credits': [45,50,80,115,30,90],\
                      'Current Courses': ["csci160 csci235 math160 jpn201",\
                                          "csci160 csci235 cla101 germn241",\
                                          "csci265 csci335 csci39542 germn241",\
                                          "csci49362 csci499",\
                                          "csci150 csci235 math160",\
                                          "csci335 csci39542 cla101 dan102"]})

print(f'Starting df:\n {classDF}')
print(f'Ending df:\n {p24.computeEnrollments(classDF)}')