"""
File: StoneMasonKarel.py
Name: 
--------------------------------
At present, the StoneMasonKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to build a column (a vertical structure
that is 5 beepers tall) in each avenue that is either on the right
or left side of the arch, as described in the Assignment 1 handout. 
Karel should end on the last avenue, 1st Street, facing east. 
"""

from karel.stanfordkarel import *


def main():
    while front_is_clear():
        build_up()
        build_down()
        move_4()
    build_up()
    build_down()

def move_4():
    """
    Pre-condition: karel is at the one of the pillar.
    Post-condition: karel move to the next pillar.
    """
    for i in range(4):
        move()

def build_up():
    """
    Pre-condition: Karel is at the bottom of the dom, facing east.
    Post-condition:Karel is at the top of the dom, facing north.
    """
    turn_left()
    if not on_beeper():
        put_beeper()
    while front_is_clear():
        move()
        while not on_beeper():
            put_beeper()

def build_down():
    """
    Pre-condition:Karel is at the top of the dom, facing north.
    post-condition: Karel is at the bottom of the dom, facing east.
    """
    turn_around()
    while front_is_clear():
        move()
    turn_left()

def turn_around():
    turn_left()
    turn_left()






# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
