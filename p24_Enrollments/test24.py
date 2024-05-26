"""
Test driver for Program 24
"""

import pandas as pd
import numpy as np
import p24

'''
Expected output:

Starting df:
      Name  # Credits                     Current Courses
0     Ana         45      csci160 csci235 math160 jpn201
1     Bao         50     csci160 csci235 cla101 germn241
2    Cara         80  csci265 csci335 csci39542 germn241
3    Dara        115                   csci49362 csci499
4    Ella         30             csci150 csci235 math160
5  Fatima         90     csci335 csci39542 cla101 dan102

Ending df:
      Name  # Credits  NumCourses  CS  Other
0     Ana         45           4   2      2
1     Bao         50           4   2      2
2    Cara         80           4   3      1
4    Ella         30           3   2      1
5  Fatima         90           4   2      2
'''

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