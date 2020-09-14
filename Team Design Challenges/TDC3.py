# Cori Hatley
# 09-14-2020
# Team Design Challenge: play a game of rock-paper-scissors with user inputs and randomly generated computer throws
# To run, enter TDC3.py in the terminal, then enter your choice of rock, paper, or scissors

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

def main():
    # Establish acceptable throw options
    throw_options = ['rock', 'paper', 'scissors']
    
    # Allow user to choose rock, paper, or scissors
    player_choice = (input('Rock, paper, or scissors?')).lower()
    if player_choice not in throw_options:
        print('You must choose either rock, paper, or scissors. Try again.')
    else:
        # Randomly generate the computer's choice
        cpu_choice = random.choice(throw_options)

        # Call functions to print the user's and computer's choices to the terminal
        throwPlayer(player_choice)
        throwCPU(cpu_choice)

        # Determine outcome of the game
        if cpu_choice == player_choice:
            print('It\'s a tie. Try again.')
        elif cpu_choice == 'rock' and player_choice == 'scissors':
            print('The computer wins.')
        elif cpu_choice == 'paper' and player_choice == 'rock':
            print('The computer wins.')
        elif cpu_choice == 'scissors' and player_choice == 'paper':
            print('The computer wins.')
        else:
            print('You win!')

main()