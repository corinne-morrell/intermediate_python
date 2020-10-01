# Cori Hatley
# 10- -20
# Intermediate Python
# Lab 7: Genomics
# Locate target gene in a strand of DNA

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
        possible.append("{0} == {1}: {2}, {3}, {4}% Match, Location: ({5}, {6})".format(test_gene, gene, match, partial, round(percent, 3), start, end))

    start += 1
    end += 1

for i in possible:
    print(i)