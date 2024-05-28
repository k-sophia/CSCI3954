"""
Name: Kelly Camacho
Email: kelly.camacho02@myhunter.cuny.edu
Resources: No Resources Used
"""

import pandas as pd
import numpy as np

def restaurantLocs(df, dba="Restaurant Name", location="Business Address"):
    newDF = df.groupby(dba).agg(
        Num_Submissions = pd.NamedAgg(
            column = dba,
            aggfunc = "count"
        ),
        Locations = pd.NamedAgg(
            column = location,
            aggfunc = "unique"
        )
    )

    return newDF