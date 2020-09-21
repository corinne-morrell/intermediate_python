# Cori Hatley
# 09-08-20
# Free throw optimization
# To run, enter python TDC5.py


import math
import numpy as np
import matplotlib.pyplot as plt

def calcLanding_time(x, v, theta):
    ''' Returns landing time of projectile given initial velocity,
    launch angle, and magnitude of acceleration due to gravity. Return value
    is used as the endpoint for the range of time values required
    to calculate the path of the projectile. '''
    landing_time = x / (v * math.cos(theta))
    return landing_time

def calcHorizontal_position(x, v, theta, t):
    ''' Returns current horizontal position given initial position,
    initial velocity, launch angle, and variable time. Return value is used
    to plot the x coordinates of the projectile's path. '''
    x_current = x + (v * math.cos(theta) * t)
    return x_current

def calcVertical_position(y, v, theta, t, g):
    ''' Returns current vertical position given initial position,
    initial velocity, launch angle, variable time, and acceleration
    due to gravity. Return value is used to plot the y coordinates
    of the projectile's path. '''
    y_current = y + (v * math.sin(theta) * t) - (0.5 * g * t**2)
    return y_current
    
def main():
    # Establish initial position (x,y) and acceleration due to gravity
    x_init = 0
    y_init = 1.98
    acc_gravity = 9.81

    # Convert angle from degrees to radians
    launch_angle = angle_degrees * (math.pi / 180.0)

    # Call functions to calculate trajectory of projectile
    landing_time = calcLanding_time(v_init, launch_angle, acc_gravity)
    time = np.linspace(0, landing_time, 20)
    x_path = calcHorizontal_position(x_init, v_init, launch_angle, time)
    y_path = calcVertical_position(y_init, v_init, launch_angle, time, acc_gravity)

    # Label figure and plot trajectory on a grid
    plt.figure('Free Throw Optimization Figure')
    plt.title('Trajectory of a Free Throw')
    plt.xlabel('Range (m)')
    plt.ylabel('Height (m)')
    plt.plot(x_path, y_path)
    plt.grid()
    plt.show()


main()