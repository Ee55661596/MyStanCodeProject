"""
File: CollectNewspaperKarel.py
Name: 
--------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""

from karel.stanfordkarel import *


def main():
    pick()
    drop()

def pick():
    """
    Pre-condition: Karel is northwest corner, facing east
    post-condition:karel is at the entrance, facing west
    """
    move()
    move()
    turn_right()
    move()
    turn_left()
    move()
    pick_beeper()
    turn_around()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_around():
    turn_left()
    turn_left()

def drop():
    """
    Pre-condition:karel is at the entrance, facing west
    Post-condition: Karel is northwest corner holding beeper, facing east
    """
    move()
    turn_right()
    move()
    turn_left()
    move()
    move()
    turn_around()
    put_beeper()










# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
