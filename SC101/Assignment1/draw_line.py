"""
File: draw_line.py
Name: Ethan 林劭懿
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked
# control the size of the circle
SIZE = 10
WIDTH = 600
HEIGHT = 800
# global variable
window = GWindow(width=WIDTH, height=HEIGHT, title='Draw Line')
click_n = 0
oval = GOval(SIZE, SIZE)


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    # start click
    onmouseclicked(draw)


def draw(mouse):
    global click_n

    click_n += 1
    if click_n % 2 == 1:
        window.add(oval, x=mouse.x-SIZE/2, y=mouse.y-SIZE/2)

    else:
        line = GLine(oval.x+SIZE/2, oval.y+SIZE/2, mouse.x, mouse.y)
        window.add(line)
        window.remove(oval)





if __name__ == "__main__":
    main()
