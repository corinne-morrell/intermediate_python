# Cori Hatley
# TDC 6: Madlibs
# Intermediate Python
# 09-28-20

import os

def replace_words( linelist, filename ):
	line_contents = read_file( filename )
	line_length = len( line_contents )
	for line_number in range( line_length ):
		line = line_contents[ line_number ]
		line_stripped = line.strip()		# removes unnecessary white space
		words = line_stripped.split( " " )	# breaks line up into a list of words, using spaces as delimeters
		
		word_list_length = len( words)
		for word_number in range( word_list_length ):
			if linelist[ word_number ].isupper() == True:
				replace = linelist.replace(word_number, (input('New' + word_number + 'here:')).strip)

		return linelist


def print_file( filename ):
	''' Read in the file with the given filename, and copy its
	contents into the terminal. Assumes that the file is in
	the same directory as the program. '''

	# Read the lines of the file into a list of strings
	file_contents = read_file( filename )
	print("\nList of lines:")
	print(file_contents)

	# Iterate over the list of lines, printing each without
	# unnecessary whitespace. Demonstrating how to break
	# the line up into a list of individual words with split().
	file_length = len( file_contents )
	print( "\nIterating over list of lines:" )
	for line_number in range( file_length ):
		line = file_contents[ line_number ]
		line_stripped = line.strip()		# removes unnecessary white space
		words = line_stripped.split( " " )	# breaks line up into a list of words, using spaces as delimeters
		#print( "line {0}: {1}".format( line_number, line ) )
		#print( "line {0} stripped: {1}".format( line_number, line_stripped ) )
		#print( "line {0} words: {1}".format( line_number, words ) )
		#print( "" )
		return words


def read_file( filename ):
	''' Returns a list of strings in which each element is one line
	from the file. The filename must be a string. Assumes that the
	file is in the same directory as the program. '''

	# Each OS formats file paths differently. Use the OS package
	# to automatically apply your machine's native formatting.
	current_directory = os.path.dirname( __file__ )
	filepath = os.path.join( current_directory, filename )
	#print( "\nfilepath:", filepath )

	# Open the file for reading ("r"). Must later be closed!
	input_file = open( filepath, "r" )

	# Store each line as an element in the list
	line_list = []
	line = input_file.readline()
	while len( line ) > 0:	
		line_list.append( line )
		line = input_file.readline()

	input_file.close()	# Very important!
	
	return line_list



def test_print_file():
	''' Make sure that print_file() works before moving on to MadLibs.'''
	print("\n\nTESTING PRINT_FILE():")
	file_name = "romantic_poetry.txt"
	print_file( file_name )


def test_read_file():
	''' Make sure that read_file() works before moving on to MadLibs.'''
	print("\n\nTESTING READ_FILE():")
	file_name = "romantic_poetry.txt"
	contents = read_file( file_name )
	print( "\nList of lines:" )
	print( contents )


if __name__ == "__main__":
	#test_read_file()
	#test_print_file()

	list_lines = read_file( "romantic_poetry.txt" )
	mad_libs = replace_words( list_lines, "romantic_poetry.txt" )
	print( mad_libs )
