'''
faster than linear, but requires some knowledge of structure ahead of time e.g. sorting 
O(log n) complexity if already sorted 
O(n log n) complexity if not sorted 
'''
from dna_sequence import Nucleotide, generate_str, str_to_gene, Codon, Gene

import random

Gene_sorted = sorted(Gene)

# must input a sorted struct
def binary_search_r(key: Codon, gene: Gene_sorted) -> bool:
    split = (len(gene))//2
    if key == gene[split]: # recursion end condition
        return True
    while len(gene)>1: 
        if key > gene[split]:
            return binary_search_r(key, gene[split:]) 
        else:
            return binary_search_r(key, gene[:split]) 
    return False


def binary_search_i(key: Codon, gene: Gene_sorted) -> bool:
    low = 0
    high = len(gene)-1 # length is index + 1
    while low <= high: #low == high is end of data 
        split = (low + high) // 2
        if key > gene[split]:
            low = split + 1 # when low==high, this kills the loop, also move past prev split
        elif key < gene[split]:
            high = split - 1 # when low==high, this kills the loop
        else:
            return True
    return False

#
def binary_search_position(key: Codon, raw: Gene) -> int:
    try:
        return raw.index(key)
    except ValueError:
        return None

if __name__ == '__main__':
#    gene_str = generate_str(12)
#    my_gene = str_to_gene(gene_str)
#    my_gene_sorted: Gene_sorted = sorted(my_gene)
#    my_codon = my_gene_sorted[-1]
#
#    num = [1,2,3,4]
#    my_codon: Codon = (
#            Nucleotide(random.choice(num)), 
#            Nucleotide(3), 
#            Nucleotide(4)) # to avoid making it too random
#   
    my_gene = random.sample(range(0,20),random.randint(10, 15))
    my_gene_sorted = sorted(my_gene)
    my_codon = random.randint(-10, 30) 
    print(f'''
    BINARY SEARCH 
    key: {my_codon}
    struct: {my_gene}
    sorted: {my_gene_sorted}
    lenght: {len(my_gene)}

    --Recursive
    {my_codon} is in gene: {binary_search_r(my_codon, my_gene_sorted)}
    at index {binary_search_position(my_codon, my_gene)}
    
    --Iterative
    {my_codon} is in gene: {binary_search_i(my_codon, my_gene_sorted)}
    at index {binary_search_position(my_codon, my_gene)}
    ''')
