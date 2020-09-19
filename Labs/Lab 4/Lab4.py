# Cori Hatley
# 09-22-2020
# Play a game of rock-paper-scissors with user inputs and randomly generated computer throws
# To run, enter Lab4.py in the terminal, then enter your choice of rock, paper, or scissors

import random

def throwPlayer(player_throw):
    '''Evaluates player's choice and prints a statement to reflect the choice'''
    if player_throw == 'rock':
        print('You chose rock.')
    elif player_throw == 'paper':
        print('You chose paper.')
    elif player_throw == 'scissors':
        print('You chose scissors.')

def throwCPU(cpu_throw):
    '''Evaluates CPU's choice and prints a statement to reflect the choice'''
    if cpu_throw == 'rock':
        print('The computer chose rock.')
    elif cpu_throw == 'paper':
        print('The computer chose paper.')
    elif cpu_throw == 'scissors':
        print('The computer chose scissors.')

def whoWins(throw_player, throw_cpu):
    '''Determines outcome of the game given player's throw and computer's throw'''
    if throw_cpu == throw_player:
        print('It\'s a tie. Try again.')
    elif throw_cpu == 'rock' and throw_player == 'scissors':
        print('The computer wins.')
    elif throw_cpu == 'paper' and throw_player == 'rock':
        print('The computer wins.')
    elif throw_cpu == 'scissors' and throw_player == 'paper':
        print('The computer wins.')
    else:
        print('You win!')

def main():
    # Establish acceptable throw options
    throw_options = ['rock', 'paper', 'scissors']
    
    # Allow user to choose rock, paper, or scissors
    player_choice = (input('Rock, paper, or scissors?\n')).lower().strip()

    # Check user input
    if player_choice not in throw_options:
        print('You must choose either rock, paper, or scissors. Check your spelling and try again.')
    else:
        # Randomly generate the computer's choice
        cpu_choice = random.choice(throw_options)

        # Call functions to print the user's and computer's choices to the terminal and determine winner
        throwPlayer(player_choice)
        throwCPU(cpu_choice)
        whoWins(player_choice, cpu_choice)


main()