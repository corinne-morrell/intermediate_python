# intro_to_graphics.py -- A minimalistic example of Zelle's graphics objects in action.
#
# Using Jonathan Zelle's graphics.py graphics package, available at: https://mcsp.wartburg.edu/zelle/python/ 
#
# Caitrin Eaton
# Intermediate Python
# Fall 2020

import graphics

def testCircle():

    # Construct a window (a GraphWin object) in which to draw shapes
    winWidth = 400
    winHeight = 600
    win = graphics.GraphWin( "A shiny new window!", winWidth, winHeight )

    # Construct a Point object at (100, 200). 
    # We'll use it to place a Circle object at this location in the window.
    xCenter = 200
    yCenter = 300
    pCenter = graphics.Point( xCenter, yCenter )
    
    # Construct a Circle object with its center at the point pCenter: (100, 200)
    radius = 50
    cir = graphics.Circle( pCenter, radius ) 
    
    # Uncomment the next line if you'd like to change the color of the circle
    cir.setFill( "yellow" )
    
    # Draw the Circle in the window
    cir.draw( win )
    
    # Uncomment the next line if you'd like to see pCenter in the window as well
    pCenter.draw( win )

	# Wait for the user to click their mouse in the window, the close
    win.getMouse()
    win.close()
    

if __name__ == "__main__":
    testCircle()
