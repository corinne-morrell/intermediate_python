# Cori Hatley
# 08-26-2020
# Find the elusive limit (as x approaches zero) by graphing

import math
import matplotlib.pyplot as plt
import numpy as np

# Get x values
x = np.linspace(0, 0.01, 10000)

# Get y values
y = ((np.sin(np.tan(x)))-(np.tan(np.sin(x))))/((np.arcsin(np.arctan(x)))-(np.arctan(np.arcsin(x))))

# Label the axes and title the figure
plt.title('The Elusive Limit')
plt.xlabel('x')
plt.ylabel('F(x)')

# Define window
plt.xlim(0, 0.01)
plt.ylim(-2, 3)

# Graph the output on a grid
plt.plot(x, y)
plt.grid(True)

# Display the figure
plt.show()