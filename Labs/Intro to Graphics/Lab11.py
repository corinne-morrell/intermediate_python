# Cori Hatley
# 11-10-20
# Intermediate Python
# Lab 11 - Solar System Simulation: Proof of Concept

# To run from the terminal, enter python Lab11.py
	
	# Click to start. To add planets:
	# Press 'm' for Mars
	# Press 'return' to animate orbit
	# Press 'esc' to quit

import graphics as gr
import math
import time
import sys

class Sun(gr.Circle):
	def __init__(self, center, radius, color, name, mass):
		x, y = center
		gr.Circle.__init__(self, gr.Point(x, y), radius)
		self.setFill(color)
		self.name = gr.Text(gr.Point(x, y), name)
		self.name.setTextColor("black")
		self.mass = mass

	def getName(self):
		return self.name

	def getMass(self):
		return self.mass
class Planet(gr.Circle):
	'''
	Creates a Planet object with a center, radius (in pixels), color, name, semimajor axis length (in pixels),
	eccentricity of the orbit (which has no units), and mass (in kg).
	Inherits characteristics of the Circle class from graphics.py.
	
	'''

	def __init__(self, center, radius, color, name, semimajor_axis, eccentricity, path_color, mass, v_aphelion):
		x, y = center
		gr.Circle.__init__(self, gr.Point(x, y), radius)
		self.setFill(color)
		self.initial_position = self.getCenter()
		self.name = gr.Text(gr.Point(x, y - 1.75 * radius), name)
		self.name.setTextColor("white")
		self.semimajor_axis = semimajor_axis
		self.eccentricity = eccentricity
		self.path_color = path_color
		self.mass = mass
		self.v_aphelion = v_aphelion
		self.theta = 0.0
		self.time = 0.0

	def getInitXY(self):
		return self.initial_position

	def getName(self):
		return self.name

	def getAxis(self):
		return self.semimajor_axis

	def getEcc(self):
		return self.eccentricity

	def getPath(self):
		return self.path_color

	def getMass(self):
		return self.mass

	def getVel(self):
		return self.v_aphelion

	def enable(self, space): # draw the Planet object in the window
		self.draw(space)
		self.name.draw(space)

	def disable(self): # undraw the Planet object
		self.undraw()
		self.name.undraw()

	def orbit(self, sun):

		G = 6.67428e-11

		dtheta = 0.1
		dtime = 0.01

		self.theta = (self.theta + dtheta) % (2 * math.pi)
		self.time = self.time + dtime

		#self.r = (self.getAxis() * (1 - (self.getEcc())**2)) / (1 + self.getEcc() * math.cos(self.theta))
		#self.r_prime = math.sqrt(self.r**2 + (4 * self.getAxis() * self.getEcc() * (self.getAxis() * self.getEcc() + self.r * math.cos(self.theta))))

		sun.sunX = sun.getCenter().getX()
		sun.sunY = sun.getCenter().getY()		
		
		self.currentX = (self.getCenter().getX()) / 10**4
		self.currentY = (self.getCenter().getY()) / 10**4

		self.distX = sun.sunX - self.currentX
		self.distY = sun.sunY - self.currentY
		self.dist = math.sqrt((self.distX)**2 + (self.distY)**2)

		self.f_gravity = (G * self.getMass() * sun.getMass()) / ((self.dist)**2)

		self.fx = math.cos(self.theta) * self.f_gravity
		self.fy = math.sin(self.theta) * self.f_gravity

		self.velX = (math.cos(self.theta) * self.getVel()) / 10**15
		self.velY = (math.sin(self.theta) * self.getVel()) / 10**15

		self.accX = (self.fx / self.getMass()) / 10**15
		self.accY = (self.fy / self.getMass()) / 10**15

		self.newX = (self.currentX + (self.velX * self.time) + ( 0.5 * self.accX * (self.time)**2))
		self.newY = (self.currentY + (self.velY * self.time) + ( 0.5 * self.accY * (self.time)**2))

		self.dx = self.newX - self.currentX
		self.dy = self.newY - self.currentY

		self.move(self.dx, self.dy)
		self.name.move(self.dx, self.dy)

		print("current position: {0}, {1}".format(self.currentX, self.currentY))
		print("new position: {0}, {1}".format(self.newX, self.newY))
		print("dx, dy: {0}, {1}".format(self.dx, self.dy))
		print("distance from sun: {0}".format(self.dist))
		print("force of gravity: {0}".format(self.f_gravity))
		print("velocity: {0}, {1}".format(self.velX, self.velY))
		print("acceleration: {0}, {1}".format(self.accX, self.accY))
		print("theta: {0}".format(self.theta))


		'''# Temporarily undraw Mars and plot orbit path
		planet.disable()

		# If new coordinates equal initial coordinates, Mars has completed one orbit
		planet_initX = solar_centerX + planet.getAxis()
		planet_initY = solar_centerY + planet.getAxis()
		if new_x == planet_initX and new_y == planet_initY:
			orbits += 1
		if orbits <= 1:
			planet_path = gr.Point(planet_centerX, planet_centerY)
			color = planet.getPath()
			planet_path.setFill(color)
			planet_path.draw(space)

		# Re-draw Mars on top of orbit path
		planet.enable(space)'''

