# Cori Hatley
# 09-08-20
# Free throw optimization
# To run, enter python TDC5.py


import math
import numpy as np
import matplotlib.pyplot as plt

def theta_range():
    '''Generates candidates for optimal launch angle and appends the values to a list'''
    launch_angle = [0]
    delta_theta = 0.01
    intervals = 157 # max angle = pi/2; (pi/2)/0.01 is approx. 157

    for theta in range(0, intervals):
        new_angle = launch_angle[theta] + delta_theta
        launch_angle.append(new_angle)
    
    return launch_angle

def velocity_range():
    '''Generates candidates for optimal launch velocity and appends the values to a list'''
    vel_init = [0]
    delta_vel = 0.01
    intervals = 1000 # max velocity is about 10m/s for shooting a basketball; 10/0.01 = 1000

    for v in range(0, intervals):
        new_vel = vel_init[v] + delta_vel
        vel_init.append(new_vel)

    return vel_init

def optimizeThrow(x_target, v, theta, g, y):
    '''Calculates x-final given the lists of all possible values for launch angle and velocity
    and checks that x-final equals the target x-value'''

    x = (v * math.cos(theta) * (-v * math.sin(theta) + math.sqrt(v**2 * (math.sin(theta)**2) + 2 * g * y))) / -g


    while x < x_target: # I don't know what I'm trying to accomplish here anymore
        if x == x_target:
            return x
        else:

'''def main():
    
    x_final = 5.8
    y_final = 1.295
    gravity = 9.81

    theta = theta_range()
    v_init = velocity_range()


main()'''