# Cori Hatley
# 09-29-2020
# Endangered Species Population Dynamics
# Objective 1: Model a colony of emperor penguins over the course of 200 years.
# Objective 2: Consider how "warm events" impact extinction and calculate average extinction over 100 trials.
# Objective 3: Determine the probability of extinction in each possible year.
# Objective 4: Visualize results by plotting years (0-200) versus probability of extinction.
# To run this program in the terminal, enter 'python Lab5.py'

import random
import matplotlib.pyplot as plt

def initial_pop(num_males, num_females):
    
    # Establish initial conditions by populating current_pop list with 6000 males and 6000 females
    current_pop = []

    males = 1
    while males <= num_males:
        current_pop.append('m')
        males += 1

    females = 1
    while females <= num_females:
        current_pop.append('f')
        females += 1
    
    return current_pop

def sim_one_year(initpop):

    # Factor in temperature and establish survival rates for warm/non-warm years
    warm_rate = 0.18
    if random.random() < warm_rate:
        warm = True
    else:
        warm = False

    if warm:
        chick_survival = 0.01
        adult_survival = 0.7
    else:
        chick_survival = 0.19
        adult_survival = 0.9

    # Initialize next population
    next_pop = []

    # If adult survives (based on survival rate determined by warm/non-warm year), append the adult from current_pop to next_pop
    index = 0
    while index < len(initpop):
        if random.random() < adult_survival:
            next_pop.append(initpop[index])
        index += 1

    # Count breeding pairs
    breeding_pairs = []
    num_m = next_pop.count('m')
    num_f = next_pop.count('f')
    num_pairs = min(num_m, num_f)
    breeding_pairs.append(num_pairs)

   # If chick survives (based on survival rate determined by warm/non-warm year), append a randomly-gendered chick to next_pop
    starting_pairs = 0
    while starting_pairs <= num_pairs:
        if random.random() < chick_survival:
            chick = random.choice(['m', 'f'])
            next_pop.append(chick)
        starting_pairs += 1

    return next_pop[:], breeding_pairs[:]

def sim_one_trial(initpop):
    
    next_pop, trial_pairs = sim_one_year(initpop)

    num_m = initpop.count('m')
    num_f = initpop.count('f')
    num_pairs = min(num_m, num_f)
    trial_pairs.append(num_pairs)

    print(len(trial_pairs))

    year = 0
    no_pairs = 0
    while no_pairs < len(trial_pairs) and year <= 200:
        num_m = next_pop.count('m')
        num_f = next_pop.count('f')
        num_pairs = min(num_m, num_f)
        trial_pairs.append(num_pairs)
        year += 1

    return trial_pairs[:]

starting_pop = initial_pop(6, 6)
one_year_test = sim_one_year(starting_pop)
one_trial_test = sim_one_trial(starting_pop)
print(one_year_test)
print(one_trial_test)