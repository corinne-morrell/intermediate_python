# Cori Hatley
# 09-17-2020
# Mini Design Challenge: Dice

import random

def roll_doubles():
    
    di1 = random.randint(1, 6)
    di2 = random.randint(1, 6)

    rolls = 1

    while di1 != di2:
        rolls += 1
        di1 = random.randint(1, 6)
        di2 = random.randint(1, 6)

    return rolls

def average_doubles():
    trials = 0
    total_rolls = 0
    while trials <= 1000:
        additional_rolls = roll_doubles()
        total_rolls += additional_rolls
    average = total_rolls/1000
    return average

def main():
    average_rolls = average_doubles()
    print(average_rolls)

if __name__ == "__main__":
    main()
    