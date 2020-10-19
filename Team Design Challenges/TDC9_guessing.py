# Cori Hatley
# 10-19-20
# Intermediate Python
# Team Design Challenge: Under/Over Guessing Game

import random

def play_game(lower_bound, upper_bound):

    # Generate random number n
    #n = random.randit(lower_bound, upper_bound)
    
    # Initialize an empty list
    number_list = []

    # Append all numbers within the range to number_list (to be used in error checking)
    for i in range(lower_bound, upper_bound+1):
        number_list.append(i)

    guesses = 0
    for guesses in range(lower_bound, upper_bound+1):
        guess = int(input("\nEnter a number between {0} and {1}:\n".format(lower_bound, upper_bound)))

        if (guess in number_list):
            print("Acceptable Input")
        else:
            print("Unacceptable Input")


play_game(1, 5)