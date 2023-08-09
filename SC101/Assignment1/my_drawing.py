"""
File: my_drawing.py
Name:Ethan 林劭懿
This is the Totoro. One of my favorite anime character.
He or maybe she is so adorable and heartwarming.
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect, GLine, GArc, GLabel
from campy.graphics.gwindow import GWindow


def main():
    """
    TODO:
    """
    window = GWindow(800, 600)
    # background
    background = GRect(window.width, window.height, x=0, y=0)
    background.filled = True
    background.fill_color = 'aqua'
    # ears_left
    ear_l = GOval(60, 100, x= (window.width-300)/2 + 30, y=100)
    ear_l.filled = True
    ear_l.fill_color = 'gray'
    # ear_r
    ear_r = GOval(60, 100, x= (window.width-300)/2 + 240, y=100)
    ear_r.filled = True
    ear_r.fill_color = 'gray'
    # body
    body = GOval(330, 360, x=(window.width-300)/2, y=120)
    body.filled = True
    body.fill_color = 'gray'

    # eye_l
    eye_l = GOval(50, 50, x=(window.width-300)/2 + 50, y=200)
    eyeball_l = GOval(30, 30, x=(window.width-300)/2 + 60, y=210)
    eye_l.filled = True
    eye_l.fill_color = 'ivory'
    eyeball_l.filled = True
    eyeball_l.fill_color = 'black'
    # eye_r
    eye_r = GOval(50, 50, x=(window.width-300)/2 + 220, y=200)
    eyeball_r = GOval(30, 30, x=(window.width-300)/2 + 230, y=210)
    eye_r.filled = True
    eye_r.fill_color = 'ivory'
    eyeball_r.filled = True
    eyeball_r.fill_color = 'black'
    # mouth
    mouth = GLine(x0=(window.width-300)/2 + 150, y0=260, x1=(window.width-300)/2 + 170, y1=260)
    # body_line
    arc = GArc(325, 200, 0, 180, x=(window.width-300)/2 + 3, y=280)
    # body_arc_l
    body_arc_l = GArc(50, 40, 0, 220, x=(window.width-300)/2 + 50, y=310)
    body_arc_l.filled = True
    body_arc_l.fill_color = 'ivory'
    # body_arc_m
    body_arc_m = GArc(50, 40, 0, 220, x=(window.width-300)/2 + 150, y=310)
    body_arc_m.filled = True
    body_arc_m.fill_color = 'ivory'
    # body_arc_r
    body_arc_r = GArc(50, 40, 0, 220, x=(window.width-300)/2 + 250, y=310)
    body_arc_r.filled = True
    body_arc_r.fill_color = 'ivory'
    # right hand
    right_hand = GOval(30, 50, x=(window.width-300)/2 + 290, y=255)
    right_hand.filled = True
    right_hand.fill_color = 'gray'
    # left hand
    left_hand = GOval(60, 80, x=(window.width-300)/2-20, y=255)
    left_hand.filled = True
    left_hand.fill_color = 'gray'
    # left feet left toe
    left_feet_toe_l = GOval(20, 50, x= (window.width-300)/2 + 50, y=420)
    left_feet_toe_l.filled = True
    left_feet_toe_l.fill_color = 'ivory'
    # left feet middle toe
    left_feet_toe_m = GOval(20, 40, x= (window.width-300)/2 + 65, y=430)
    left_feet_toe_m.filled = True
    left_feet_toe_m.fill_color = 'ivory'
    # left feet right toe
    left_feet_toe_r = GOval(20, 30, x= (window.width-300)/2 + 80, y=440)
    left_feet_toe_r.filled = True
    left_feet_toe_r.fill_color = 'ivory'

    # right feet right toe
    right_feet_toe_r = GOval(20, 30, x= (window.width-300)/2 + 240, y=430)
    right_feet_toe_r.filled = True
    right_feet_toe_r.fill_color = 'ivory'
    # right feet middle toe
    right_feet_toe_m = GOval(20, 40, x= (window.width-300)/2 + 255, y=420)
    right_feet_toe_m.filled = True
    right_feet_toe_m.fill_color = 'ivory'
    # left feet left toe
    right_feet_toe_l = GOval(20, 50, x= (window.width-300)/2 + 270, y=420)
    right_feet_toe_l.filled = True
    right_feet_toe_l.fill_color = 'ivory'

    # umbrella
    rect_u = GRect(20, 120, x=(window.width-300)/2 + 310, y=165)
    rect_u.filled = True
    rect_u.fill_color = 'green'

    # umbrella surface
    surface_u = GOval(200, 90, x=(window.width-300)/2 + 300, y=135)
    surface_u.filled = True
    surface_u.fill_color = 'green'

    # surface arc
    surface_arc = GArc(200, 90, 0, 170,x=(window.width-300)/2 + 300, y=165)

    # label
    label = GLabel('Totoro')
    label.font = '-80'


    window.add(background)
    window.add(ear_l)
    window.add(ear_r)
    window.add(left_hand)
    window.add(left_feet_toe_l)
    window.add(left_feet_toe_m)
    window.add(left_feet_toe_r)
    window.add(right_feet_toe_l)
    window.add(right_feet_toe_m)
    window.add(right_feet_toe_r)
    window.add(body)
    window.add(eye_l)
    window.add(eyeball_l)
    window.add(eye_r)
    window.add(eyeball_r)
    window.add(mouth)
    window.add(arc)
    window.add(body_arc_l)
    window.add(body_arc_m)
    window.add(body_arc_r)
    window.add(right_hand)
    window.add(rect_u)
    window.add(surface_u)
    window.add(surface_arc)
    window.add(label, x=0, y=label.height+10)

if __name__ == '__main__':
    main()
