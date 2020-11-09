# test_checkKey.py -- Demo GraphWin.checkKey() and GraphWin.checkMouse() by displaying
# key codes in the graphics window and printing mouse click coordinates to the terminal.
#
# Caitrin Eaton 
# Intermediate Python
# Fall 2020
#
# To run in the terminal: python test_checkKey.py
#
# USAGE NOTES:
# This program tests the results of GraphWin.checkKey()
# Press any key to see its corresponding GraphWin.checkKey() return value.
# Click anywhere in the window to see the corresponding GraphWin.checkMouse() return value.
# Press 'q' to quit.

import graphics as gr
import random


def test_checkKey():
	""" Displays the result of GraphWin.checkKey(), in a loop. """
	
	# Construct the window in which the animation will appear
	win = gr.GraphWin("Press 'q' to quit", 300, 300, autoflush=False)
	
	# Display a welcome message with instructions
	instructions = "Click, then\npress any key"
	x = win.getWidth()/2
	y = win.getHeight()/2
	message = gr.Text( gr.Point(x,y), str(instructions) )
	message.setSize( 34 )
	message.setFace( "helvetica" )
	message.draw( win )
	win.getMouse()
	
	# Display key presses in the graphics window, and print mouse click 
	# coordinates to the terminal.
	mouse = None
	key = None
	frame_rate = 5	# frames per second
	while key != "q":
		
		# Check for key press
		key = win.checkKey()
		message.setText( key )
		
		# Check for mouse click
		mouse = win.checkMouse()
		if mouse != None:
			print( mouse )
			
		# Refresh the window
		gr.update( frame_rate )
	
	# Let the user decide when to close the window
	message.setText( "Click to exit" )
	win.update()
	win.getMouse()
	win.close()
	
if __name__ == "__main__":
	test_checkKey()
