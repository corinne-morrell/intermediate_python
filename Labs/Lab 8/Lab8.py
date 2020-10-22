# Cori Hatley
# 10-27-20
# Intermediate Python
# Lab 8: Under/Over AI Player

import random
def main():
    ''' Generates a random number and passes lower_bound, upper_bound, and target to play_game function. '''
    
    # Initialize lower and upper boundaries
    lower_bound = 1
    upper_bound = 100

    # Generate random number target
    target = random.randint(lower_bound, upper_bound)

    # Initialize an empty list
    number_list = []

    # Append all numbers within the range to number_list (to be used in error checking)
    for i in range(lower_bound, upper_bound+1):
        number_list.append(i)

    # human_player(number_list, lower_bound, upper_bound, target, turns=0)
    optimal_AI(number_list, lower_bound, upper_bound, target, turns=0)

def optimal_AI(number_list, lower_bound, upper_bound, target, turns=0):

    turns += 1
    if upper_bound >= lower_bound:
        mid = (upper_bound + lower_bound) // 2

        if number_list[mid] == target:
            print("The correct number is {0}.\nThe computer guessed correctly in {1} turns.\n".format(mid, turns))

        elif number_list[mid] > target:
            return optimal_AI(number_list, lower_bound, mid - 1, target, turns)

        else:
            return optimal_AI(number_list, mid + 1, upper_bound, target, turns)

    else:
        print("Something went wrong. Please try again.")
        optimal_AI(number_list, lower_bound, upper_bound, target, turns)


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

