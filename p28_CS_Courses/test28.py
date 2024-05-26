"""
Test driver for Program 28
"""

import numpy as np
import pandas as pd
import p28

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

CS courses:
 ['csci150', 'csci160', 'csci235', 'csci265', 'csci335', 'csci39542', 'csci49362', 'csci499']
'''

classDF = pd.DataFrame({'Name': ["Ana","Bao","Cara","Dara","Ella","Fatima"],\
                         '# Credits': [45,50,80,115,30,90],\
                         'Current Courses': ["csci160 csci235 math160 jpn201",\
                                             "csci160 csci235 cla101 germn241",\
                                             "csci265 csci335 csci39542 germn241",\
                                             "csci49362 csci499",\
                                             "csci150 csci235 math160",\
                                             "csci335 csci39542 cla101 dan102"]})


print(f'Starting df:\n {classDF}\n')
print(f'CS courses:\n {p28.csCourses(classDF)}')