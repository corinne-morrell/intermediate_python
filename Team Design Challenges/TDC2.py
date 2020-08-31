# Cori Hatley
# 08-31-20
# Visualize equations using less code than Lab 1 by implementing functions

import math
import matplotlib.pyplot as plt
import numpy as np

# Part 1 - visualize sine wave
def plotSine(a, b, c, d):
    ''' Returns the graph of the sine function when given an independent variable x along with
    variables a, b, c, and d which translate the basic function'''
    x = np.linspace(0, 14, 1000)
    sine = a*np.sin(b*x-c)+d

    # Label the axes and title the figure
    plt.figure('Sine Wave Figure')
    plt.title('The Sine Wave')
    plt.xlabel('x [radians]')
    plt.ylabel('Sin(x)')

    # Graph the output on a grid
    plt.plot(x, sine)
    plt.grid()
    plt.show()

    return sine

plotSine(1, 1, 0, 0)

# Part 2 - visualize the Heaviside function
def plotHeaviside():
    '''Returns the graph of the Heaviside function when given an independent variable x'''
    x_array = np.arange(-10, 10, 1)
    
    # Define the piecewise function
    for x in x_array:
        if x < 0:
            h = 0
        else:
            h = 1
    
    # Label the axes and title the figure
    plt.figure('Heaviside Figure')
    plt.title('The Heaviside Function')
    plt.xlabel('x')
    plt.ylabel('H(x)')

    # Graph the output on a grid
    plt.plot(x, h)
    plt.grid()
    plt.show()

    return h

   
plotHeaviside()





