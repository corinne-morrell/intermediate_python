# Cori Hatley
# 10-16-20
# TDC: Robot Navigation

import random

def build_map(rows, cols, obstacles):
    '''Returns a 2D list of integers that represents a map, in which obstacles
    are 1s and empty spaces are 0s. Accepts 3 integers as parameters that 
    determine the size (number of rows and columns) of the map, and the number
    of obstacles it contains.'''
    
    map = [] # append rows to this list
    prob_obstacle = obstacles / (rows * cols)
    obstacles_created = 0
    for row in range(rows):
        # create a new row
        map.append([])
        for col in range(cols):
            if (random.random() < prob_obstacle) and (obstacles_created < obstacles):
                map[row].append(1)
                obstacles_created += 1
            else:
                map[row].append(0)
    
    return map


def draw_map( robo_map ):
    ''' Accepts a 2D list of ints as a parameter and draws it in the terminal.
    Expects obstacles to be 1s and empty cells to be 0s. Returns nothing. '''
    
    friendly_map = []

    for i in range(len(robo_map)):
        friendly_map.append([])
        for j in range(len(robo_map[i])):
            if robo_map[i][j] == 0:
                friendly_map[i].append("   ")
            else:
                friendly_map[i].append(" | ")
    
    for k in range(len(friendly_map)):
        printable_map = ' '.join(friendly_map[k])
        print(printable_map)

print_map = build_map(20, 10, 30)
draw_map(print_map)

