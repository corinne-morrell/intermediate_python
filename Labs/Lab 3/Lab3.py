# Cori Hatley
# 09-15-20
# Visualize predator-prey capture dynamics with matplotlib
# To run, enter python Lab3.py

import matplotlib as plt

#def calcTrajectory(vel_previous_pred, acc_init_pred, exh_pred, dis_init_pred, vel_max_prey, acc_init_prey, exh_prey, dis_init_prey, t_previous, delta_t):

time_current = [0.0]
acc_current_cheetah = [10.0]
vel_current_cheetah = [0.0]
dis_current_cheetah = [0.0]

vel_init_cheetah = 0.0
vel_max_cheetah = 29.0
acc_init_cheetah = 10.0
exhaustion_cheetah = -0.55
dis_init_cheetah = 0.0

delta_time = 0.1
total_time = 20

for t in range (0, 20):
    updated_time = time_current[t] + delta_time
    time_current.append(updated_time)
    
    updated_acc_cheetah = acc_init_cheetah + (exhaustion_cheetah * time_current[t])
    acc_current_cheetah.append(updated_acc_cheetah)
    
    updated_vel_cheetah = max(0, min(vel_init_cheetah + acc_current_cheetah[t] * delta_time, vel_max_cheetah))
    vel_current_cheetah.append(updated_vel_cheetah)
    vel_init_cheetah = updated_vel_cheetah

    updated_dis_cheetah = dis_init_cheetah + vel_current_cheetah[t] * delta_time
    dis_current_cheetah.append(updated_dis_cheetah)

    
print(time_current)
print(acc_current_cheetah)
print(vel_current_cheetah)
print(dis_current_cheetah)