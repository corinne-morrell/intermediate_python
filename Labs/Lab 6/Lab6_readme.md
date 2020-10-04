## How to Run
-----
To run this program from the terminal, enter `python Lab6.py -i filename -x x_column -y y_column`, where `filename` is the name of the CSV file you would like to visualize, and `x_column` and `y_column` are the columns you would like to plot.

## Inputs
-----
The program requires command line arguments of `-i filename`, `-x x_column`, and `-y y_column`. If the x- and y-columns are not specified, the program will automatically plot the first two columns in the CSV file. If no filename is supplied in the command line, the user will receive an `no such file or directory` message.

#### Examples:

![Example with all 3 command line args](https://i.imgur.com/nR2QuC1.png)
![Example with only file name given](https://i.imgur.com/xGOWp3W.png)
![Example with no file name given](https://i.imgur.com/T42LGzC.png)

## Outputs
-----
The program prints a statement that indicates the user's choice of CSV file, x-column, and y-column. The program also prints the header names of the chosen columns, as well as lists of the values contained within each column. Finally, the program produces a figure containing a scatterplot and a bar graph of the data from the CSV file.

#### Examples:

![Print Statement](https://i.imgur.com/nR2QuC1.png)
![Figure](https://i.imgur.com/xG0RAmE.png)

## Findings
-----

I thought it would be interesting to see if I could produce a Hertzsprung-Russell diagram using this program. A Hertzsprung-Russell, or HR, diagram is a scatter plot of stars that shows the relationship between luminosity and surface temperature and is an important tool for studying stellar evolution. I found a few open source files containing massive amounts of stellar data obtained from the Hipparcos satellite. The smallest file I could find contained data from nearly 100,000 stars. I was able to scale the file down to about 10,000 stars, but I ran into a problem with the program throwing errors when it came to formatting the contents to float values. I'll keep working on it though!

#### Examples:
![HR Diagram](https://upload.wikimedia.org/wikipedia/commons/9/95/HRDiagram.jpg)

## Concept Map
-----

To prepare for this lab, I created an algorithm flowchart.

![Lab 6 Prep](https://i.imgur.com/lpnzWyI.png)

Figuring out how to convert rows into columns was tricky, but had a logical solution. The most challenging part of this lab was the implementation of command line arguments. I found this difficult because I was working from the example provided in the lab instructions, and it was challenging to try to understand the syntax and convert variables into what was needed for this program.

## Collaborators
-----

Devon Gardner and I worked together closely on this lab. He helped me understand command line arguments and we collaborated on how to convert the rows from the CSV file into columns.

## References
-----

*Plotting Categorical Variables.* Matplotlib.org. Retrieved Sep 30, 2020, from https://matplotlib.org/gallery/lines_bars_and_markers/categorical_variables.html#sphx-glr-gallery-lines-bars-and-markers-categorical-variables-py.

> I referenced this source to format the subplots of the output figure.

*Python - Command Line Arguments.* TutorialsPoint.com. Retreived Sep 30, 2020, from https://www.tutorialspoint.com/python/python_command_line_arguments.htm

> I referenced this source for learning how to implement command line arguments.