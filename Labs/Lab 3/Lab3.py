# Cori Hatley
# 09-15-20
# Visualize predator-prey capture dynamics with matplotlib
# To run, enter python Lab3.py

import matplotlib.pyplot as plt
import numpy as np

def trajectoryCheetah():
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
    cycles = 449

    for t in range (0, cycles):
        updated_time = time_current[t] + delta_time
        time_current.append(updated_time)
    
        updated_acc_cheetah = acc_init_cheetah + (exhaustion_cheetah * time_current[t])
        acc_current_cheetah.append(updated_acc_cheetah)
    
        updated_vel_cheetah = max(0, min(vel_init_cheetah + acc_current_cheetah[t] * delta_time, vel_max_cheetah))
        vel_current_cheetah.append(updated_vel_cheetah)
        vel_init_cheetah = updated_vel_cheetah

        updated_dis_cheetah = dis_init_cheetah + vel_current_cheetah[t] * delta_time
        dis_current_cheetah.append(updated_dis_cheetah)
        dis_init_cheetah = updated_dis_cheetah

    return dis_current_cheetah

def trajectoryGazelle():
    time_current = [0.0]
    acc_current_gazelle = [4.5]
    vel_current_gazelle = [0.0]
    dis_current_gazelle = [20.0]

    vel_init_gazelle = 0.0
    vel_max_gazelle = 27.0
    acc_init_gazelle = 4.5
    exhaustion_gazelle = -0.05
    dis_init_gazelle = 20.0

    delta_time = 0.1
    cycles = 449

    for t in range (0, cycles):
        updated_time = time_current[t] + delta_time
        time_current.append(updated_time)
    
        updated_acc_gazelle = acc_init_gazelle + (exhaustion_gazelle * time_current[t])
        acc_current_gazelle.append(updated_acc_gazelle)
    
        updated_vel_gazelle = max(0, min(vel_init_gazelle + acc_current_gazelle[t] * delta_time, vel_max_gazelle))
        vel_current_gazelle.append(updated_vel_gazelle)
        vel_init_gazelle = updated_vel_gazelle

        updated_dis_gazelle = dis_init_gazelle + vel_current_gazelle[t] * delta_time
        dis_current_gazelle.append(updated_dis_gazelle)
        dis_init_gazelle = updated_dis_gazelle

    return dis_current_gazelle

def main():

    time = np.arange(0, 45, 0.1)
    cheetah_path = trajectoryCheetah()
    gazelle_path = trajectoryGazelle()

    plt.figure('Predator-Prey Capture Dynamics')
    plt.title('Cheetah vs. Gazelle')
    plt.xlabel('Time (s)')
    plt.ylabel('Displacement (m)')
    plt.plot(time, cheetah_path)
    plt.plot(time, gazelle_path)
    plt.grid(True)
    plt.show()

main()