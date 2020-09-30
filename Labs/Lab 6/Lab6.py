# Cori Hatley
# Lab 6: Scientific Data Visualization
# Intermediate Python
# 10-06-20

import os
import sys, getopt
import matplotlib.pyplot as plt

def get_metadata(filename):
    ''' Reads the first item in row_list from read_file and appends 
    each value to a list of metadata.'''

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

def viz_data(filename, x, y):
    row_contents = read_file(filename)
    row_length = len( row_contents )

    # breaks up row_list into seperate lists for each row
    for row_number in range(row_length):
        row_contents[row_number] = row_contents[row_number].strip().split( "," )


def main(argv):
    
    argv = argv[1:]
    filename = ''
    x_col = 999
    y_col = 999
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
