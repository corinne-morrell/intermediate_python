# Cori Hatley
# 09-29-2020
# Endangered Species Population Dynamics
# Objective 1: Model a colony of emperor penguins over the course of 200 years.
# Objective 2: Consider how "warm events" impact extinction and calculate average extinction over 1000 trials.
# Objective 3: Determine the probability of extinction in each possible year.
# Objective 4: Visualize results by plotting years (0-200) versus probability of extinction.
# To run this program in the terminal, enter 'python Lab5.py'

import random
import matplotlib.pyplot as plt

def sim_one_year():

    # Establish initial conditions by populating current_pop list with 6000 males and 6000 females
    current_pop = []

    males = 1
    while males <= 6:
        current_pop.append('m')
        males += 1

    females = 1
    while females <= 6:
        current_pop.append('f')
        females += 1
