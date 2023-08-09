"""
File: CheckerboardKarel.py
Name: 林劭懿 Ethan
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds provided in the starter folder.
"""

from karel.stanfordkarel import *


def main():
    """

    """
    while front_is_clear():
        build_1()
        build_2()
    if front_is_clear():
        build_1()
        if front_is_clear():
            build_2()
            build_1()
        else:
            build_2()
    else:
        if  front_is_clear():
            build_1()









def build_1():
    """
    Pre-condition:karel didn't mark the beeper yet,facing east.
    Post-condition: karel mark a straight line of beeper start from the bottom, with bottom being marked and facing east.
    """
    turn_left()
    put_beeper()
    up_1()
    down()
    if front_is_clear():
        move()

def build_2():
    """
    Pre-condition: Karel didn't mark the beeper yet.
    Post-condition: Karel karel mark a straight line of beeper start from the bottom, without bottom being marked and facing east.
    """
    turn_left()
    up_2()
    down()
    if front_is_clear():
        move()


def up_2():
    """
    Pre-condition: Karel is at the bottom of the street without beeper, facing east.
    Post-condition: Karel is at the top of the street without beeper, facing north.

    """
    if front_is_clear():
        move()
        put_beeper()
        while front_is_clear():
            move()
            if front_is_clear():
                move()
                put_beeper()



def up_1():
    """
    Pre-condition: karel at the bottom of street, with beeper.
    Post-condition: Karel at the top of the street, with beeper.
    """

    while front_is_clear():
        move()
        if front_is_clear():
            move()
            put_beeper()

def down():
    """
    Pre-condition: Karel is at the top of the street, facing north.
    Post-condition: Karel is at the bottom of the street, facing east.
    """
    turn_around()
    while front_is_clear():
        move()
    turn_left()

def turn_right():
    for i in range(3):
        turn_left()

def turn_around():
    for i in range(2):
        turn_left()





































    # put_beeper()
    # turn_left()
    # while front_is_clear():
    #     up()
    #     down()
    #     move()


# def up():
#     while front_is_clear():
#         move()
#         check_back()
#         check_front()
#     check_back()
#     check_front()
#
# def down():
#     turn_around()
#     while front_is_clear():
#         move()
#     turn_left()
#
#
#
#
#
# def check_back():
#     turn_around()
#     if front_is_clear():
#         move()
#         if on_beeper():
#             turn_around()
#             move()
#         else:
#             turn_around()
#             move()
#             put_beeper()
#
#
# def check_front():
#     if front_is_clear():
#         move()
#         if on_beeper():
#             turn_around()
#             move()
#             turn_around()
#         else:
#             turn_around()
#             move()
#             if not on_beeper():
#                 put_beeper()
#                 turn_around()
#             else:
#                 turn_around()






































    # while front_is_clear():
    #     up()
    #     down()
    #     move()
    # up()
    # down()


# def check_front():
#     while front_is_clear():
#
#
#         move()
#         if on_beeper():
#             turn_around()
#             move()
#             put_beeper()
#             turn_around()
#         else:
#             turn_around()
#             move()
#             put_beeper()
#             turn_around()



# def up():
#     while front_is_clear():
#         move()
#         check_around_beepers()
#         turn_right()
#
# def down():
#     while not front_is_clear():
#         turn_around()
#         move()
#     while front_is_clear():
#         move()
#         turn_left()
#
# def check_around_beepers():
#     check_s()
#     check_e()
#     check_n()
#     check_w()
#
# def check_s():
#     """
#     Pre-condition: Karel is at Street 1, Avenue 1 and don't know whether southside of it having beeper , facing east
#     Post-condition: Karel is at Street 1, Avenue 1 and have find out southside of it having beeper  , facing south
#     """
#     turn_right()
#     if front_is_clear():
#         move()
#         while not on_beeper():
#             turn_around()
#             move()
#             put_beeper()
#             turn_around()
#
#         turn_around()
#         move()
#         turn_around()

#
# def check_e():
#     """
#     Pre-condition:Karel is at Street 1, Avenue 1 and don't know whether eastside of it having beeper , facing south
#     Post-condition: Karel is at Street 1, Avenue 1 and have find out eastside of it having beeper , facing east.
#     """
#     turn_left()
#     if front_is_clear():
#         move()
#         while not on_beeper():
#             turn_around()
#             move()
#             while not on_beeper():
#                 put_beeper()
#                 turn_around()
#             turn_around()
#
#         turn_around()
#         move()
#         turn_around()
#
# def check_n():
#     """
#     Pre-condition: Karel is at Street 1, Avenue 1 and don't know whether northside of it having beeper , facing east.
#     Post-condition: Karel is at Street 1, Avenue 1 and have find out northside of it having beeper , facing north.
#     """
#     turn_left()
#     if front_is_clear():
#         move()
#         while not on_beeper():
#             turn_around()
#             move()
#             while not on_beeper():
#                 put_beeper()
#                 turn_around()
#             turn_around()
#         turn_around()
#         move()
#         turn_around()
#
# def check_w():
#     """
#     Pre-condition: Karel is at Street 1, Avenue 1 and don't know whether westside of it having beeper  , facing north.
#     Post-condition:　Karel is at Street 1, Avenue 1 and have find out northside of it having beeper  , facing west.
#     """
#     turn_left()
#     if front_is_clear():
#         move()
#         while not on_beeper():
#             turn_around()
#             move()
#             while not on_beeper():
#                 put_beeper()
#                 turn_around()
#             turn_around()
#         turn_around()
#         move()
#         turn_around()












# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
