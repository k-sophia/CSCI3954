"""
Test driver for Program 47
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import p47

from sklearn.manifold import MDS
from scipy.spatial.distance import cdist
import p47
#Helper function to display plots:
def displayPlot(vote2d,title):
    sns.scatterplot(data = vote2d,x="x", y="y", hue="party",
                    hue_order=['Democrat', 'Republican', 'Libertarian']);
    plt.title(title)
    plt.show()
df = pd.read_csv('vote_pivot.csv')
votes = df.drop('member',axis=1).to_numpy()
legs = pd.read_csv('legislators.csv')[['leg_id','party']]

#Fit to Euclidean distances:
#Expected plot votes_mds_euclid.png
md_fit = p47.makeMDS(votes)
vote2d = p47.makeDisplayDF(df,md_fit,legs)
displayPlot(vote2d,'MDS of Votes with Eucidean Distances')

#Fit to Hamming distances:
#Expected plot shown in votes_mds_hamming.png
md_fit = p47.makeMDS(votes, metric="hamming")
vote2d = p47.makeDisplayDF(df,md_fit,legs)
displayPlot(vote2d,'MDS of Votes with Hamming Distances')

#Fit to Manhattan distances:
#Expected plot shown in votes_mds_manhattan.png
md_fit = p47.makeMDS(votes, metric="cityblock")
vote2d = p47.makeDisplayDF(df,md_fit,legs)
displayPlot(vote2d,'MDS of Votes with Manhattan Distances')