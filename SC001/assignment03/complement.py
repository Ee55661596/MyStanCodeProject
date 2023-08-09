"""
File: complement.py
Name: 林劭懿 Ethan
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program provides different DNA sequence as
a python string that is case-sensitive.
Your job is to output the complement of them.
"""


def main():
    """
    This program asks uses for a DNA sequence,
    and finds the complement strand of a DNA sequence
    """
    print(build_complement('ATC'))
    print(build_complement(''))
    print(build_complement('ATGCAT'))
    print(build_complement('GCTATAC'))


def build_complement(dna):
    strand = ''
    if dna == '':
        print('DNA strand is missing.', end='')
    for i in range(len(dna)):
        alphabet = dna[i]
        if alphabet == 'A':
            strand = strand + 'T'
        elif alphabet == 'T':
            strand = strand + 'A'
        elif alphabet == 'C':
            strand = strand + 'G'
        else:
            strand = strand + 'C'
    return strand


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
