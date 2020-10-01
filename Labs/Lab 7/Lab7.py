# Cori Hatley
# 10- -20
# Intermediate Python
# Lab 7: Genomics
# Locate target gene in a strand of DNA

dna_strand = 'abcdefghi'
gene = 'def'
start = 0
end = len(gene)



while end <= len(dna_strand):
    test_gene = []
    for i in range(start, end):
        test_gene.append(dna_strand[i])
    start += 1
    end += 1

    print(test_gene)