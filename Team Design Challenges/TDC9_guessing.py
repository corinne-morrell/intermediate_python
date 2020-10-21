# Cori Hatley
# 10-19-20
# Intermediate Python
# Team Design Challenge: Under/Over Guessing Game

import random
def main():
    ''' Generates a random number n and passes lower_bound, upper_bound, and n to play_game function. '''
    
    # Initialize lower and upper boundaries
    lower_bound = 1
    upper_bound = 5

    # Generate random number n
    n = random.randint(lower_bound, upper_bound)

    play_game(lower_bound, upper_bound, n)

def play_game(lower_bound, upper_bound, n):
    ''' Prompts the user to guess a number between lower_bound and upper_bound then
    compares the guess to a random number n. If guess does not equal n, a hint message
    (too high or too low) prints and the user is prompted to guess again. '''

    # Initialize an empty list
    number_list = []

    # Append all numbers within the range to number_list (to be used in error checking)
    for i in range(lower_bound, upper_bound+1):
        number_list.append(i)

    # Prompt user input
    guess = int(input("\nEnter a number between {0} and {1}:\n".format(lower_bound, upper_bound)))

    # Check if guess exists in number_list
    if (guess in number_list):

        # Compare guess to n
        if guess == n:
            print("Congratulations! Your guess of {0} is correct!".format(guess))

        # If guess is not equal to n, give the user a hint
        elif guess < n:
            print("Your guess of {0} is too low.".format(guess))
            play_game(lower_bound, upper_bound, n)
        else:
            print("Your guess of {0} is too high.".format(guess))
            play_game(lower_bound, upper_bound, n)

    # If guess is not in number_list, print error message and call the function recursively
    else:
        print("Invalid input. Please try again.")
        play_game(lower_bound, upper_bound, n)


if __name__ == "__main__":
    main()

