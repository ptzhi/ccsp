'''
dna is made up by AGCT, 4choose3 is an amino acid (codon), a classic task in bioinformatics is to find a particular amino acid within a strand

we generate a gene with n nucleotides as base for our search algorithms
'''

from enum import IntEnum
from typing import Tuple, List

import random

## Create IntEnum class for DNA
# Nucleotide: IntEnum = IntEnum('Nucleotide', ('A', 'C','G','T'))

class Nucleotide(IntEnum):
    A=1
    C=2
    G=3
    T=4

# type hints
Codon = Tuple[Nucleotide, Nucleotide, Nucleotide]
Gene = List[Codon]

def generate_str(n: int) -> str:
    ords_lst = [ord(n.name) for n in Nucleotide]
    gene_lst = [chr(random.choice(ords_lst)) for _ in range(n)]
    gene_str = ''.join(gene_lst)
    return gene_str

def str_to_gene(s: str) -> Gene:
    gene: Gene = []
    for i in range(0, len(s), 3):
        if (i+2)>=len(s):
            return gene
        else:
            codon: Codon = (Nucleotide[s[i]], Nucleotide[s[i+1]], Nucleotide[s[i+2]])
            gene.append(codon)
    return gene


