import random

# What I want to do is to add a while loop, keep the game going until the user does not want. Kepp the score,
# and end the game at 5.


def main():

    game_on = True
    while game_on:
        player = input("Welcome to Rock, Paper, Scissors Game!\nPlease enter your choice:\n").lower().strip()
        check_computer()
        checker(player, check_computer())
        game_on = keep_playing()
        '''
        if gameON = False:
            break
        else:
            gameON = True
    '''

def check_computer():
    choices = ["rock", "paper", "scissors"]
    computers_choice = random.choice(choices)
    return computers_choice


def checker(player, computers_choice):
    if computers_choice == player:
        print("The computer drew the same as you.\nIt is a tie!")
    elif player == "rock":
        if computers_choice == "paper":
            print("The computer drew paper.\nYou have lost! Paper covers rock!")
        else:
            print("The computer drew scissors.\nYou have won! Rock smashes scissors!")
    elif player == "paper":
        if computers_choice == "rock":
            print("The computer drew rock.\nYou have won! Paper covers rock!")
        else:
            print("The computer drew scissors.\nYou have lost! Scissors cut paper!")
    elif player == "scissors":
        if computers_choice == "rock":
            print("The computer drew rock.\nYou have lost! Rock smashes scissors!")
        else:
            print("The computer drew paper.\nYou have won! Scissors cut paper!")
    else:
        print("Oops! Something went wrong! Try to check your spelling.")

def keep_playing():
    while True:
        try:
            keep_playing = int(input("Do you want to keep playing?\nIf yes, type 1.\nIf no, type 2."))
        except ValueError:
            print("Oops! Something went wrong! Try to check your spelling.")
        else:
            if keep_playing == 1:
                game_state = True
                break
            elif keep_playing == 2:
                game_state = False
                print("Good game! You are always welcome. Stay safe!")
                break
    return game_state

main()