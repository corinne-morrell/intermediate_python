# Cori Hatley
# Lab 6: Scientific Data Visualization
# Intermediate Python
# 10-06-20
# To run, enter python Lab6.py -i filename -x x-column -y y-column

import os
import sys, getopt
import matplotlib.pyplot as plt

def read_file(filename):
    ''' Returns a list of strings in which each element is one line
    from the file. The filename must be a string. Assumes that the
    file is in the same directory as the program. '''
    # print('File name: ', filename)
    # Format file path
    current_directory = os.path.dirname( __file__ )
    filepath = os.path.join( current_directory, filename )

    # Open the file for reading ("r")
    input_file = open( filepath, "r" )

    # Store each line as an element in the list
    row_list = []
    row = input_file.readline()
    while len( row ) > 0:	
        row_list.append( row )
        row = input_file.readline()

    input_file.close()

    return row_list

def plot(x_header, y_header, columns):
    
    # Plot figures
    fig, ax = plt.subplots(1,2)

    ax[0].plot(columns[0], columns[1], 'bo')
    ax[0].set_title("Scatterplot")
    ax[0].set_xlabel(x_header)
    ax[0].set_ylabel(y_header)
    ax[0].grid()

    ax[1].bar(columns[0], columns[1])
    ax[1].set_title("Bar Graph")
    ax[1].set_xlabel(x_header)
    ax[1].set_ylabel(y_header)

def viz_data(filename, x, y):

    # Call read_file to get row_list
    row_contents = read_file(filename)
    row_length = len(row_contents)
    
    # Breaks up row_list into seperate lists for each row
    for row_number in range(row_length):
        row_contents[row_number] = row_contents[row_number].strip().split( "," )
    
    # Separate headers from row contents
    x_header = row_contents[0][x]
    y_header = row_contents[0][y]
    row_contents = row_contents[1:]
    row_length = len(row_contents)

    # Format contents to floats
    for row_num in range(len(row_contents)):
        for data in range(len(row_contents[row_num])):
            row_contents[row_num][data] = float(row_contents[row_num][data])

    # Append values from row lists into column lists by indexing each value in row contents
    columns = []
    for value in [x, y]:
        column = []
        for row in range(row_length):
            column.append(row_contents[row][value])
        columns.append(column)

    print('X Header:', x_header)
    print('Y Header:', y_header)
    print('X Column:', columns[0])
    print('Y Column:', columns[1])

    plot(x_header, y_header, columns)


def main(argv):
    
    argv = argv[1:]
    filename = ''
    x_col = 0
    y_col = 1
    try:
        opts, args = getopt.getopt(argv, "hi:x:y:")
    except getopt.GetoptError:
        print("test.py -i <filename> -x <x_column> -y <y_column>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            print("usage: test.py -i <filename> -x <x_column> -y <y_column>")
            sys.exit()
        elif opt == "-i":
            filename = arg
        elif opt == "-x":
            x_col = int(arg)
        elif opt == "-y":
            y_col = int(arg)
    print('Input file is "{0}", X Column: {1}, Y Column: {2}.'.format(filename, x_col, y_col))
    
    viz_data(filename, x_col, y_col)

if __name__ == "__main__":
    main(sys.argv)
    plt.show()