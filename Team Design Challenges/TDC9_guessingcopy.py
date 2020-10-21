# Cori Hatley
# 10-19-20
# Intermediate Python
# Team Design Challenge: Under/Over Guessing Game

import random

def play_game(lower_bound, upper_bound):

    # Generate random number n
    n = random.randint(lower_bound, upper_bound)
    
    # Initialize an empty list
    number_list = []

    # Append all numbers within the range to number_list (to be used in error checking)
    for i in range(lower_bound, upper_bound+1):
        number_list.append(i)


    # Prompt user input
    guess = int(input("\nEnter a number between {0} and {1}:\n".format(lower_bound, upper_bound)))

    guesses = 0

    while guesses < upper_bound:
    # Check if guess exists in number_list
        if (guess in number_list):
            if guess == n:
                print("Congratulations! Your guess of {0} is correct!".format(guess))
                guesses = upper_bound
            elif guess < n:
                print("Your guess of {0} is too low.".format(guess))
            else:
                print("Your guess of {0} is too high.".format(guess))
        else:
            print("Invalid input. Please try again.")

        guesses += 1


play_game(1, 5)