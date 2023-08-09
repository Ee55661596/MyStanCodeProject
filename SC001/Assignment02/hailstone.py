"""
File: hailstone.py
Name: 林劭懿 Ethan
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


# This constant controls when to stop
EXIT = 1


def main():
    """
    This program simulates the execution of the Hailstone sequence,
    lists all the progress, and prints the number of steps (to reach 1).
    """
    data = int(input('Enter a number: '))
    if data == EXIT:
        print('It took 0 steps to reach 1.')
    else:
        step = 0
        while True:
            num = data
            if data == EXIT:
                break
            elif data % 2 == 0:
                even = data // 2
                data = even
                step = step + 1
                print(str(data) + ' is even, so I take half: '+ str(even))
                if data == EXIT:
                    print('It took ' + str(step) + ' steps to reach 1.')
                    break
            else:
                odd = 3 * data + 1
                data = odd
                step = step + 1
                print(str(data) + ' is odd, so I make 3n+1: ' + str(odd))




















# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
