"""
File: MidpointKarel.py
Name: 林劭懿 Ethan
----------------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""

from karel.stanfordkarel import *


def main():
    """

    """
    while facing_east() or facing_west():
        if on_beeper():
            pick_beeper()
            turn_around()
            move()
            if not on_beeper():
                put_beeper()
                move()
            else:
                turn_left()




        else:
            if not front_is_clear():
                turn_around()
                put_beeper()
            if not front_is_clear():
                turn_left()
            else:
                move()


def turn_around():
    for i in range(2):
        turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
