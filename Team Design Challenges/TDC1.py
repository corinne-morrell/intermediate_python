# Corinne Hatley
# 08-24-20

import matplotlib.pyplot as plt

#Visualize a straight line: y = mx + b

m = 0.5
b = 2

x = 0
y = m*x + b
plt.plot(x, y, 'gx')

x = 1
y = m*x+b
plt.plot(x, y, 'gx')

x = 2
y = m*x+b
plt.plot(x, y, 'gx')

x = 3
y = m*x+b
plt.plot(x, y, 'gx')

x = 4
y = m*x+b
plt.plot(x, y, 'gx')

plt.xlabel('inputs')
plt.ylabel('outputs')

# Display the figure
plt.show()