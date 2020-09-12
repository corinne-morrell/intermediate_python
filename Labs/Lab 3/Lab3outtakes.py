# Cori Hatley
# 09-15-20
# Visualize predator-prey capture dynamics with matplotlib
# To run, enter python Lab3.py

import matplotlib as plt

'''def calcTime(time, dt):
    Generates a range of time values from 0 to 45 seconds in 0.1 s intervals and appends the values to a list
    t_previous = 0.0
    t_current = [0.0]
    for time in range(10):
        t_previous = t_previous + dt
        t_current.append(t_previous)
    return t_current


def calcPredator_displacement(time):
    exhaust = [-0.55]
    acc_init = [10.0]
    acc_current = acc_init + exhaust * time
    print(acc_current)

#def calcPrey_displacement():

def main():
    t_init = 0.0
    delta_t = 0.1
    t_c = calcTime(t_init, delta_t)

    calcPredator_displacement(t_c)

    #plt.plot(t_current, dis_predator)
    #plt.plot(t_current, dis_prey)

main()
'''

time_current = [0.0]
delta_time = 0.1
cycles = 20

for t in range (0, cycles):
    updated_time = time_current[t] + delta_time
    time_current.append(updated_time)
    
print(time_current)