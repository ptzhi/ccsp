"""
If working in spark we can define schema so that numerical data do not take up more space than required. For example, number of passengers per taxi driver per month does not need to be in DoubleType (8 byte double precision float). Instead it could be stored as IntegerType (4 byte int).

Python doesn't have off-the-shelf methods to accomplish this, so we can create our own functions to compress and decompress.

In this example we take nucleotides 'ACTG' which as string is 8x4=32 bits and convert to a bitstring representation e.g. A=00, C=01, T=11, G=10, which gives '00011110' and 2x4=8 bits (4x less space). 
"""

class CompressGene:
    def __init__(self, gene: str) -> None:
        self._compress(gene)

    _dict = {"A": 0b00, "C": 0b01, "T": 0b11, "G": 0b10}

    def _compress(self, gene: str):
        self.bit_string: int = 1 # sentinel
        for nucleotide in gene.upper():
            self.bit_string <<= 2
            self.bit_string |= self._dict[nucleotide]

    def decompress(self) -> str:
        gene: str = ""
        for i in range(0, self.bit_string.bit_length() - 1, 2): #exclude sentinel
            bits: int = self.bit_string >> i & 0b11
            if bits == 0b00:
                gene+= 'A'
            elif bits == 0b01:
                gene+= 'C'
            elif bits == 0b10:
                gene+= 'G'
            elif bits == 0b11:
                gene+= 'T'
        return gene[::-1]

    def __str__(self) -> str:
        return self.decompress()

if __name__ == '__main__':
    from sys import getsizeof
    original: str = 'ATCTCTGGCTACGATGCTTGACGACTG'
    print("original is {} bytes".format(getsizeof(original)))
    compressed: CompressGene = CompressGene(original)
    print("compressed is {} bytes".format(getsizeof(compressed.bit_string)))
    print(compressed)
    print("original and decompressed are the same: {}".format(original==compressed.decompress()))
    
