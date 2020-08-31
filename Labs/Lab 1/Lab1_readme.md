## How to Run
-----
To run this project from the terminal, enter `python Lab1.py`

## Inputs
-----
There are no inputs required to run the program.

Arbitrary values were chosen for the constants in the sine and cubic functions. Inputs could be implemented to manipulate the graphs of these functions.

For the third function, the aim was to find the limit as x approaches zero. Simply inputting zero into the function would produce an error.

### Examples

For the sine wave (**y = Asin(Bx-C)+D**):
  * (A) would affect amplitude
  * (B) would affect period
  * (C) would affect horizontal translation
  * (D) would affect vertical translation

Using inputs to perform transformations on the cubic polynomial would be more convenient if the function was converted from

**y = ax<sup>3</sup>+bx<sup>2</sup>+cx+d**

to the form

**y = a(x-h)<sup>3</sup>+k**

The variables h and k could then be input to manipulate the graph as follows:

  * (h) would affect horizontal translation
  * (k) would affect vertical translation



## Outputs
-----
The project will generate three graphs:
1. A sine wave
2. A cubic polynomial
3. An elusive limit

### Examples

![Sine Wave Figure](https://i.imgur.com/G8moPqW.png)

![Cubic Polynomial Figure](https://i.imgur.com/OLlfpQm.png)

![Elusive Limit Figure](https://i.imgur.com/tVNl3Qz.png)

## Findings
-----
I am familiar with the behavior of the graphs of sine and cubic functions, so the outputs were no surprise.

The third equation in the program attempted to model the following limit:

![Elusive Limit](https://i.imgur.com/0SiZ279.png)

 The limit was given to me by my Calculus II professor nearly a year ago as a challenge. I have tried to solve this limit by using L'Hopital's rule, representing the function as a power series... to no avail.

 Unfortunately, graphing the limit did not help. Regardless of how many points are plotted, the graph becomes unreadable as x approaches zero because the function oscillates wildly. This leads me to believe that the limit does not exist, but I still want proof.

## Concept Map
-----

To prepare for this lab, I created an outline in Google Slides, which can be viewed [here.](https://docs.google.com/presentation/d/1GcceN8GR_AM_VNhqFKPyQHaH_cMxy3mCJVEfDDdIYDg/edit?usp=sharing)

In my outline, I included the appropriate x- and y-scales for each function that I intended to use for my graphs. Unfortunately, while coding the project, I could not figure out how to display the scale I had chosen. I thought using `np.arange` would at least determine the x-scale, but this was not the case. Each graph displays a generic grid with generic tick labels. I have not yet found a solution to this issue.


## Collaborators
-----

Devon Gardner, my lab partner, assisted me by suggesting using Markdown for this readme. Devon taught me how to generate all three figures at once so I could consolidate my code into a single file instead of three separate files. He also recommended using `np.linspace` instead of `np.arange` for the limit problem, which allowed for more of the graph to be displayed.

Daniel Hickey, who tutors me in all things software in exchange for calculus tutoring, suggested the use of `np.arange`.

## References
-----

Miller, A. (2017, Oct 2). *Markdown Syntax for Superscript and Subscript.* Github. https://github.com/getgrav/grav/issues/1672

*I used this source to format this readme; specifically, I used it to create superscripts for the cubic polynomial function.*

Pritchard, A. (2017, May 29). *Markdown Cheatsheet.* GitHub. https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet

*I used this source to format this readme.*

Ramos, J. (2017, Aug 10). *LaTex Rendering in `README.md` on Github.* Stack Overflow. https://stackoverflow.com/questions/35498525/latex-rendering-in-readme-md-on-github

*Following this user's suggestion, I rendered the limit equation using [EqnEditor Render](https://latex.codecogs.com). I then took a screenshot of the LaTex-formatted equation and embedded it into this readme.*

