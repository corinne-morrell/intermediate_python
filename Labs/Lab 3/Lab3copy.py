# Cori Hatley
# 09-15-20
# Visualize predator-prey capture dynamics with matplotlib
# To run, enter python Lab3.py

import matplotlib as plt

#def calcTrajectory(vel_previous_pred, acc_init_pred, exh_pred, dis_init_pred, vel_max_prey, acc_init_prey, exh_prey, dis_init_prey, t_previous, delta_t):

time_current = [0]
#displacement_predator = [0.0]
#displacement_prey = [20.0]

#vel_max_pred = 29.0
acc_init_pred = 10.0
exhaustion_pred = -0.55

#vel_max_prey = 27.0
#acc_init_prey = 4.5
#exhaustion_prey = -0.05

delta_time = 0.1
total_time = 20

for t in range (0, 20):
    updated_time = time_current[t] + delta_time
    time_current.append(updated_time)
    
    acc_current_pred = acc_init_pred + (exhaustion_pred * time_current[t])
    
