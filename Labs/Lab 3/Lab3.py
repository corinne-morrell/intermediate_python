# Cori Hatley
# 09-15-20
# Visualize predator-prey capture dynamics with matplotlib
# To run, enter python Lab3.py

import matplotlib as plt

def calcTime(time, dt, acc_init, exhaust):
    '''Generates a range of time values from 0 to 45 seconds in 0.1 s intervals and appends the values to a list'''
    t_previous = 0
    t_current = []
    for time in range(10):
        t_previous = t_previous + dt
        t_current.append(t_previous)
    return t_current


def calcPredator_displacement(acc_init, exhaust):
    time = t_current
    acc_current = acc_init + exhaust * time
    print(acc_current)

#def calcPrey_displacement():

def main():
    t_init = 0
    dt = 0.1
    t_current = calcTime(t_init, dt)

    calcPredator_displacement(10, -0.55)

    #plt.plot(t_current, dis_predator)
    #plt.plot(t_current, dis_prey)

main()