"""
Test driver for Program 35
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import p35


'''
Expected output:   
         Summons Number Registration State  ... Plate ID  NY
0            1454437777                 99  ...  GPM6410   0
1            1459682567                 NY  ...  JGJ7440   1
2            1456168186                 NY  ...  GVA5471   1
3            1456655127                 NY  ...  JLH5263   1
4            1457203959                 NY  ...  HXL2432   1
...                 ...                ...  ...      ...  ..
6942292      2002620428                 NY  ...  KJC7708   1
6942293      6021025209                 NY  ...  KLN1112   1
6942294      1477942397                 NY  ...  HAB8482   1
6942295      1472568643                 NY  ...  DXB8276   1
6942296      1478409680                 NY  ...  JHA8797   1

[6942297 rows x 7 columns]
Of the 6942297 violations for first half of 2021 for Upper East Side (PD District 19),
       5183535 are for cars registered in New York.
'''
df = pd.read_csv('Parking_Violations_Issued_Precinct_19_2021.csv',low_memory=False)
df['Issue Date'] = pd.to_datetime(df['Issue Date'])
dff = p35.addIndicator(df)
print(dff)
print(f'Of the {len(dff)} violations for first half of 2021 for Upper East Side (PD District 19),\n \
      {len(dff[dff.NY == 1])} are for cars registered in New York.')

'''
Expected output:
         Summons Number Registration State Issue Date  ...  Plate ID NY RED
0            1454437777                 99 2021-01-01  ...   GPM6410  0   0
1            1459682567                 NY 2021-01-01  ...   JGJ7440  1   0
2            1456168186                 NY 2021-01-01  ...   GVA5471  1   0
3            1456655127                 NY 2021-01-01  ...   JLH5263  1   0
4            1457203959                 NY 2021-01-01  ...   HXL2432  1   0
...                 ...                ...        ...  ...       ... ..  ..
6942292      2002620428                 NY 2021-06-29  ...   KJC7708  1   0
6942293      6021025209                 NY 2021-06-29  ...   KLN1112  1   0
6942294      1477942397                 NY 2021-06-30  ...   HAB8482  1   0
6942295      1472568643                 NY 2021-06-30  ...   DXB8276  1   0
6942296      1478409680                 NY 2021-06-30  ...   JHA8797  1   0

[6942297 rows x 8 columns]
'''
dfff = p35.addIndicator(dff, colName = 'Vehicle Color', indicator="RED")
print(dfff)
plt.xlim(pd.to_datetime("01/01/21"),pd.to_datetime("06/30/21"))
sns.histplot(data=dfff, x = 'Issue Date', hue = 'RED', binwidth = 7)
plt.title('Parking violations for Upper East Side, Jan-Jul 2021')
# expected plot shown in parking_red.png
plt.show()