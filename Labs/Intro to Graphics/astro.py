# Cori Hatley
# 11-10-20
# Intermediate Python
# Lab 10 - Interactive Animation

# To run from the terminal, enter python astro.py
	
	# Click to start. To add planets:
	# Press 'm' for Mars
	# Press 'n' for Neptune
	# Press 'return' to animate orbit
	# Press 'esc' to quit

import graphics as gr
import math
import time

class Planet(gr.Circle):
	'''Creates a Planet object with a center, radius (in m), color, distance from Sun (in m),
	mass (in kg), and name.'''
	def __init__(self, center, radius, color, distance, mass, name):
		x, y = center
		gr.Circle.__init__(self, gr.Point(x, y), radius)
		self.setFill(color)
		self.distance = distance
		self.mass = mass
		self.name = gr.Text(gr.Point(x, y - 1.75 * radius), name)
		self.name.setTextColor("white")

	def getDistance(self):
		return self.distance

	def getMass(self):
		return self.mass

	def getName(self):
		return self.name

	def enable(self, win): # draw the Planet object in the window
		self.draw(win)
		self.name.draw(win)

	def disable(self): # undraw the Planet object
		self.undraw()
		self.name.undraw()

def createSpace():
	'''Creates a black graphics window. Returns a GraphWin object.'''
	# Create a black window
	winWidth = 1000
	winHeight = 800
	win = gr.GraphWin( "The Solar System", winWidth, winHeight )
	win.setBackground("black")

	return win

def createSun(win):
	'''Creates a Circle object to represent the Sun in the center of the window.'''
	xCenter = win.getWidth() / 2
	yCenter = win.getHeight() / 2
	pCenter = gr.Point(xCenter, yCenter)

	radius = 50
	sun = gr.Circle(pCenter, radius)

	sun.setFill("yellow")
	sun.draw(win)
	
	return sun


'''def createMars():
	distance = 2.1478 * 10**11
	d_pixels = 215
	ecliptic = win.getHeight() / 2
	radius = 3
	mass = 6.39 * 10**23

	mars = Planet((d_pixels, ecliptic), radius, "red", distance, mass, "Mars")

	return mars

def animateOrbits():
	xCenter = win.getWidth() / 2
	yCenter = win.getHeight() / 2

	t = 0.0
	dt = 0.01
	delay = 0.01'''


def testPlanet(win, sun):
	
	mars_x = 400
	mars_y = win.getHeight() / 2

	t = 0.0
	dt = 0.01
	delay = 0.0001

	mars_orbit_radius = 400 - win.getWidth() / 2
	#solar_center = gr.Point(win.getWidth() / 2, win.getHeight()/ 2)

	mars = Planet((mars_x, mars_y), 10, "red", 100, 100, "Mars")
	# mars_orbit = gr.Circle(gr.Point(win.getWidth() / 2, win.getHeight() / 2), 400 - win.getWidth() / 2)
	# mars_orbit.setOutline("lightgrey")
	neptune = Planet((200, win.getHeight() / 2), 20, "blue", 100, 100, "Neptune")
	
	key = ""
	while key != "Escape":
		key = win.getKey()
		if key == "m":
			mars.enable(win)
			# mars_orbit.draw(win)
		if key == "n":
			neptune.enable(win)
		if key == "Return":
			while key != "Escape":
				key = win.checkKey()
				new_mars_x, new_mars_y = sun.getCenter().getX() + mars_orbit_radius * math.cos(t), sun.getCenter().getY() + mars_orbit_radius * math.sin(t)
				center = mars.getCenter()
				mars.move(new_mars_x - center.getX(), new_mars_y - center.getY())
				mars.name.move(new_mars_x - center.getX(), new_mars_y - center.getY())
			
				t = (t + dt) % (2 * math.pi)

				time.sleep(delay)

	
def welcome_screen( win ):
	''' Display a welcome screen with instructions.'''

	# Instructions for the user
	instructions = "Click to start"
	instructions += "\n\nTo add planets:"
	instructions += "\n\nPress 'm' for Mars"
	instructions += "\n\nPress 'n' for Neptune"
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
	box.setFill( "white" )
	box.setOutline( "black" )
	box.draw( win )
	message = gr.Text( gr.Point(x_center,y_center), str(instructions) )
	message.setSize( 14 )
	message.setFace( "helvetica" )
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
	testPlanet(win, sun)
	win.close()