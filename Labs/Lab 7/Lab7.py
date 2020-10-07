# Cori Hatley
# 10-09-20
# Intermediate Python
# Lab 7: Genomics - Locate best possible match to target gene in a strand of DNA
# To run from the terminal, enter python Lab7.py -d dna_filename -g gene_filename

import os
import sys, getopt

def main(argv):
    ''' Initializes command line arguments and checks for problems with input, then
    calls find_match '''

    argv = argv[1:]
    dna_filename = ''
    gene_filename = ''
    
    try:
        opts, args = getopt.getopt(argv, "hd:g:")
    except getopt.GetoptError:
        print("test.py -d <dna_filename> -g <gene_filename>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            print("usage: test.py -d <dna_filename> -g <gene_filename>")
            sys.exit()
        elif opt == "-d":
            dna_filename = arg
        elif opt == "-g":
            gene_filename = arg
    
    find_match(dna_filename, gene_filename)


def find_match(dna_filename, gene_filename):
    ''' Scrubs through segments of DNA from dna_filename to determine the best possible match 
    to target gene in gene_filename; prints the DNA strand, the target gene, the best match, percent
    similarity of the best match to the target gene, position of the best match within the DNA strand,
    and any mutations present in the best match. '''

    # Call functions to read files and concatenate into strings
    dna_strand = ''.join(read_DNA(dna_filename))
    target_gene = ''.join(read_gene(gene_filename))

    # Initialize start and end positions for segment of dna_strand
    start = 0
    end = len(target_gene)
    
    # Initialize list to store information about all matches
    possible_match =[]

    #Initialize list to store similarity scores
    similarities = []

    # Initialize starting index value to check through each value in similarities list
    best_match = 0

    while end <= len(dna_strand):
        # Concatenate a string that contains a segment of dna_strand and is len(target_gene) long
        character_match = ''
        for i in range(start, end):
            character_match += dna_strand[i]

        # Check if character_match matches target_gene and returns a boolean value
        match = (character_match == target_gene)

        # Initialize empty lists for cataloguing partial matches and mutations
        partial = []
        mutations = []
        
        # Compare each character in character_match to target_gene and append boolean value to partial match list
        for i in range(len(target_gene)):
            partial.append(target_gene[i] == character_match[i])
            # If a character in character_match does not match target_gene, catalog the information about the mutation in mutations list
            if partial[i] == False:
                mutations.append("In position {0}, expected '{1}' but found '{2}'.\n".format([i], target_gene[i], character_match[i]))
        mut_string = ''.join(mutations)

        # Calculate percent similarity by counting occurences of True in partial match list
        percent = partial.count(True) / len(partial) * 100
        
        # Append calculated percent values to similarities list to track all potential matches
        similarities.append(percent)

        # Append a string of information about the matching gene to possible_match list
        possible_match.append("Best match: {0}\nSimilarity: {1}%\nGene Location: Position {2} - {3}\nMutations:\n{4}\n".format(character_match, round(percent, 3), start, end, mut_string))
        
        # Compare percent value calculated in each iteration of the loop to the previous percent value stored in similarities list
        if percent > similarities[best_match]:
            best_match = start

        # Update loop so each iteration of character_match starts at the next character in dna_strand
        start += 1
        end += 1

    # Print the DNA strand and target gene to the terminal
    print('\nDNA Strand: {0}\nTarget Gene: {1}\n'.format(dna_strand, target_gene))

    # Determine best match out of all matches by printing the item in possible_match at index [best_match]
    print(possible_match[best_match])

def read_gene(gene_filename):
    ''' Returns a list of strings in which each element is one line
    from the file. The filename must be a string. Assumes that the
    file is in the same directory as the program. '''
    
    # Format file path
    current_directory = os.path.dirname( __file__ )
    filepath = os.path.join( current_directory, gene_filename )

    # Open the file for reading ("r")
    input_file = open( filepath, "r" )

    # Store each line as an element in the list
    target_gene = []
    gene = input_file.readline()
    while len( gene ) > 0:	
        target_gene.append( gene )
        gene = input_file.readline()

    input_file.close()

    return target_gene

def read_DNA(dna_filename):
    ''' Returns a list of strings in which each element is one line
    from the file. The filename must be a string. Assumes that the
    file is in the same directory as the program. '''
    
    # Format file path
    current_directory = os.path.dirname( __file__ )
    filepath = os.path.join( current_directory, dna_filename )

    # Open the file for reading ("r")
    input_file = open( filepath, "r" )

    # Store each line as an element in the list
    dna_strand = []
    dna = input_file.readline()
    while len( dna ) > 0:	
        dna_strand.append( dna )
        dna = input_file.readline()

    input_file.close()

    return dna_strand

def test_gene():
    dna_strand = 'abcdeffhi'
    gene = 'def'
    start = 0
    end = len(gene)

    possible =[]

    while end <= len(dna_strand):
        test_gene = ''
        for i in range(start, end):
            test_gene += dna_strand[i]

        match = (test_gene == gene)
        partial = []

        for i in range(len(gene)):
            partial.append(gene[i] == test_gene[i])
        
        percent = partial.count(True) / len(partial) * 100

        if percent > 30:
            possible.append("{0} == {1}: {2}, {3}, {4}% Match, Start Position: {5}, Final Position: {6}".format(test_gene, gene, match, partial, round(percent, 3), start, end))

        start += 1
        end += 1

    for i in possible:
        print(i)

    print(test_gene)

if __name__ == "__main__":
    main(sys.argv)