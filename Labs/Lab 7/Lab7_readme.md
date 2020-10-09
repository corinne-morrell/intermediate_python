## How to Run
-----
To run this program from the terminal, enter `python Lab7.py -d dna_filename -g gene_filename`, where `dna_filename` and `gene_filename` are the names of the `.txt` files containg the DNA strand and target gene, respectively, that you would like to test.

## Inputs
-----
The program requires command line arguments of `-d dna_filename` and `-g gene_filename`. If no file names are supplied in the command line, the user will receive a `no such file or directory` message.

![Example Input](https://i.imgur.com/lL0pykd.png)
![Example Input](https://i.imgur.com/EQtfRMa.png)
![Example Input](https://i.imgur.com/RBZfNY6.png)

## Outputs
-----
The program prints the DNA strand and target gene selected by the user in the command line. Then, it prints the best match to the target gene that exists within the DNA strand, as well as the similarity to the target gene, location of the best match within the strand, and any mutations present.

![Example Output](https://i.imgur.com/n2FpvGX.png)
![Example Output](https://i.imgur.com/ST1Lgqw.png)

## Findings
-----

This was a really interesting look into how genomics works. For me, it was also more great practice for learning to think algorithmically, as this lab was pretty challenging to conceptualize and debug at certain points.


## Concept Map
-----

To prepare for this lab, I created an algorithm flowchart.

![Lab 7 Prep](https://i.imgur.com/lNLA9lc.png)

The logic behind `def test_gene` turned out to be simpler than I had anticipated. The biggest challenge I faced was how to determine and print the best match from my list of possible matches. Overall, I found this lab really interesting. Since my coding experience is limited, the more complicated logic puzzles are both fun and challenging.

## Collaborators
-----

Devon Gardner and I wrote `def test_gene` together.

## References
-----

The only sources referenced in this lab were Professor Eaton's code examples for reading into files, and the command line arguments that I wrote in Lab 6.