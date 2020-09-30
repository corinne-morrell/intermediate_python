# command_line_parameters.py -- A quick example of command line parameters
# 		in Python. 
# 
# To run this example, type in the terminal:
# 		python3 command_line_paramjeters.py followed by some stuff literally any stuff
# Note that "python3" might be something else on your machine ("python", "py", etc.)
#
# Caitrin Eaton
# Intermediate Python
# Fall 2020
# 
# This example is based on the tutorial at: 
# https://www.tutorialspoint.com/python/python_command_line_arguments.htm 
# Follow this link for some helpful text about this code sample :)

import sys

def test_cmdline( argv ):
	''' Accepts a list of command line arguments, argv, and 
	prints them out in a few different ways to help the user
	get a feel for what command line arguments are. '''

	print("len(argv) =", len(argv))		# How many elements are there?
	print("argv =", argv )				# What are the elements?
	print("program name:", argv[0] )	# The first element is always the name of the program that was executed from the terminal
	print("other stuff:", argv[1:] )	# The rest is whatever the user typed after "python3 command_line_parameters.py"


if __name__ == "__main__":
	test_cmdline( sys.argv )