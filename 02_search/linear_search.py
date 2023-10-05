'''
search through every element in sequence for the key
O(n) complexity where n is the number of elements in the sequence
'''

from dna_sequence import Nucleotide, generate_str, str_to_gene, Codon, Gene


def linear_search(key: Codon, gene: Gene) -> bool:
    return key in gene

def linear_search_position(key: Codon, gene: Gene) -> int:
    position = 0
    for codon in gene:
        position +=1
        if key == codon:
            return position
    return "not present" 

if __name__ == '__main__':
    gene_str = generate_str(100)
    my_gene = str_to_gene(gene_str)
    my_codon: Codon = (Nucleotide.A, Nucleotide.G, Nucleotide.T)
    print(f'''
          LINEAR SEARCH
          {my_codon} is in gene: {linear_search(my_codon, my_gene)}
          at position {linear_search_position(my_codon, my_gene)}
    ''')
