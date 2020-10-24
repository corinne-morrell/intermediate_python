# Cori Hatley
# 10-27-20
# Intermediate Python
# Lab 8: Under/Over AI Player

import random
import matplotlib.pyplot as plt

def main():
    ''' Calls plot_results to generate figure displaying results. '''
    plot_results()

def plot_results():
    ''' Establishes lower bound, upper bound, and target value; calls calc_average function
    to run multiple trials of optimal_AI and suboptimal_AI, then plots the upper bound of the
    target range versus average number of turns for each player on a graph. '''

    # Initialize lower and upper boundaries
    lower_bound = 1
    upper_bound = []
    for value in range(2, 501):
        upper_bound.append(value)

    # Initialize empty lists for average turns for Optimal and Suboptimal AI
    optimal_average_turns = []
    sub_average_turns = []
    for n in upper_bound:

        # Initialize an empty list for possible target values
        target_list = []

        # Append all numbers within the range to target_list
        for i in range(lower_bound, n):
            target_list.append(i)

        # Generate a random integer for target value
        target = random.randint(lower_bound, n)

        # Call calc_average to run multiple trials for Optimal and Suboptimal AI and append averages to lists
        optimal_turns, sub_turns = calc_average(target_list, lower_bound, n, target)
        optimal_average_turns.append(optimal_turns)
        sub_average_turns.append(sub_turns)
    
    # Plot the figure
    plt.figure("AI Player Performance")
    plt.title("Optimal vs. Sub-Optimal")
    plt.xlabel("Upper Bound of Guessing Range")
    plt.ylabel("Average Number of Turns")
    plt.plot(upper_bound, optimal_average_turns, label="Optimal AI Player")
    plt.plot(upper_bound, sub_average_turns, label="Sub-Optimal AI Player")
    plt.legend()
    plt.grid()
    plt.show()

def calc_average(target_list, lower_bound, upper_bound, target):
    ''' Takes the list of possible target values, the lower and upper bounds, and the target
    value and calls optimal_AI and suboptimal_AI 100 times, then returns the average number of
    turns for all trials. '''

    # Initialize empty lists for keeping track of number of turns per trial
    sub_turns_list = []
    optimal_turns_list = []

    # Initialize trials to 1
    trials = 1

    # Run 100 trials
    while trials <= 100:

        target = random.randint(lower_bound, upper_bound)
        sub_turns = suboptimal_AI(target_list, target)
        optimal_turns = optimal_AI(target_list, lower_bound, upper_bound, target, turns=0)
        sub_turns_list.append(sub_turns)
        optimal_turns_list.append(optimal_turns)

        trials += 1

    # Calculate average number of turns
    optimal_average_turns = sum(optimal_turns_list) / len(optimal_turns_list)
    sub_average_turns = sum(sub_turns_list) / len(sub_turns_list)
    
    return optimal_average_turns, sub_average_turns
    

def optimal_AI(target_list, lower_bound, upper_bound, target, turns=0):
    ''' Implements binary search to guess the target value when given a list
    of possible values, a lower bound, upper bound, target value, and initial
    turn count of 0. Returns the number of turns (searches) required to find
    the correct value. '''
    
    # Increment turn counter by 1 each time the function is called
    turns += 1

    # Calculate midpoint of the guessing range
    if upper_bound >= lower_bound:
        mid = (upper_bound + lower_bound) // 2

    # Base Case: AI finds the target in 1 turn
    if mid == target:
        return turns

    # Recursive Calls: if target is not found in 1 turn, optimal_AI calls itself
    # If midpoint is greater than target, call optimal_AI for only the lower half of the guessing range
    elif mid > target:
        return optimal_AI(target_list, lower_bound, mid-1, target, turns)

    # If midpoint is less than target, call optimal_AI for only upper half of the guessing range
    else:
        return optimal_AI(target_list, mid+1, upper_bound, target, turns)


def suboptimal_AI(target_list, target):
    ''' Implements linear search to guess the target value when given a list
    of possible values, a lower bound, upper bound, and target value. Returns
    the number of turns (searches) required to find the correct value. '''

    # Check each item in the list of target values one at a time, starting at index 0
    for turn in range(len(target_list)):
        if target_list[turn] == target:
            return turn+1
        else:
            return len(target_list)

if __name__ == "__main__":
    main()

