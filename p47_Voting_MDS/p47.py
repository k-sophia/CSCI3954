"""
Name: Kelly Camacho
Email: kelly.camacho02@myhunter.cuny.edu
Resources: No Resources Used
"""

import pandas as pd
import numpy as np
from sklearn.manifold import MDS
from scipy.spatial.distance import cdist


def makeMDS(points,metric='euclidean',random_state=25):
    dist = cdist(points, points, metric)
    mds = MDS(random_state=random_state, dissimilarity='precomputed')
    return mds.fit_transform(dist)


def makeDisplayDF(df,md_fit,legs):

    data = {
        'member' : df['member'],
        'x' : md_fit[:,0],
        'y' : md_fit[:,1]
    }

    df2 = pd.DataFrame(data)
    
    legs['member'] = legs['leg_id']
    df3 = df2.merge(legs, on='member', how='left')    
    return df3