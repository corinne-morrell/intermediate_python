## How to Run
-----
To run this program from the terminal, enter `python Lab4.py` then enter your choice of `rock`, `paper`, or `scissors`.

## Inputs
-----
The program requires an input of `rock`, `paper`, or `scissors` to run. Inputs can be capitalized or lower case.

#### Examples:

![Example Input 1](https://i.imgur.com/W6LOZlH.png)
![Example Input 2](https://i.imgur.com/INgiGeo.png)

## Outputs
-----
The program prints a statement to reflect the user's choice and the computer's random choice, then determines the outcome of the game. If the user attempts to choose something other than `rock`, `paper`, or `scissors`, the program will print an error message.

#### Examples:

![Computer Wins](https://i.imgur.com/ycaN0Vp.png)
![Player Wins](https://i.imgur.com/Sl5ZcTW.png)
![Tie Game](https://i.imgur.com/0bSkrKh.png)
![Error Message](https://i.imgur.com/KblS8xb.png)

## Findings
-----

This program helped me understand ways that games can be designed to be unfair, whether in favor of the user or the computer. My program is not malicious, but I can see how I could manipulate the program to ensure that the computer always wins.

#### Examples:
![Malicious Program](https://i.imgur.com/pAMez4v.png)

## Concept Map
-----

To prepare for this lab, I created an algorithm flowchart.

![Lab 4 Prep](https://i.imgur.com/tHFVRFZ.png)

When preparing for this lab, I originally thought I would be able to classify each choice as being "greater than" another choice. In other words, I had hoped I would be able to establish that paper beats rock by writing `paper > rock` so I could then evaluate the outcome as follows:

![Example](https://i.imgur.com/fCnT0Pg.png)

Unfortunately, this didn't work. I had to evaluate the outcomes for each possible combination that would allow the computer to win, followed by an `else:` statement for the player to win.

Another tricky piece of writing this code was how to deal with incompatible user inputs. At first, my program would print the error message, then it would still randomly choose an option for the computer's throw and print a statement declaring the user as the winner. To correct this, I had to put the remaining function calls within an else statement so those functions would only be called after the user input was checked and confirmed to be compatible.


## Collaborators
-----

Nisa Genc reviewed my program and suggested that I add `.strip()` to my user input. This would prevent any spaces that the user enters from throwing an error message. She also recommended that I create a unique function to determine the outcome of the game. In my first draft, I determined the outcome within the main function.

Arthur Waddell also reviewed my program and recommended adding more spaces between lines of code to improve readability.

## References
-----

Caune, Peteris. (2008, Nov 20.) *How to randomly select an item from a list.* Stack Overflow. Retrieved Sep 9, 2020, from https://stackoverflow.com/questions/306400/how-to-randomly-select-an-item-from-a-list.

>I referenced this source for the proper syntax for randomly choosing an option for the computer's throw.