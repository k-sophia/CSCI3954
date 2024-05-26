"""
Name: Kelly Camacho
Email: kelly.camacho02@myhunter.cuny.edu
Resources: No Resources Used
"""

import pandas as pd
import numpy as np
import scipy.stats as st

'''
takes five inputs:
    alpha: the fraction of the distribution contained in the interval (as in scipy.stats.t.interval()); default value is 95.
    mu: the mean of the normal distribution sampled; default value is 0.
    sigma: the standard deviation of the normal distribution sampled; default value is 1.
    size: the size of the samples; default value is 10.
    trials: the number of samples; default value is 100.
    
returns:
    A list of intervals, stored as tuples of their lower and upper values (of length trials)
    A list of length trials containing the percentage of successful predictions after each trial. 
        The ith entry has the percent of the first i trials for which the true mean (mu) is in the confidence interval computed for the sample.
'''
def ciRuns(alpha = 0.95, mu = 0, sigma = 1, size = 10, trials = 100):
    interval = []
    success = []

    for t in range(1, trials+1):
        sampleData = np.random.normal(mu, sigma, size)
        add = st.t.interval(alpha,len(sampleData)-1, loc=np.mean(sampleData),scale=st.sem(sampleData))
        interval.append(add)

    num = 0.0
    for r1 in range(0, len(interval)):
        for r2 in range(0, r1+1):
            x,y = interval[r2]
            if(x <= mu <= y):
                num += 1

        getPercent = (num/(r1+1)) *  10.0
        if(getPercent > 100):
            success.append(100)
        else:
            success.append(getPercent)

    return interval, success