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

# Part 2 - visualize the Heaviside function
def plotHeaviside():
    '''Returns the graph of the Heaviside function when given an independent variable x'''
    x_array = np.arange(-10, 10, 0.001)
    h_list = []
    
    # Define the piecewise function
    for x in x_array:
        if x < 0:
            h_list.append(0)
        else:
            h_list.append(1)
    
    h_array = np.asarray(h_list)

    # Label the axes and title the figure
    plt.figure('Heaviside Figure')
    plt.title('The Heaviside Function')
    plt.xlabel('x')
    plt.ylabel('H(x)')

    # Graph the output on a grid
    plt.plot(x_array, h_array, 'kd')
    plt.grid()

def main():
    a = 1
    b = 1
    c = 0
    d = 0
    plotSine(a, b, c, d)   
    plotHeaviside()
    plt.show()

main()





