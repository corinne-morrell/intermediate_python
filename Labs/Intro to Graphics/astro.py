# Cori Hatley
# 11-10-20
# Intermediate Python
# Lab 10 - Interactive Animation
# To run from the terminal, enter python astro.py

import graphics as gr

def createSpace():

    # Create a black window to represent the cosmic dark
    winWidth = 800
    winHeight = 600
    win = gr.GraphWin( "The Solar System", winWidth, winHeight )
    win.setBackground("black")



    return win

def createSun(win):



    xCenter = 400
    yCenter = 300
    pCenter = gr.Point(xCenter, yCenter)

    radius = 50
    sun = gr.Circle(pCenter, radius)

    sun.setFill("yellow")
    sun.draw(win)



class Planet(gr.Circle):
    def __init__(self, center, radius, color, distance, mass, name):
        gr.Circle(center, radius)
        self.setFill(color)
        self.distance = distance
        self.mass = mass
        self.name = name

    def getDistance(self):
        return self.distance

    def getMass(self):
        return self.mass

    def getName(self):
        return self.name

#def orbits():
def testPlanet(win):
    
    mars_center = gr.Point(200, 200)
    mars = Planet(mars_center, 10, "red", 100, 100, "Mars")
    mars.draw(win)  

if __name__ == "__main__":
    win = createSpace()
    createSun(win)
    testPlanet(win)
    win.getMouse()
    win.close()