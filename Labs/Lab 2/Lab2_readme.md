## How to Run
-----
To run this project from the terminal, enter `python Lab2.py`

## Inputs
-----
Enter initial velocity (m/s) and launch angle (degrees, 0 < angle < 90) when prompted.

Additonal inputs could be implemented to:
  * change the initial position
  * change the magnitude of the acceleration due to gravity, i.e. to plot the trajectory of a projectile launched on the Moon

## Outputs
-----
The program will generate a graph that plots the trajectory of a ballistic projectile when given initial velocity and launch angle. The graph also displays printouts of the user input values (initial velocity and launch angle) and critical calculated values (maximum height, maximum range, and total time).

### Examples

![Projectile Figure 1](https://i.imgur.com/hY8Fnpl.png)

![Projectile Figure 2](https://i.imgur.com/pAUIOIp.png)

## Findings
-----

One complication I ran into while coding was an issue with both the landing time and maximum height functions returning negative values. I realized that I needed to use `g` = +9.81 m/s<sup>2</sup>, because even though the acceleration vector does point in the negative direction, the value of `g` is always positive. We only need to account for the downward direction of the acceleration in the vertical position function (by using -`g` instead of `g` = -9.81 m/s<sup>2</sup>).

## Concept Map
-----

To prepare for this lab, I created a flowchart using Lucidchart, which can be viewed [here.](https://app.lucidchart.com/invitations/accept/14dc5252-89b7-49b3-bae6-8bd9cb70e0a6)

My flowchart was extremely useful for helping me determine the best way to order my functions and function calls because it allowed me to visualize which functions would require the outputs of other functions. This is something that I struggled with in TDC2, but it's beginning to make more sense!


## Collaborators
-----

Devon Gardner and I discussed the use of different kinematic equations, such as a landing time equation that would work for any given initial position, as opposed to starting at (0,0), and an equation to determine the maximum height of the projectile.

## References
-----

*Basic Syntax.* Markdown Guide. Retrieved Sep 2, 2020, from https://www.markdownguide.org/basic-syntax/

> I referenced this source to format this `readme` using Markdown.

*How to Get 'Degree' Character in a String in Python.* (2010, Jul 9). Stack Overflow. Retrieved Sep 2, 2020, from https://stackoverflow.com/questions/3215168/how-to-get-character-in-a-string-in-python

> I referenced this source to add the degree character to the 'Launch Angle' text that appears on the graph.

*How to Round to 2 Decimals with Python.* (2013, Dec 8). Stack Overflow. Retrieved Sep 2, 2020, from https://stackoverflow.com/questions/20457038/how-to-round-to-2-decimals-with-python

> I referenced this source to format the float values in the text that appears on the graph.

*Literal String Interpolation.* (2015, Aug 1). Python.org. Retrieved Sep 2, 2020, from https://www.python.org/dev/peps/pep-0498/#how-to-denote-f-strings.

> I referenced this source to determine the correct syntax for an f-string, which I used to display the printout values on the graph.

*Pyplot Text.* Matplotlib.org. Retrieved Sep 2, 2020, from https://matplotlib.org/3.3.0/gallery/pyplots/pyplot_text.html#sphx-glr-gallery-pyplots-pyplot-text-py.

> I referenced this source to add the printout values that appear on the graph.

Serway, R.A. & Jewett, J.W. (2013). *Physics for Scientists and Engineers (9th ed.).* Cengage Learning.

> I referenced this source to look up the horizontal range formula for a projectile.

Yong, Cui. (2020, May 10). *String Formatting in Python - 6 Things to Know About F-Strings.* Medium. https://medium.com/swlh/string-formatting-in-python-6-things-to-know-about-f-strings-72fd38d96172#

> I referenced this source to create new lines for each printout value that appears on the graph so I wouldn't have to use `plt.text` multiple times. The code looks a little messier, but the output is cleaner.
