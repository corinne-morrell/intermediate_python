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

def init_pop():
    # Initialize population by populating current_pop list with 6000 males and 6000 females
    initial_pop = []

    males = 1
    while males <= 6:
        initial_pop.append('m')
        males += 1

    females = 1
    while females <= 6:
        initial_pop.append('f')
        females += 1

def sim_one_year(init_pop):
    '''Simulates a colony of emperor penguins over 1 year by checking for warm conditions and determining
    adult/chick survival rates depending on warm/not warm then appends the surviving penguins to the next year's population'''

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

    # Initialize current and next populations
    init_pop = []
    next_pop = []

    # If adult survives (based on survival rate determined by warm/non-warm year), append the adult from init_pop to next_pop
    penguin = 0
    while penguin < len(init_pop):
        if random.random() < adult_survival:
            next_pop.append(init_pop[penguin])
        penguin += 1

    # Count breeding pairs
    num_m = next_pop.count('m')
    num_f = next_pop.count('f')
    num_pairs = min(num_m, num_f)

   # If chick survives (based on survival rate determined by warm/non-warm year), append a randomly-gendered chick to next_pop
    breeding_pairs = 0
    while breeding_pairs <= num_pairs:
        if random.random() < chick_survival:
            chick = random.choice(['m', 'f'])
            next_pop.append(chick)
        breeding_pairs += 1

    return next_pop[:]

def sim_one_trial(initial_pop):
    
    #moved lines 60-70 from sim_one_year because Prof. Eaton pointed out that it will re-write my next_pop and start with current_pop for every year
    #now the problem is that lines 37 and 39 depend on current_pop, an empty list, how do I fix this?

    trial_pairs = []
    num_m = initial_pop.count('m')
    num_f = initial_pop.count('f')
    num_pairs = min(num_m, num_f)
    trial_pairs.append(num_pairs)

    year = 0
    no_pairs = 0
    while no_pairs < trial_pairs and year <= 200:
        sim_one_year()
        num_m = pop.count('m')
        num_f = pop.count('f')
        num_pairs = min(num_m, num_f)
        # add trial_pairs.pop(*) to empty out previous values???
        trial_pairs.append(num_pairs)
        year += 1

test_pop = sim_one_year
sim_one_trial(test_pop)