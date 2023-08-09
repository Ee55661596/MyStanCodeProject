"""
File: rocket.py
Name: 林劭懿 Ethan
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 3 Handout.

"""

# This constant determines rocket size.
# SIZE = jerry


def main():
    """
    This program can depict a rocket, and the size od the rocket is control by the constant SIZE
    """
    word = str(input('Word : '))
    # Capital Sensitive
    word = word.upper()
    upper(word)
    lower(word)


def upper(word):
    ch = ''
    for i in range (len(word)):
        ch += word[i]
        print(ch)


def lower(word):
    for i in range(len(word)-1):
        for j in range(i+1):
            print(" ", end='')
        print(word[i+1:])











#     head()
#     belt()
#     upper()
#     lower()
#     belt()
#     head()
#
#
# def lower():
#     for i in range(SIZE):
#         print('|', end='')
#         for j in range(i):
#             print(".", end='')
#         for j in range(SIZE-i):
#             print("\\/", end='')
#         for j in range(i):
#             print(".", end='')
#         print('|', end='')
#         print('')
#
#
# def upper():
#     for i in range(SIZE):
#         print('|', end='')
#         for j in range(SIZE - (i+1)):
#             print(".", end='')
#         for j in range(i+1):
#             print("/\\", end='')
#         for j in range(SIZE - (i+1)):
#             print(".", end='')
#         print('|', end='')
#         print('')
#
#
# def belt():
#     print('+', end='')
#     for i in range(SIZE*2):
#         print('=' , end='')
#     print('+', end='')
#     print('')
#
#
# def head():
#     for i in range(SIZE):
#         for j in range(SIZE - i):
#             print(" ", end='')
#         for j in range(i+1):
#             print("/", end='')
#         for j in range(i+1):
#             print("\\", end='')
#         print('')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
