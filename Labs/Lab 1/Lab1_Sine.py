# Cori Hatley
# 08-26-2020
# Visualize at least two periods of a sine wave

import math
import matplotlib.pyplot as plt
import numpy as np

# Define the constants where: A = amplitude, 2pi/B = period
#   C = phase shift, D = vertical shift
A = 0.5
B = 1
C = 0
D = 0

# Get x values of the sine wave
x = np.arange(0,4.5*math.pi,math.pi/16)

# Get y values of the sine wave
y = A*(np.sin(B*(x-C)))+D

# Graph the output
plt.plot(x, y)

# Label the axes and title the figure
plt.title('The Sine Wave')
plt.xlabel('x (radians)')
plt.ylabel('F(x)')

# Define window
plt.xlim(0, 4.5*math.pi)
plt.ylim(-1.25, 1.25)

# Display the graph on a grid
plt.grid(True)
# Why do the grid labels not match the scale I used for x (pi/16)?

# Display the figure
plt.show()