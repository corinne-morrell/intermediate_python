# Cori Hatley
# 08-26-2020
# The purpose of this lab is to visualize mathematical models using matplotlib

import math
import matplotlib.pyplot as plt
import numpy as np

# The Sine Wave
# Visualize at least two periods of a sine wave

# Define the constants where: a=amplitude, 2pi/b=period, c=phase shift, d=vertical shift
a = 0.5
b = 1
c = 0
d = 0

# Get x and y values
x = np.arange(0,4.5*math.pi,math.pi/16)
y = a*(np.sin(b*(x-c)))+d

# Label the axes and title the figure
plt.figure('Sine Wave Figure')
plt.title('The Sine Wave')
plt.xlabel('x [radians]')
plt.ylabel('Sin(x)')

# Graph the output and display on a grid
plt.plot(x, y)
plt.grid()
# Why do the grid labels not match the scale I used for x (pi/16)?

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# The Cubic Polynomial
# Visualize a cubic polynomial

# Define the constants
a = 1
b = 2
c = 5
d = 1

# Get x and y values
x = np.arange(-10,10,0.25)
y = (a*(x**3))+(b*(x**2))+(c*x)+d

# Label the axes and title the figure
plt.figure('Cubic Polynomial Figure')
plt.title('The Cubic Polynomial')
plt.xlabel('x')
plt.ylabel('F(x)')

# Graph the output on a grid
plt.plot(x, y, 'ob')
plt.grid()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# The Elusive Limit
# Find the elusive limit (as x approaches zero) by graphing

# Get x and y values
x = np.linspace(0, 0.01, 10000)
y = ((np.sin(np.tan(x)))-(np.tan(np.sin(x))))/((np.arcsin(np.arctan(x)))-(np.arctan(np.arcsin(x))))

# Label the axes, title the figure, and define the window
plt.figure('Elusive Limit Figure')
plt.title('The Elusive Limit')
plt.xlabel('x')
plt.ylabel('F(x)')
plt.xlim(0, 0.01)
plt.ylim(-2, 3)

# Graph the output on a grid
plt.plot(x, y)
plt.grid()

# Display the figures
plt.show()