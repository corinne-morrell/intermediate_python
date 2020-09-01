# Cori Hatley
# 09-08-20
# Visualize the trajectory of a ballistic projectile using functions and matplotlib


import math
import numpy as np
import matplotlib.pyplot as plt

def calcLanding_time(v, theta, g):
    landing_time = (2 * v * math.sin(theta)) / g
    return landing_time

def calcHorizontal_position(x, v, theta, t):
    x_current = x + (v * math.cos(theta) * t)
    return x_current

def calcVertical_position(y, v, theta, t, g):
    y_current = y + (v * math.sin(theta) * t) + (0.5 * g * t**2)
    return y_current
    
def main():
    x_init = 0
    y_init = 0
    acc_gravity = -9.81
    v_init = float(input('Enter initial velocity (m/s):'))
    angle_degrees = float(input('Enter launch angle (degrees):'))
    launch_angle = angle_degrees * (math.pi / 180.0)

    landing_time = calcLanding_time(v_init, launch_angle, acc_gravity)
    time = np.linspace(0, landing_time, 20)

    x1 = calcHorizontal_position(x_init, v_init, launch_angle, time)
    y1 = calcVertical_position(y_init, v_init, launch_angle, time, acc_gravity)

    plt.figure('Ballistic Projectile Figure')
    plt.title('Trajectory of a Ballistic Projectile')
    plt.xlabel('Horizontal Position (m)')
    plt.ylabel('Vertical Position (m)')
    plt.plot(x1, y1)
    plt.grid()
    plt.show()

main()