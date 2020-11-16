# box_sorting_challenge.py -- Help UPS pack delivery trucks efficiently by sorting Box objects
# 2 different ways: in order of decreasing volume and in order of decreasing weight.
# 
# YOUR NAME HERE
# Caitrin Eaton
# Intermediate Python
# Fall 2020

import random
from box_class_solution import Box


def build_box_list( n=10 ):
	'''Returns a list of n boxes with random lengths, widths, heights, and 
	weights. Uses the loop index to assign a unique ID number to each box. 
	Leaves the address fields blank.'''

	boxes = []
	max_size = 100      # maximum possible length, width, and height, in centimeters
	max_weight = 15     # maximum possible weight, in kg


	for id in range(1, n+1):
		l = random.randrange(1, max_size)
		w = random.randrange(1, max_size)
		h = random.randrange(1, max_size)
		m = random.randrange(1, max_weight)
		ithBox = Box(l, w, h, m, id)
		boxes.append(ithBox)

	return boxes


def sort_volume( boxes ):
	'''Returns a list of Box objects sorted in order of decreasing volume.'''

	# Make a copy of the boxes list, so that we don't destroy the original.
	unsorted = boxes[:]
	n = len(unsorted)

	# Pop the largest box from the unsorted list until the unsorted list is empty 
	sorted = []
	
	while n > 0:
		maxIdx = 0
		for i in range(1, n):
			if unsorted[i].calcVolume() > unsorted[maxIdx].calcVolume():
				maxIdx = i
		maxBox = unsorted.pop(maxIdx)
		sorted.append(maxBox)

	return sorted


def sort_weight( boxes ):
	'''Returns a list of Box objects sorted in order of decreasing weight.'''

	# Make a copy of the boxes list, so that we don't destroy the original.
	unsorted = boxes[:]

	# Pop the largest box from the unsorted list until the unsorted list is empty 
	sorted = []
	
	# TODO: IMPLEMENTATION SELECTION SORT HERE

	return sorted


def test_box_list():
	'''Tests the boxList() function by printing the returned list of boxes'''

	# Create a list of 10 boxes
	boxes = build_box_list( 10 )

	# Check to make sure we can access an individual box object in the list
	boxes[5].setAddress( "To infinity and beyond!" )

	# Print the list of boxes using your __str__ method :)
	for i in range(len(boxes)):
		print( f"\nboxes[{i}] =\n{boxes[i]}")


def test_sort_volume():
	'''Tests the sortVolume() function by creating a list of boxes, and printing 
	its volumes before and after sorting.'''

	print("\n========= TESTING SORT_VOLUME() ==========")

	# Create a list of boxes and print their volumes
	print("\nBEFORE SORTING:")
	boxes = build_box_list()
	for b in boxes:
		print( "Box {0} volume = {1:3.2f} cm**3".format(b.getID(), b.calcVolume()) )

	# Sort the list of boxes and print their volumes
	print("\nAFTER SORTING:")
	sortedBoxes = sort_volume( boxes )
	for b in sortedBoxes:
		print( "Box {0} volume = {1:3.2f} cm**3".format(b.getID(), b.calcVolume()) )


def test_sort_weight():
	'''Tests the sortWeight() function by creating a list of boxes, and printing 
	its volumes before and after sorting.'''

	print("\n========= TESTING SORT_WEIGHT() ==========")

	# Create a list of boxes and print their volumes
	print("\nBEFORE SORTING:")
	boxes = build_box_list()
	for b in boxes:
		print( "Box {0} weight = {1:3.2f} kg".format(b.getID(), b.getWeight()) )

	# Sort the list of boxes and print their volumes
	print("\nAFTER SORTING:")
	sortedBoxes = sort_weight( boxes )
	for b in sortedBoxes:
		print( "Box {0} weight = {1:3.2f} kg".format(b.getID(), b.getWeight()) )


if __name__=="__main__":
	#test_box_list()
	test_sort_volume()
	#test_sort_weight()
