"""
Name: Kelly Camacho
Email: kelly.camacho02@myhunter.cuny.edu
Resources: Code/Hint from HW Description
"""

import pandas as pd
import numpy as np
import numpy.linalg as LA


def moving(transition_mx, starting_pop, num_years = 1):
    return LA.matrix_power(transition_mx, num_years) @ starting_pop


def steadyState(transition_mx, starting_pop):
    w,v = LA.eig(transition_mx)

    eigenvector = v[:, 0]/sum(v[:, 0])
    sumOfPopulation = sum(starting_pop)
    multiply = eigenvector * sumOfPopulation

    return multiply




"""
t_mx = np.array([[.7, .07, .1],
                 [.25, .9, .15],
                 [.05, .03, .75]])
pop0 = np.array([20, 40, 25])
pop1 = moving(t_mx, pop0)
print(f'Population of each state after 1 year: {pop1}')
pop100 = moving(t_mx, pop0, num_years=100)
print(f'Population of each state after 100 years: {pop100}')
pop_steady = steadyState(t_mx, pop0)
print(f'Steady state population: {pop_steady}')

t_mx2 = np.array([[0.35792119, 0.05205802],
                  [0.64207881, 0.94794198]])
pop2 = np.array([25, 32])
pop_steady2 = steadyState(t_mx2, pop2)
print(f'Steady state population: {pop_steady2}')
"""



