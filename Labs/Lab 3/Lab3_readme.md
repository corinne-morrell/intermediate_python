## How to Run
-----
To run this project from the terminal, enter `python Lab3.py`

## Inputs
-----
There are no inputs required to run the program.

Inputs could be implemented to allow the user to choose the predator and prey or to choose the initial distance between predator and prey before the chase begins.

## Outputs
-----
The program generates a single graph which simultaneously displays the displacements (as functions of time) of a hunting cheetah and a gazelle attempting to escape capture.


![Cheetah vs. Gazelle Figure - Initial Conditions](https://i.imgur.com/gpGxI4T.png)

>The figure above displays the trajectories calculated with the actual data for top speed and acceleration and pre-determined values for rate of exhaustion. The cheetah intersects the gazelle after approximately 2.8 seconds of pursuit, about 37 meters from the cheetah's starting point. The second intersection point indicates the time at which the cheetah would become exhausted and, if it had failed to catch the gazelle at the initial intersection, it would have no chance of capturing the gazelle beyond this point.

## Findings
-----
By manipulating the values for top speed, acceleration, and exhaustion rate of the cheetah, I was able to determine which factor is most likely to be most important for the cheetah to successfully capture the gazelle. Holding the values for the gazelle constant, I re-tested the simulation under the following conditions:

1. Top speed reduced by 50%
2. Acceleration reduced by 50%
3. Exhaustion rate doubled
4. Top speed increased by 50%
5. Acceleration increased by 50%

![Top Speed Reduced by 50%](https://i.imgur.com/h7eSomq.png)
> When top speed is reduced by 50%, the cheetah does not catch the gazelle. The cheetah's closest approach is approximately 8 meters.

![Acceleration Reduced by 50%](https://i.imgur.com/B1IpMho.png)
> When acceleration is reduced by 50%, the cheetah does not catch the gazelle. The cheetah's closest approach is approximately 19 meters.

![Exhaustion Rate Doubled](https://i.imgur.com/smeSoUr.png)
> When exhaustion rate is doubled, the cheetah still captures the gazelle. This occurs after approximately 3.0 seconds of pursuit at a distance of 40 meters from the cheetah's starting position.

![Top Speed Increased by 50%](https://i.imgur.com/qVRtPju.png)
> When top speed is increased by 50%, the cheetah successfully captures the gazelle. However, the capture occurs at the same time and displacement as the capture under initial conditions (2.8 seconds, 37 meters).

![Acceleration Increased by 50%](https://i.imgur.com/PKXtRF8.png)
> When acceleration is increased by 50%, the cheetah captures the gazelle approximately 0.8 seconds and 8 meters sooner than the capture under initial conidtions.

Based on these results, it seems that acceleration is the most important factor for the cheetah's success. Increasing top speed had virtually no effect. While increasing the cheetah's exhaustion rate did lead to a slightly slower capture, the differences compared to the initial conditions are negligible. The most dramatic changes occurred when acceleration was either decreased or increased.

## Concept Map
-----

To prepare for this lab, I created an algorithm flowchart.

![Lab 3 Prep](https://i.imgur.com/nh9PriC.jpeg)

This lab was the most challenging for me so far, and I ended up deviating from my original plan quite a bit. In the previous labs, I was able to define separate functions for each equation. I planned to do this with this lab, but having to use previously calculated values in each successive equation complicated the matter. I thought using a `for` loop to populate my lists would be the best solution for this problem. I ended up creating distinct functions for both predator and prey, with all of the necessary equations contained within. This approach also required that I establish initial conditions (i.e. top speed) within the functions in order for the loops to populate the lists properly, whereas I normally would have set values for those factors in the `main` function.


## Collaborators
-----

Daniel Hickey, who tutors me in programming in exchange for calculus tutoring, helped me with getting my loops to function properly. He sent me an example of a loop used for a similar problem (a population dynamics model, cited below) and helped me to de-bug my code.

## References
-----

Downey, A.B., Elkner, J., & Meyers, C. (2002.) Lists and for loops. *How to Think Like a Computer Scientist.* Runestone Interactive Project. https://runestone.academy/runestone/books/published/thinkcspy/Lists/Listsandforloops.html

>I referenced this source for general formatting for using a `for` loop in conjunction with a list.

Pritchard, A. (2017, May 29). *Markdown Cheatsheet.* GitHub. https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet

>I referenced this source to format this readme.

*Matplotlib.pyplot.legend.* Matplotlib.org. Retrieved Sep 12, 2020, from https://matplotlib.org/3.3.1/api/_as_gen/matplotlib.pyplot.legend.html.

> I referenced this source to include a legend on the graph.

The Digital Biologist. (2018, Sep 4). *Foxes & Chickens: A Population Dynamics Model in Five Lines of Python.* https://www.digitalbiologist.com/blog/2018/9/a-population-dynamics-model-in-five-lines-of-python

>I referenced this source to help me code my loops to populate my lists. Specifically, this helped me to identify how to index into my lists so the next iteration would use the previously calculated values.