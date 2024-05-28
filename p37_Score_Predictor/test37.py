"""
Test driver for Program 37
"""

import pandas as pd
import numpy as np
import p37

# Expected output:
# The highest accuracy, 0.725, was obtained by including column, action_type.
df = pd.read_csv('lebron.csv')
columns = ['minute', 'action_type', 'shot_type', 'opponent']
acc,col_name = p37.bestForPredict(df,columns)
print(f'The highest accuracy, {acc}, was obtained by including column, {col_name}.')


# Expected output:
# The highest accuracy, 0.6, was obtained by including column, opponent.
columns = ['minute', 'opponent']
acc,col_name = p37.bestForPredict(df,columns, test_size = 100, random_state = 17)
print(f'The highest accuracy, {acc}, was obtained by including column, {col_name}.')