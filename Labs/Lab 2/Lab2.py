# Cori Hatley
# 09-08-20
# Visualize the trajectory of a ballistic projectile using functions and matplotlib


import math
import numpy as np
import matplotlib.pyplot as plt

def calcLanding_time(v, theta, g):
    ''' Returns landing time of projectile given initial velocity,
    launch angle, and magnitude of acceleration due to gravity '''
    landing_time = (2 * v * math.sin(theta)) / g
    return landing_time

def calcMax_height(v, theta, g):
    ''' Returns maximum height of projectile given initial velocity,
    launch angle, and magnitude of acceleration due to gravity '''
    max_height = ((np.abs(v))**2 * (math.sin(theta))**2) / (2 * g)
    return max_height

def calcX_final(x, v, theta, t):
    ''' Returns final horizontal position of projectile given
    initial position, initial velocity, launch angle, and landing time '''
    x_final = x + (v * math.cos(theta) * t)
    return x_final

def calcHorizontal_position(x, v, theta, t):
    ''' Returns current horizontal position given initial position,
    initial velocity, launch angle, and variable time '''
    x_current = x + (v * math.cos(theta) * t)
    return x_current

def calcVertical_position(y, v, theta, t, g):
    ''' Returns current vertical position given initial position,
    initial velocity, launch angle, variable time, and acceleration
    due to gravity '''
    y_current = y + (v * math.sin(theta) * t) - (0.5 * g * t**2)
    return y_current
    
def main():
    # Establish initial position (x,y) and acceleration due to gravity
    x_init = 0
    y_init = 0
    acc_gravity = 9.81

    # Allow user inputs for initial velocity and launch angle and convert angle input from degrees to radians
    v_init = float(input('Enter initial velocity (m/s):'))
    angle_degrees = float(input('Enter launch angle (degrees):'))
    launch_angle = angle_degrees * (math.pi / 180.0)

    # Call functions to calculate trajectory of projectile
    landing_time = calcLanding_time(v_init, launch_angle, acc_gravity)
    time = np.linspace(0, landing_time, 20)
    max_height = calcMax_height(v_init, launch_angle, acc_gravity)
    x_final = calcX_final(x_init, v_init, launch_angle, landing_time)
    x_path = calcHorizontal_position(x_init, v_init, launch_angle, time)
    y_path = calcVertical_position(y_init, v_init, launch_angle, time, acc_gravity)

    # Label figure and plot trajectory on a grid
    plt.figure('Ballistic Projectile Figure')
    plt.title('Trajectory of a Ballistic Projectile')
    plt.text(x_final/4, max_height/4,
    f'Initial velocity: {v_init} m/s\nLaunch angle: {angle_degrees} \N{DEGREE SIGN}\nMaximum height: {round(max_height, 2)} m\nMaximum range: {round(x_final, 2)} m\nTotal time: {round(landing_time,2)} s')
    plt.xlabel('Range (m)')
    plt.ylabel('Height (m)')
    plt.xlim(0, 1.05*x_final)
    plt.ylim(0, 1.05*max_height)
    plt.plot(x_path, y_path)
    plt.grid()
    plt.show()


main()