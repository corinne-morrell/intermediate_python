import graphics

def testRectangle():

    # Construct a window (a GraphWin object) in which to draw shapes
    winWidth = 400
    winHeight = 600
    win = graphics.GraphWin( "Draw Something Prep", winWidth, winHeight )

    head = Rectangle(Point(100, 200), Point(300, 400))

    
    # Draw the Circle in the window
    head.draw( win )

	# Wait for the user to click their mouse in the window, the close
    win.getMouse()
    win.close()

def drawRobot():
    
    

if __name__ == "__main__":
    testRectangle()
