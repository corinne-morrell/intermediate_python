# Cori Hatley
# 11-03-20
# Intermediate Python
# Lab 9: Fibonacci Sequence
# To run from the terminal, enter python Lab9.py

import time
import matplotlib.pyplot as plt

def fib_efficient(n, sym_tables, sequence):
    ''' Efficiently calculates the n-th term of the Fibonacci sequence '''

    if n <= 2:
        return 1

    # Check to see if the term has already been calculated
    if n in sequence:
        return sequence[n]

    # Recursive call and recombination for calculating the next term in the sequence
    else:
        sym_tables[0] += 1
        fib_num = fib_efficient(n-1, sym_tables, sequence) + fib_efficient(n-2, sym_tables, sequence)
        sequence[n] = fib_num
        return fib_num


    
def fib_inefficient(n, sym_tables):
	''' Inefficiently calculates the n-th term of the Fibonacci sequence '''
	
	sym_tables[0] += 1
    
	fib_n = 0
	if n > 2:
		# Subdivision: Calculate the previous 2 Fibonacci numbers.
		# Recombination: add the previous 2 Fibonacci numbers to produce the n-th value in the sequence.
		fib_n = fib_inefficient(n-2, sym_tables) + fib_inefficient (n-1, sym_tables)
	elif n >= 0:
		# Base case: The 0-th and 1-st Fibonacci numbers can be hardcoded, 1 and 1.
		fib_n = 1
	return fib_n

def time_efficient(n):
	''' Time the fib_efficient() function as it calculates the n-th Fibonacci number. Returns the time in seconds. '''
	#print( f"Calculating the {n}-th Fibonacci number..." )
	fib_sequence = {}
	num_tables = [0]
	t_start = time.time()
	fib_n= fib_efficient(n, num_tables, fib_sequence)
	t_end = time.time()
	delta_t = t_end - t_start
	t_fib = delta_t * 1000000
	#print( f"\tfib_efficient({n}) = {fib_n}" )
	#print( f"\tcompleted in {t_fib} microseconds" )
	#print( f"\tsymbol tables created = {num_tables}" )
	return t_fib, num_tables

def time_inefficient(n):
	''' Time the fibonacci() function as it calculates the n-th Fibonacci number. Returns the time in seconds. '''
	#print( f"Calculating the {n}-th Fibonacci number..." )
	num_tables = [0]
	t_start = time.time()
	fib_n = fib_inefficient( n, num_tables )
	t_end = time.time()
	delta_t = t_end - t_start
	t_fib = delta_t * 1000000
	#print( f"\tfib_inefficient ({n}) = {fib_n}" )
	#print( f"\tcompleted in {t_fib} microseconds" )
	#print( f"\tsymbol tables created = {num_tables}" )
	return t_fib, num_tables

def plot_results():

    eff_runtime = []
    eff_memory = []

    ineff_runtime = []
    ineff_memory = []

    fib_index = []

    for n in range(1, 11):
        fib_index.append(n)

        eff_time, eff_tables = time_efficient(n)
        ineff_time, ineff_tables = time_inefficient(n)

        eff_runtime.append(eff_time)
        eff_memory.append(eff_tables)

        ineff_runtime.append(ineff_time)
        ineff_memory.append(ineff_tables)

    # Plot figures
    fig, ax = plt.subplots(1,2)

    ax[0].plot(fib_index, eff_runtime, label="Efficient Implementation")
    ax[0].plot(fib_index, ineff_runtime, label="Inefficient Implementation")
    ax[0].set_title("Runtime")
    ax[0].set_xlabel("N (Index of Fibonacci Number)")
    ax[0].set_ylabel("Runtime (microseconds)")
    ax[0].grid()
    ax[0].legend()

    ax[1].plot(fib_index, eff_memory, label="Efficient Implementation")
    ax[1].plot(fib_index, ineff_memory, label="Inefficient Implementation")
    ax[1].set_title("Memory Requirements")
    ax[1].set_xlabel("N (Index of Fibonacci Number)")
    ax[1].set_ylabel("Number of Symbol Tables Created")
    ax[1].grid()
    ax[1].legend()

    plt.show()


    

def main():
    plot_results()

main()