# Cori Hatley
# 10-27-20
# Intermediate Python
# Lab 8: Under/Over AI Player

import random
import matplotlib.pyplot as plt

def main():
    
    plot_results()

def plot_results():
    
    # Initialize lower and upper boundaries
    lower_bound = 1
    upper_bound = []
    for value in range(100, 1001):
        upper_bound.append(value)

    optimal_average_turns = []
    sub_average_turns = []
    for n in upper_bound:

        # Initialize an empty list
        number_list = []

        # Append all numbers within the range to number_list
        for i in range(lower_bound, n):
            number_list.append(i)

        target = random.randint(lower_bound, n)
        optimal_turns, sub_turns = calc_average(number_list, lower_bound, n, target)
        optimal_average_turns.append(optimal_turns)
        sub_average_turns.append(sub_turns)

    plt.figure("Optimal AI Player Performance")
    plt.title("Average Number of Turns vs. Upper Bound")
    plt.xlabel("Average Number of Turns")
    plt.ylabel("Upper Bound of Guessing Range")
    plt.plot(upper_bound, optimal_average_turns)
    plt.show()

def calc_average(number_list, lower_bound, upper_bound, target):

    sub_turns_list = []
    optimal_turns_list = []
    trials = 1
    while trials <= 10:

        target = random.randint(lower_bound, upper_bound)
        sub_turns = suboptimal_AI(number_list, target)
        optimal_turns = optimal_AI(number_list, lower_bound, upper_bound, target, turns=0)
        sub_turns_list.append(sub_turns)
        optimal_turns_list.append(optimal_turns)

        trials += 1
    print(sub_turns_list)
    optimal_average_turns = sum(optimal_turns_list) // len(optimal_turns_list)
    sub_average_turns = sum(sub_turns_list) // len(sub_turns_list)
    
    return optimal_average_turns, sub_average_turns
    

def optimal_AI(number_list, lower_bound, upper_bound, target, turns=0):
    ''' Implements binary search to guess the target value when given a list
    of possible values, a lower bound, upper bound, target value, and initial
    turn count of 0. Returns the number of turns (searches) required to find
    the correct value. '''
    
    turns += 1
    if upper_bound >= lower_bound:
        mid = (upper_bound + lower_bound) // 2
        return mid

    if mid == target:
        return turns

    elif mid > target:
        return optimal_AI(number_list, lower_bound, mid-1, target, turns)

    else:
        return optimal_AI(number_list, mid+1, upper_bound, target, turns)


def suboptimal_AI(number_list, target):
    ''' Implements linear search to guess the target value when given a list
    of possible values, a lower bound, upper bound, and target value. Returns
    the number of turns (searches) required to find the correct value. '''

    for turn in range(len(number_list)):
        if number_list[turn] == target:
            return turn+1
        else:
            return len(number_list)
            
    print("Target not found.")

def human_player(number_list, lower_bound, upper_bound, target, turns=0):
    ''' Prompts the user to guess a number between lower_bound and upper_bound then
    compares the guess to a random number n. If guess does not equal n, a hint message
    (too high or too low) prints and the user is prompted to guess again. '''

    turns += 1
    # Prompt user input
    guess = int(input("\nEnter a number between {0} and {1}:\n".format(lower_bound, upper_bound)))

    # Check if guess exists in number_list
    if (guess in number_list):

        # Compare guess to n
        if guess == target:
            print("Congratulations! Your guess of {0} is correct!\nYou guessed correctly in {1} turns.\n".format(guess, turns))

        # If guess is not equal to n, give the user a hint
        elif guess < target:
            print("Your guess of {0} is too low.".format(guess))
            human_player(number_list, lower_bound, upper_bound, target, turns)
        else:
            print("Your guess of {0} is too high.".format(guess))
            human_player(number_list, lower_bound, upper_bound, target, turns)

    # If guess is not in number_list, print error message and call the function recursively
    else:
        print("Invalid input. Please try again.")
        human_player(number_list, lower_bound, upper_bound, target, turns)


if __name__ == "__main__":
    main()

