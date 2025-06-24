"""
Resources: No Resources Used
"""

import pandas as pd

# takes as input a data frame, df, that contains a column Current Courses.
# returns a sorted list of unique strings
# each string is a computer science course (csci)
def csCourses(df):
    courses = ' '.join(df['Current Courses'].unique()).split()
    uniqueCourse = set(courses)
    uniqueCS = [x for x in uniqueCourse if "csci" in x]
    uniqueCS.sort()
    return uniqueCS