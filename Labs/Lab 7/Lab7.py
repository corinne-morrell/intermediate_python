# Cori Hatley
# 10-09-20
# Intermediate Python
# Lab 7: Genomics
# Locate best possible match to target gene in a strand of DNA

import os
import sys, getopt

def main(argv):
    ''' Initializes command line arguments and checks for problems with input '''
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
        
    print('DNA Strand: {0}, Target Gene: {1}'.format(dna_filename, gene_filename))
    
    find_match(dna_filename, gene_filename)


def find_match(dna_filename, gene_filename):
    dna_strand = ''.join(read_DNA(dna_filename))
    target_gene = ''.join(read_gene(gene_filename))
    start = 0
    end = len(target_gene)
    
    possible_match =[]

    while end <= len(dna_strand):
        character_match = ''
        for i in range(start, end):
            character_match += dna_strand[i]

        match = (character_match == target_gene)
        partial = []

        for i in range(len(target_gene)):
            partial.append(target_gene[i] == character_match[i])
        
        percent = partial.count(True) / len(partial) * 100

        # loop to only keep best match? check through "possible" list
        if percent > 50:
            possible_match.append("{0} == {1}: {2}, {3}, Similarity: {4}%, Start Position: {5}, Final Position: {6}".format(character_match, target_gene, match, partial, round(percent, 3), start, end))

        start += 1
        end += 1

    print("\nPossible Matches\n")
    for i in possible_match:
       print(i)


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