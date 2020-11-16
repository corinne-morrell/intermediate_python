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

	def getInitXY(self):
		return self.initial_position

	def getName(self):
		return self.name

	def getAxis(self):
		scaledAxis = self.semimajor_axis / 10**(-9)
		return scaledAxis

	def getEcc(self):
		return self.eccentricity

	def getPath(self):
		return self.path_color

	def getMass(self):
		scaledMass = self.mass / 10**(-9)
		return scaledMass

	def getVel(self):
		scaledVel = self.v_aphelion / 10**(-9)
		return scaledVel

	def enable(self, win): # draw the Planet object in the window
		self.draw(win)
		self.name.draw(win)

	def disable(self): # undraw the Planet object
		self.undraw()
		self.name.undraw()

	def orbit(self, sun):
		key = win.checkKey()
		theta = 0.0
		time = 0.0
		dtheta = 0.001
		dtime = 0.01
		#orbits = 0

		while key != "Escape":
			key = win.checkKey()

			solar_mass = 1.989e30 / 10**(-9)

			G = 6.67428e-11

			initX = self.getInitXY().getX()
			initY = self.getInitXY().getY()

			axis = self.getAxis()
			ecc = self.getEcc()
			r = (axis * (1 - ecc ** 2)) / (1 + ecc * math.cos(theta))
			r_prime = math.sqrt(r**2 + (4 * axis * ecc * (axis * ecc + r * math.cos(theta))))

			f_gravity = G * self.mass * solar_mass / (r_prime**2)

			fx = math.cos(theta) * f_gravity
			fy = math.sin(theta) * f_gravity

			v_init = self.getVel()
			v_init_x = (math.cos(theta) * v_init)
			v_init_y = (math.sin(theta) * v_init)

			accX = (fx / self.getMass())
			accY = (fy / self.getMass())

			newX = initX + (v_init_x * time) + ( 0.5 * accX * time**2)
			newY = initY + (v_init_y * time) + ( 0.5 * accY * time**2)

			currentX = self.getCenter().getX()
			currentY = self.getCenter().getY()

			dx = newX - currentX
			dy = newY - currentY

			self.move(dx, dy)
			self.name.move(dx, dy)

			theta = (theta + dtheta) % (2 * math.pi)
			time = time + dtime

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
				planet_path.draw(win)

			# Re-draw Mars on top of orbit path
			planet.enable(win)'''





def createSpace():
	'''
	Creates a graphics window with a black background.
	
	Parameters: N/A
	Returns: a GraphWin object
	
	'''

	# Create a black window
	winWidth = 1400
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

	radius = 20
	sun = gr.Circle(pCenter, radius)
	name = gr.Text(pCenter, "Sun")
	name.setSize(14)

	sun.setFill("yellow")
	sun.draw(win)
	name.draw(win)

	return sun

def createInnerPlanets(sun):
	'''
	Creates a Planet object to represent Mars and animates Mars' orbital motion around the Sun.

	Parameters: GraphWin object, object at center of orbit
	Returns: N/A

	'''

	solar_centerX = sun.getCenter().getX()
	solar_centerY = sun.getCenter().getY()

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



def animateOrbits(win, sun):

	key = win.getKey()
	planet_list = []

	if key == "i":
		mercury, venus, earth, mars = createInnerPlanets(sun)
		planet_list.append(mercury)
		planet_list.append(venus)
		planet_list.append(earth)
		planet_list.append(mars)

	for planet in planet_list:
		planet.enable(win)
		
	key = win.getKey()
	if key == "Return":
		for planet in planet_list:
			planet.orbit(sun)
			gr.update(60)


def welcome_screen(win):
	'''
	Display a welcome screen with instructions.

	Parameters: a GraphWin object
	Returns: N/A

	'''

	# Instructions for the user
	instructions = "Click to start"
	instructions += "\n\nChoose between Inner (Mercury - Mars) and Outer (Jupiter - Neptune) Planets"
	instructions += "\n\nPress 'i' for Inner Planets"
	instructions += "\n\nPress 'o' for Outer Planets"
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
	createInnerPlanets(sun)
	animateOrbits(win, sun)
	win.getMouse()
	win.close()