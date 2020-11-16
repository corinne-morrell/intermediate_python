# chessboard.py -- Uses the Zelle Graphics package to draw a chessboard. This requires
# nested loops (to automate construction of all of the rectangles along the rows and columns 
# of the board) and some computational thinking to help us decide within the loop whether 
# each rectangle should be red or black. 
#
# Caitrin Eaton
# Intermediate Python
# Fall 2020
# 
# To run in the terminal: python3 chessboard.py

import graphics

def create_board( win ):
    ''' Use the Graphics package to draw an 8x8 chessboard of red and black Rectangles.
    Requires a reference to the GraphWin, win, in which the board should be drawn.
	Returns a nested list of references to all Rectangles.'''

	# TODO: Build a chessboard from red and black Rectangle objects by looping over all 8 columns within all 8 rows (nested loop)
	
    # Things to consider: 
    # -- The top left corner of the first box can be at (0, 0).
    # -- What are the coordinates of its bottom right corner?
    # -- How much does the X coordinate change from column to column? (You chose this width, above.)
    # -- How much does the Y coordinate change from row to row? (You chose this height, above.)
    # -- How can we alternate colors?

    board = []


    return board


def main(): 
    ''' Make the window appear to be filled with graph paper, then draw some shapes
    on top of it, to demonstrate some basic functionality of the Zelle Graphics package. '''

    # Construct a window (a GraphWin object) in which to draw shapes
    winWidth = 400
    winHeight = 600
    win = graphics.GraphWin( "Chessboard", winWidth, winHeight)

    # Make sure that we can draw one rectangle and fill it with a color
    top_left = graphics.Point( 100, 100 ) 
    bottom_right = graphics.Point( 150, 200 )
    r = graphics.Rectangle( top_left, bottom_right )
    r.setFill( "darkorchid" )
    r.draw( win )

    # Draw the chessboard
    board = create_board( win )

	# Wait for the user to click their mouse in the window, the close
    win.getMouse()
    win.close()
    

if __name__ == "__main__":
    main()
