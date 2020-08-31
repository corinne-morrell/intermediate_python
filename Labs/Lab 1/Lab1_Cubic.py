# Cori Hatley
# 08-26-2020
# Visualize a cubic polynomial

import math
import matplotlib.pyplot as plt
import numpy as np

# Define the constants
a = 1
b = 2
c = 5
d = 1

# Get x values
x = np.arange(0,10,0.25)

# Get y values
y = (a*(x**3))+(b*(x**2))+(c*x)+d

# Define window
plt.xlim(0, 11)
plt.ylim(0, 1300)
#How do I specify the spacing on the axes?

# Label the axes and title the figure
plt.title('The Cubic Polynomial')
plt.xlabel('x')
plt.ylabel('F(x)')

# Graph the output on a grid
plt.plot(x, y, 'ob')
plt.grid(True)

# Display the figure
plt.show()