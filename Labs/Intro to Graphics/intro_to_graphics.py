# intro_to_graphics.py -- A minimalistic example of Zelle's graphics objects in action.
#
# Using Jonathan Zelle's graphics.py graphics package, available at: https://mcsp.wartburg.edu/zelle/python/ 
#
# Caitrin Eaton
# Intermediate Python
# Fall 2020

import graphics
import time
import random

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

def drawRobot():
    # Construct a window (a GraphWin object) in which to draw shapes
    winWidth = 400
    winHeight = 600
    win = graphics.GraphWin( "Draw Something Prep", winWidth, winHeight )

    head = graphics.Rectangle(graphics.Point(100, 200), graphics.Point(300, 400))

    leftEye = graphics.Circle(graphics.Point(150, 250), 20)
    rightEye = graphics.Circle(graphics.Point(250, 250), 20)
    leftPupil = graphics.Circle(graphics.Point(150, 260), 8)
    rightPupil = graphics.Circle(graphics.Point(250, 260), 8)

    mouth = graphics.Rectangle(graphics.Point(125, 325), graphics.Point(275, 375))
    mouthLine1 = graphics.Line(graphics.Point(125, 350), graphics.Point(275, 350))
    mouthLine2 = graphics.Line(graphics.Point(200, 325), graphics.Point(200, 375))
    mouthLine3 = graphics.Line(graphics.Point(175, 325), graphics.Point(175, 375))
    mouthLine4 = graphics.Line(graphics.Point(150, 325), graphics.Point(150, 375))
    mouthLine5 = graphics.Line(graphics.Point(225, 325), graphics.Point(225, 375))
    mouthLine6 = graphics.Line(graphics.Point(250, 325), graphics.Point(250, 375))

    leftAntenna = graphics.Rectangle(graphics.Point(140, 150), graphics.Point(160, 200))
    rightAntenna = graphics.Rectangle(graphics.Point(240, 150), graphics.Point(260, 200))
    
    # Draw the Circle in the window
    head.draw( win )
    leftEye.draw( win )
    rightEye.draw( win )
    leftPupil.draw( win )
    rightPupil.draw( win )
    mouth.draw( win )
    mouthLine1.draw( win )
    mouthLine2.draw( win )
    mouthLine3.draw( win )
    mouthLine4.draw( win )
    mouthLine5.draw( win )
    mouthLine6.draw( win )
    leftAntenna.draw ( win )
    rightAntenna.draw ( win )

    for frame in range( 100 ):
        dx = random.randint( -3, 3)
        dy = 0
        leftAntenna.move( dx, dy )

        dx = random.randint( -3, 3)
        dy = 0
        rightAntenna.move( dx, dy )
        time.sleep( 0.05 )	# human-friendly animation speed

	# Wait for the user to click their mouse in the window, the close
    win.getMouse()
    win.close()

    

if __name__ == "__main__":
    #testCircle()
    drawRobot()
