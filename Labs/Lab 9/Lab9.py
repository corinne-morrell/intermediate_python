# Cori Hatley
# 11-03-20
# Intermediate Python
# Lab 9: Fibonacci Sequence
# To run from the terminal, enter python Lab9.py

import time

def fib_sequence():
    ''' Creates a dictionary to store terms in the Fibonacci sequence '''
    fib_nums = { }

    return fib_nums

def fib_efficient(n):
    ''' Efficiently calculates the n-th term of the Fibonacci sequence '''
    # Call fib_sequence to access dictionary
    sequence = fib_sequence()

    # Check to see if the term has already been calculated
    if n in sequence and n > 2:
        return sequence[n]

    # Recursive call and recombination for calculating the next term in the sequence
    elif n not in sequence and n > 2:
        fib_num = fib_efficient(n-1) + fib_efficient(n-2)
        sequence[n] = fib_num
        return fib_num

    # Establish base case
    else:
        return 1

def time_fibonacci_eff(n):
	''' Time the fib_efficient() function as it calculates the n-th Fibonacci number. Returns the time in seconds. '''
	print( f"Calculating the {n}-th Fibonacci number..." )
	t_start = time.time()
	fib_n = fib_efficient(n)
	t_end = time.time()
	delta_t = t_end - t_start
	t_fib = delta_t * 1000000
	print( f"\tfib_efficient({n}) = {fib_n}" )
	print( f"\tcompleted in {t_fib} microseconds" )
	return t_fib
    
def fibonacci_inefficient(n):
	''' Inefficiently calculates the n-th term of the Fibonacci sequence '''
	fib_n = 0
	if n > 2:
		# Subdivision: Calculate the previous 2 Fibonacci numbers.
		# Recombination: add the previous 2 Fibonacci numbers to produce the n-th value in the sequence.
		fib_n = fibonacci_inefficient(n-2) + fibonacci_inefficient(n-1)
	elif n >= 0:
		# Base case: The 0-th and 1-st Fibonacci numbers can be hardcoded, 1 and 1.
		fib_n = 1
	return fib_n


def time_fibonacci_ineff(n):
	''' Time the fibonacci() function as it calculates the n-th Fibonacci number. Returns the time in seconds. '''
	print( f"Calculating the {n}-th Fibonacci number..." )
	t_start = time.time()
	fib_n = fibonacci_inefficient( n )
	t_end = time.time()
	delta_t = t_end - t_start
	t_fib = delta_t * 1000000
	print( f"\tfibonacci_inefficient({n}) = {fib_n}" )
	print( f"\tcompleted in {t_fib} microseconds" )
	return t_fib

def main():
    time_fibonacci_eff(6)
    time_fibonacci_ineff(6)

main()