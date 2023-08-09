"""
File: bouncing_ball.py
Name: Ethan 林劭懿
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
window = GWindow(800, 500, title='bouncing_ball.py')


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    # Set up the ball
    set_oval()
    # Bounce
    onmouseclicked(move)


def set_oval():
    oval = GOval(SIZE, SIZE, x=START_X, y=START_Y)
    oval.filled = True
    oval.fill_color = 'Blue'
    window.add(oval)


def move(mouse):
    global VX
    vy = 0
    ori = window.get_object_at(mouse.x, mouse.y)
    if ori is not None:
        window.remove(ori)
        oval_new = GOval(SIZE, SIZE, x=START_X, y=START_Y)
        oval_new.filled = True
        oval_new.fill_color = 'Blue'
        window.add(oval_new)
        while True:
            if oval_new.x+SIZE/2 >= START_X and oval_new.y >= START_Y:
                oval_new.move(VX, vy)
                pause(DELAY)
                vy += GRAVITY
            if oval_new.y > (window.height - SIZE) and vy > 0:
                vy *= -REDUCE
            # outside the window
            if oval_new.x >= window.width:
                window.remove(oval_new)
                set_oval()
                break


if __name__ == "__main__":
    main()
