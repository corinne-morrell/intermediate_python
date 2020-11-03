# animation_test.py -- A minimalistic example of Zelle's graphics objects' move() method, in action.
#
# Using Jonathan Zelle's graphics.py graphics package, available at: https://mcsp.wartburg.edu/zelle/python/ 
#
# Caitrin Eaton
# Intermediate Python
# Fall 2020

import time
import graphics
import random

def animation_test():
	win = graphics.GraphWin( "Animation Test", 600, 400 )
	circ = graphics.Circle( graphics.Point(100,200), 20 )
	circ.draw( win )
	for frame in range( 100 ):
		dx = 3
		dy = random.randint( -2, 2 )
		circ.move( dx, dy )
		print(frame, "center:", circ.getCenter())
		time.sleep( 0.05 )	# human-friendly animation speed
	win.getKey()

if __name__=="__main__":
	animation_test()
