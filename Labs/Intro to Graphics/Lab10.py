# Cori Hatley
# 11-10-20
# Intermediate Python
# Lab 10 - Interactive Animation

# To run from the terminal, enter python Lab10.py
	
	# Click to start. To add planets:
	# Press 'm' for Mars
	# Press 'return' to animate orbit
	# Press 'esc' to quit

import graphics as gr
import math
import time

class Planet(gr.Circle):
	'''
	Creates a Planet object with a center, radius (in pixels), color, and name.
	Inherits characteristics of the Circle class from graphics.py.
	
	'''

	def __init__(self, center, radius, color, name):
		x, y = center
		gr.Circle.__init__(self, gr.Point(x, y), radius)
		self.setFill(color)
		self.name = gr.Text(gr.Point(x, y - 1.75 * radius), name)
		self.name.setTextColor("white")

	def getName(self):
		return self.name

	def enable(self, win): # draw the Planet object in the window
		self.draw(win)
		self.name.draw(win)

	def disable(self): # undraw the Planet object
		self.undraw()
		self.name.undraw()

def createSpace():
	'''
	Creates a graphics window with a black background.
	
	Parameters: N/A
	Returns: a GraphWin object
	
	'''

	# Create a black window
	winWidth = 1000
	winHeight = 800
	win = gr.GraphWin("The Solar System", winWidth, winHeight, autoflush=False)
	win.setBackground("black")

	return win

def createSun(win):
	'''
	Creates a Circle object to represent the Sun in the center of the window.
	
	Parameters: a GraphWin object
	Returns: a Circle object at the center of the window

	'''

	xCenter = win.getWidth() / 2
	yCenter = win.getHeight() / 2
	pCenter = gr.Point(xCenter, yCenter)

	radius = 50
	sun = gr.Circle(pCenter, radius)
	name = gr.Text(pCenter, "Sun")
	name.setSize(14)

	sun.setFill("yellow")
	sun.draw(win)
	name.draw(win)

	return sun

def createMars(win, sun):
	'''
	Creates a Planet object to represent Mars and animates Mars' orbital motion around the Sun.

	Parameters: GraphWin object, object at center of orbit
	Returns: N/A

	'''

	# Initalize variables for the center of the Sun, center of Mars, and Mars' orbit radius
	solar_centerX = sun.getCenter().getX()
	solar_centerY = sun.getCenter().getY()
	mars_x = solar_centerX + 150
	mars_y = solar_centerY
	mars_orbit_radius = 150

	# Instantiate Mars as a Planet object
	mars = Planet((mars_x, mars_y), 10, "red", "Mars")

	# Initialize t and dt for animation while loop
	t = 0.0
	dt = 0.01
	
	# Initialize key variable and number of orbits completed
	key = ""
	orbits = 0

	while key != "Escape":
		key = win.getKey()
		if key == "m":
			mars.enable(win)
		if key == "Return":
			while key != "Escape":
				# Calculate points on the circular orbit of Mars and move Mars to the new coordinates
				key = win.checkKey()
				new_mars_x = solar_centerX + mars_orbit_radius * math.cos(t)
				new_mars_y = solar_centerY + mars_orbit_radius * math.sin(t)
				mars_centerX = mars.getCenter().getX()
				mars_centerY = mars.getCenter().getY()
				dx = new_mars_x - mars_centerX
				dy = new_mars_y - mars_centerY
				mars.move(dx, dy)
				mars.name.move(dx, dy)

				# Update t
				t = (t + dt) % (2 * math.pi)

				# Temporarily undraw Mars and plot orbit path
				mars.disable()

				# If new coordinates equal initial coordinates, Mars has completed one orbit
				if new_mars_x == mars_x and new_mars_y == mars_y:
					orbits += 1
				if orbits <= 1:
					mars_path = gr.Point(mars_centerX, mars_centerY)
					mars_path.setFill("pink")
					mars_path.draw(win)

				# Re-draw Mars on top of orbit path
				mars.enable(win)

				# Set window update frequency
				gr.update(60)

def welcome_screen(win):
	'''
	Display a welcome screen with instructions.

	Parameters: a GraphWin object
	Returns: N/A

	'''

	# Instructions for the user
	instructions = "Click to start"
	instructions += "\n\nTo add planets:"
	instructions += "\n\nPress 'm' for Mars"
	instructions += "\n\nPress 'return' to orbit"
	instructions += "\n\nPress 'esc' to quit"

	# Display the instructions in a box with a solid background
	x_center = win.getWidth()/2
	y_center = win.getHeight()/2 - win.getHeight()*0.10
	x_top_left = x_center - win.getWidth()/3
	y_top_left = y_center - win.getHeight()/8
	x_bottom_right = x_center + win.getWidth()/3
	y_bottom_right = y_center + win.getHeight()/8
	box = gr.Rectangle( gr.Point(x_top_left, y_top_left), gr.Point(x_bottom_right, y_bottom_right) )
	box.setFill("white")
	box.setOutline("black")
	box.draw( win )
	message = gr.Text( gr.Point(x_center,y_center), str(instructions) )
	message.setSize( 14 )
	message.setFace("helvetica")
	message.draw( win )
	win.update()

	# Wait for the user to click before making the instructions disappear
	win.getMouse()
	message.undraw()
	box.undraw()
	win.update()

if __name__ == "__main__":
	win = createSpace()
	welcome_screen(win)
	sun = createSun(win)
	createMars(win, sun)
	win.close()