def createSpace():
	'''
	Creates a graphics window with a black background.
	
	Parameters: N/A
	Returns: a GraphWin object
	
	'''

	# Create a black window
	spaceWidth = 1400
	spaceHeight = 800
	space = gr.GraphWin("The Solar System", spaceWidth, spaceHeight, autoflush=False)
	space.setBackground("black")

	return space

def createSun(space):
	'''
	Creates a Circle object to represent the Sun in the center of the window.
	
	Parameters: requires Space (a GraphWin object returned from createSpace)
	Returns: a Circle object at the center of the window

	'''
	# Find the center of the window
	sunX = space.getWidth() / 2
	sunY = space.getHeight() / 2

	# Instantiate Sun object
	sun = Sun((sunX, sunY), 20, "yellow", "Sun", 1.989e30)
	name = sun.getName()

	sun.draw(space)
	name.draw(space)

	return sun

def createPlanets(sun):
	'''
	Creates Planet objects.

	Parameters: requires the Sun (a Circle object returned from createSun)
	Returns: Planet objects

	'''
	# Find the center of the Sun
	solar_centerX = sun.getCenter().getX()
	solar_centerY = sun.getCenter().getY()

	# Create Planet objects
	mercury_x = solar_centerX + 70
	mercury_y = solar_centerY
	mercury = Planet((mercury_x, mercury_y), 5, "grey", "Mercury", 57.91e9, 0.2056, "lightgrey", 3.3011e23, 5.898e4)

	venus_x = solar_centerX + 109
	venus_y = solar_centerY
	venus = Planet((venus_x, venus_y), 5, "orange", "Venus", 108.21e9, 0.0067, "orange", 4.8675e24, 3.526e4)

	earth_x = solar_centerX + 152
	earth_y = solar_centerY
	earth = Planet((earth_x, earth_y), 5, "teal", "Earth", 149.6e9, 0.0167, "teal", 5.9724e24, 3.029e4)

	mars_x = solar_centerX + 250
	mars_y = solar_centerY
	mars = Planet((mars_x, mars_y), 5, "red", "Mars", 227.92e9, 0.0935, "lightpink", 6.4171e23, 2.65e4)

	return mercury, venus, earth, mars

def animateOrbits(space, sun):
	'''
	Animates the orbital motion of the planets.

	Parameters: requires Space (a GraphWin object returned from createSpace)
	and the Sun (a Circle object returned from createSun)
	Returns: N/A

	'''

	# Create a list containing all of the Planet objects
	planet_list = [*createPlanets(sun)]

	# Initialize the key variable as an empty string
	key = ""

	# Detect key press
	key = space.getKey()

	# When the user presses "Return", draw the planets in the window
	if key == "Return":
		for planet in planet_list:
			planet.enable(space)
		
		# Call the orbit function for each planet in the list of planets until the user presses "Escape"
		while key != "Escape":
			key = space.checkKey()
			for planet in planet_list:
				planet.orbit(sun)
			
			# Update the window to show the motion
			gr.update(60)

def welcome_screen(space):
	'''
	Displays a welcome screen with instructions.

	Parameters: requires Space (a GraphWin object returned from createSpace)
	Returns: N/A

	'''

	# Instructions for the user
	instructions = "Welcome to the Solar System!"
	instructions += "\n\nTo begin, click anywhere in the window."
	instructions += "\n\nPress 'return' to simulate the orbital motion of the planets."
	instructions += "\n\nPress 'esc' to end the simulation."
	instructions += "\n\nClick to close the window."

	# Display the instructions in a box with a solid background
	x_center = space.getWidth()/2
	y_center = space.getHeight()/2 - space.getHeight()*0.10
	x_top_left = x_center - space.getWidth()/3
	y_top_left = y_center - space.getHeight()/8
	x_bottom_right = x_center + space.getWidth()/3
	y_bottom_right = y_center + space.getHeight()/8
	box = gr.Rectangle( gr.Point(x_top_left, y_top_left), gr.Point(x_bottom_right, y_bottom_right) )
	box.setFill("white")
	box.setOutline("black")
	box.draw(space)
	message = gr.Text( gr.Point(x_center,y_center), str(instructions) )
	message.setSize( 14 )
	message.setFace("helvetica")
	message.draw(space)
	space.update()

	# Wait for the user to click before making the instructions disappear
	space.getMouse()
	message.undraw()
	box.undraw()
	space.update()

if __name__ == "__main__":
	space = createSpace()
	welcome_screen(space)
	sun = createSun(space)
	createPlanets(sun)
	animateOrbits(space, sun)
	space.getMouse()
	space.close()