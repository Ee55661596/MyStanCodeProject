"""
File: babygraphics.py
Name: 
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    x_coordinate = int((width / len(YEARS)) * int(year_index))
    # the string is qualified, because the sequence of the year must follow the sequence of 1900 1910....
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, width=LINE_WIDTH, fill='black')
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, width=LINE_WIDTH, fill='black')
    # vertical line (left)
    canvas.create_line(GRAPH_MARGIN_SIZE, 10, GRAPH_MARGIN_SIZE, 590, width=LINE_WIDTH, fill='black')
    # vertical line (rest)
    for i in range(len(YEARS)):
        canvas.create_line(GRAPH_MARGIN_SIZE + get_x_coordinate(CANVAS_WIDTH - 2 * GRAPH_MARGIN_SIZE, i),
                           GRAPH_MARGIN_SIZE - 30,
                           GRAPH_MARGIN_SIZE + get_x_coordinate(CANVAS_WIDTH - 2 * GRAPH_MARGIN_SIZE, i),
                           CANVAS_HEIGHT - GRAPH_MARGIN_SIZE + 35, width=LINE_WIDTH)
    # add year text
        canvas.create_text(GRAPH_MARGIN_SIZE + get_x_coordinate(CANVAS_WIDTH - 2 * GRAPH_MARGIN_SIZE, i) + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, text=YEARS[i], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #

    # set a x distance between vertical lines and y distance for the ?/1000
    x_dis = int((CANVAS_WIDTH - 2*GRAPH_MARGIN_SIZE) / 12)
    y_dis = int(CANVAS_HEIGHT - 2*GRAPH_MARGIN_SIZE) / 1000

    # set the y coordinate when the rank is out of 1000
    y_minimum = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE

    # nested for to loop every names and every years
    for i in range(len(lookup_names)):
        name = lookup_names[i]
        print(name)              #for checking

        # set rank, next_rank; year, next_year to create line and assign 1001 to the rank or next_rank if the rank is out of 1000
        for j in range(len(YEARS)-1):
            year = YEARS[j]
            print(year)#for checking

            if str(year) in name_data[name]:
                rank = int(name_data[name][str(year)])
                print(rank)#for checking

            else:
                rank = 1001
                print(rank)#for checking

            next_year = YEARS[j+1]
            print(next_year)#for checking

            if str(next_year) in name_data[name]:
                next_year_rank = int(name_data[name][str(next_year)])
                print(next_year_rank)#for checking
            else:
                next_year_rank = 1001
                print(next_year_rank)#for checking

    # combinations of rank < 1000 and rank > 1000
            if rank > 1000 and next_year_rank > 1000:
                canvas.create_line(GRAPH_MARGIN_SIZE + j*x_dis, y_minimum, GRAPH_MARGIN_SIZE + (j+1)*x_dis, y_minimum,
                                   fill=COLORS[i % 4], width=LINE_WIDTH)
                canvas.create_text(GRAPH_MARGIN_SIZE + j*x_dis + TEXT_DX, y_minimum, text=name + '*', fill=COLORS[i % 4], anchor=tkinter.SW)
                print('both >1000')

            elif rank > 1000 and next_year_rank < 1000:
                canvas.create_line(GRAPH_MARGIN_SIZE + j*x_dis, y_minimum,
                                   GRAPH_MARGIN_SIZE + (j+1)*x_dis, GRAPH_MARGIN_SIZE + next_year_rank*y_dis,
                                   fill=COLORS[i % 4], width=LINE_WIDTH)
                canvas.create_text(GRAPH_MARGIN_SIZE + j * x_dis + TEXT_DX, y_minimum, text=name + '*',
                                   fill=COLORS[i % 4], anchor=tkinter.SW)
                print('rank>1000 but next<1000')

            elif rank < 1000 and next_year_rank < 1000:
                canvas.create_line(GRAPH_MARGIN_SIZE + j * x_dis, GRAPH_MARGIN_SIZE + rank*y_dis,
                                   GRAPH_MARGIN_SIZE + (j + 1) * x_dis, GRAPH_MARGIN_SIZE + next_year_rank * y_dis,
                                   fill=COLORS[i % 4], width=LINE_WIDTH)
                canvas.create_text(GRAPH_MARGIN_SIZE + j * x_dis + TEXT_DX, GRAPH_MARGIN_SIZE + rank * y_dis, text=name + str(rank),
                                   fill=COLORS[i % 4], anchor=tkinter.SW)
                print('both<1000')

            elif rank <1000 and next_year_rank > 1000:
                canvas.create_line(GRAPH_MARGIN_SIZE + j * x_dis, GRAPH_MARGIN_SIZE + rank * y_dis,
                                   GRAPH_MARGIN_SIZE + (j + 1) * x_dis, y_minimum,
                                   fill=COLORS[i % 4], width=LINE_WIDTH)
                canvas.create_text(GRAPH_MARGIN_SIZE + j * x_dis + TEXT_DX, GRAPH_MARGIN_SIZE + rank * y_dis, text=name + str(rank),
                                   fill=COLORS[i % 4], anchor=tkinter.SW)
                print('rank<1000 but next>1000')

    # create text for year, after the for loop, finish with the final text
        if next_year_rank > 1000:
            canvas.create_text(GRAPH_MARGIN_SIZE + TEXT_DX + (j+1) * x_dis, y_minimum,
                               text=name + '*', fill=COLORS[i % 4], anchor=tkinter.SW)
        else:
            name_str = ""
            name_str = str(name) + str(next_year_rank)
            canvas.create_text(GRAPH_MARGIN_SIZE + TEXT_DX + (j+1) * x_dis, GRAPH_MARGIN_SIZE + next_year_rank * y_dis,
                               text=name_str, fill=COLORS[i % 4], anchor=tkinter.SW)


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
