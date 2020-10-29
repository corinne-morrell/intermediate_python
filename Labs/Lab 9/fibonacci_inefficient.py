# fibonacci_inefficient.py -- The recursive fibonacci number generator from Lab 09 prep lecture our Lecture 26: Fibonacci.
#
# Caitrin Eaton
# Lab 09
# Intermediate Python
# Fall 2020

import time


def fibonacci_inefficient( n ):
	''' Returns the n-th number in the fibonacci sequence: 1, 1, 2, 3, 5, 8, ... '''
	fib_n = 0
	if n >= 2:
		# Subdivision: Calculate the previous 2 Fibonacci numbers.
		# Recombination: add the previous 2 Fibonacci numbers to produce the n-th value in the sequence.
		fib_n = fibonacci_inefficient(n-2) + fibonacci_inefficient(n-1)
	elif n >= 0:
		# Base case: The 0-th and 1-st Fibonacci numbers can be hardcoded, 1 and 1.
		fib_n = 1
	return fib_n


def time_fibonacci_ineff( n ):
	''' Time the fibonacci() function as it calculates the n-th Fibonacci number. Returns the time in seconds. '''
	print( f"Calculating the {n}-th Fibonacci number..." )
	t_start = time.time()
	fib_n = fibonacci_inefficient( n )
	t_end = time.time()
	t_fib = t_end - t_start
	print( f"\tfibonacci_inefficient({n}) = {fib_n}" )
	print( f"\tcompleted in {t_fib} seconds" )
	return t_fib


def test_fibonacci():
	''' Test the fibonacci() function by calculating the first several numbers in the Fibonacci sequence. '''
	for n in range(-2,11):
		fib_n = fibonacci_inefficient( n )
		print( f"fibonacci_inefficient({n}) = {fib_n}" )


if __name__ == "__main__":
	#test_fibonacci()
	#time_fibonacci_ineff( 20 )
	fib_list = fibonacci_efficient(10)
	print(fib_list)