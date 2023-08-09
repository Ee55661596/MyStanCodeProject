"""
File: caesar.py
Name:林劭懿 Ethan
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    This program demonstrates the idea of caesar cipher.
    """
    data = int(input('Secret number: '))
    code = str(input("What's the ciphered string? "))
    new_seq = move(data)
    transmit = transfer(code, new_seq)
    print('The deciphered string is: ' + str(transmit))


def move(data):
    """
    Try to generate the new sequence of the alphabet
    :param    data: int, the  amount of displacement.
    :return   new_seq: str, the new sequence of the alphabet.
    """
        new_seq = ''
        new_seq += ALPHABET[26 - data:]
        new_seq += ALPHABET[:26 - data]
        return new_seq


def transfer(code, new_seq):
    """
    Try to decipher the code.
    """
    transmit = ''
    # case-insensitive
    code = code.upper()
    for i in range(len(code)):
        code_seq = code[i]
        if code_seq.isalpha():
            transmit += ALPHABET[new_seq.find(code_seq)]
        else:
            transmit += code_seq
    return transmit


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
