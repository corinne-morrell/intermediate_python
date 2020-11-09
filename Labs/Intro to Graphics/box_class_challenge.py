# box_class_challenge.py -- Complete this Box class to gain experience with the design of custom types in Python.
# 
# Cori Hatley
# Intermediate Python
# Fall 2020


class Box:
	def __init__(self, length, width, height, weight, idNum=None, address=None):
		''' Constructs a new Box object. The dimensions (length, width, height) of each  
		Box should be floats measured in centimeters. The weight should be a float measured in
		kilograms.  The ID number should be a positive integer. The address should be a string.'''

		# TODO: 
		# This constructor is missing some field assignments (self.____ = ____). 
		# Can you fill them in?
		# Hint: The slides and recorded lecture may help!
		self.length = length
		self.width = width
		self.height = height
		self.weight = weight
		self.id = idNum
		self.address = address
	
	# --------------------------------------------------------------
	#                       ACCESSOR METHODS
	#             Make it easy to read an object's fields
	# -------------------------------------------------------------
	def getLength(self):
		'''Returns the Box object's length (an integer or float).'''
		return self.length


	def getWidth(self):
		'''Returns the Box object's width (an integer or float).'''
		return self.width


	def getHeight(self):
		'''Returns the Box object's height (an integer or float).'''
		return self.height


	def getWeight(self):
		'''Returns the Box object's weight (an integer or float).'''
		return self.weight


	def getID(self):
		'''Returns the Box object's ID number (an integer).'''
		return self.id

	def getAddress(self):
		'''Returns the Box object's address (a string).'''
		return self.address
	
	# --------------------------------------------------------------
	#                       MUTATOR METHODS
	#      Make it easy (and safe!) to update an object's fields
	# --------------------------------------------------------------
	def setLength(self, l):
		'''Only updates the length field if l is a positive number'''
		if (type(l)==float or type(l)==int) and (l > 0):
			self.length=l
		else:
			print("Invalid length", l, "of type", type(l))

	def setWidth(self, w):
		'''Only updates the width field if w is a positive number'''

		if (type(w)==float or type(w)==int) and (w > 0):
			self.width=w
		else:
			print("Invalid width", w, "of type", type(w))


	def setHeight(self, h):
		'''Only updates the height field if h is a positive number'''

		if (type(h)==float or type(h)==int) and (h > 0):
			self.height=h
		else:
			print("Invalid height", h, "of type", type(h))


	def setWeight(self, w):
		'''Only updates the weight field if w is a positive number'''

		if (type(w)==float or type(w)==int) and (w > 0):
			self.weight=w
		else:
			print("Invalid weight", w, "of type", type(w))


	def setID(self, n):
		'''Only updates the ID field if n is a positive integer'''
		if type(n)==int and n>=0:
			self.id=n
		else:
			print("Invalid ID number", n, "of type", type(n))

	def setAddress(self, a):
		'''Only updates the address field if a is a string'''
		if type(a)==str:
			self.address=a
		else:
			print("Invalid address", a, "of type", type(a))

	# --------------------------------------------------------------
	#                       UTILITY METHODS
	# --------------------------------------------------------------
	def calcVolume(self):
		'''Returns the Box object's current volume in cm**3 '''

		return self.weight * self.length * self.height

	def __str__( self ):
		''' Explains to Python how best to represent a Box object as a string, e.g. for "pretty printing." '''

		box_str = "\nBox Id: {0}\nLength: {1} cm\nWidth: {2} cm\nHeight: {3} cm\nWeight: {4} kg\nAddress: {5}".format(self.id, self.length, self.width, self.height, self.weight, self.address)
		return box_str




def testBox():
	'''Tests the Box class's constructor, accessors, and mutators.'''

	# Construct a Box object and print its information
	b = Box( 1, 2, 3, 4, 0, "yo" )
	print( b )
	print("ID:", b.getID())
	print("dimensions: {0:3.2f} x {1:3.2f} x {2:3.2f} cm")
	print("weight:", b.getWeight())
	print("address:", b.getAddress())

	# Use the mutator methods to alter the object's fields
	print("\nUpdating ID to -1...")
	b.setID(-1)
	print("new ID:", b.getID())

	print("\nUpdating ID to 42...")
	b.setID(42)
	print("new ID:", b.getID())

	print("\nUpdating address to -1...")
	b.setAddress(-1)
	print("new address:", b.getAddress())

	print("\nUpdating address to the robotics lab...")
	b.setAddress("Dr. Caitrin Eaton, PME 127, 5800 Bay Shore Rd, Sarasota, FL 34243")
	print("new address:", b.getAddress() )


def testBoxStr():
	'''Tests tbe Box class's shiny new __str__() utility method.'''

	# Construct a Box object and print its information
	ncf = "New College of Florida, 5800 Bay Shore Rd, Sarasota, FL 34243"
	b = Box( 1.0, 2.0, 3.0, 4.0, 42, ncf )
	print(b)


if __name__=="__main__":
	testBox()
	testBoxStr()
	

		