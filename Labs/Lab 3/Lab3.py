# Cori Hatley
# 09-15-20
# Visualize predator-prey capture dynamics with matplotlib
# To run, enter python Lab3.py

import matplotlib.pyplot as plt
import numpy as np

def trajectoryCheetah():
    ''' Calculates all relevent values for cheetah's trajectory (time, acceleration, velocity, and displacement)
    and returns displacement in a list
    '''
    # Create lists
    time_current = [0.0]
    acc_current_cheetah = [10.0]
    vel_current_cheetah = [0.0]
    dis_current_cheetah = [0.0]

    # Establish initial conditions
    vel_init_cheetah = 0.0          # m/s
    vel_max_cheetah = 29.0          # m/s
    acc_init_cheetah = 10.0         # m/s**2
    exhaustion_cheetah = -0.55      # m/s**3
    dis_init_cheetah = 0.0          # m

    # Establish time intervals
    delta_time = 0.1                # s
    cycles = 449                    # time_init + cycles * dt = 45 s

    # Generate values to populate the lists
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

    # Return the list to be used in function call to plot
    return dis_current_cheetah

def trajectoryGazelle():
    ''' Calculates all relevent values for gazelle's trajectory (time, acceleration, velocity, and displacement)
    and returns displacement in a list
    '''

    #Create lists
    time_current = [0.0]
    acc_current_gazelle = [4.5]
    vel_current_gazelle = [0.0]
    dis_current_gazelle = [20.0]

    # Establish initial conditions
    vel_init_gazelle = 0.0          # m/s
    vel_max_gazelle = 27.0          # m/s
    acc_init_gazelle = 4.5          # m/s**2
    exhaustion_gazelle = -0.05      # m/s**3
    dis_init_gazelle = 20.0         # m

    # Establish time intervals
    delta_time = 0.1                # s
    cycles = 449                    # time_init + cycles * dt = 45 s

    # Generate values to populate the lists
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

    # Return the list to be used in function call to plot
    return dis_current_gazelle

def main():

    # Generate times for x-values
    time = np.arange(0, 45, 0.1)

    # Call functions for y-values
    cheetah_path = trajectoryCheetah()
    gazelle_path = trajectoryGazelle()

    # Label and plot the figure
    plt.figure('Predator-Prey Capture Dynamics')
    plt.title('Cheetah vs. Gazelle')
    plt.xlabel('Time (s)')
    plt.ylabel('Displacement (m)')
    plt.plot(time, cheetah_path)
    plt.plot(time, gazelle_path)
    plt.legend(['Cheetah', 'Gazelle'])
    plt.grid(True)
    plt.show()

main()