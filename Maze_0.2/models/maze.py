#!/usr/bin/python3
from msilib import RadioButtonGroup
from textwrap import indent
from turtle import left, position, xcor
from check_input import check_input
from maze_generator import *
from maze_solver import *
from tkinter import *
from functools import partial
from time import sleep
import copy
import maze
from color import generate_gradient_rgbs


class Window_property():
    _scale = 0

class MyCanvas():
    _my_canvas = 0

class Maze():
    _maze_dict = {}
    _random_dict = {}
    _rgb_list = []
    _max_number = 0
    _max_solved = 0

class UserInput():
    _show_display = 0
    _displaying_time = 0
    _waiting_time = 0

    def update_show_display(self, displaying_time):
        self._show_display = cb_show_display.get()
        self._displaying_time = int(displaying_time.get())
        self._waiting_time = float(userinput._displaying_time / float(len(Maze._maze_dict["MZ_init"]) * len(Maze._maze_dict["MZ_init"][0])))


def find_max(MZ):
    max = 0
    for y in range(len(MZ)):
        for x in range(len(MZ[0])):
            if MZ[y][x] > max:
                max = MZ[y][x]
    return max

def sub_to_hexa(MZ, rgb_idx):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    if Maze._rgb_list == []:
        Maze._rgb_list = generate_gradient_rgbs(Maze._max_number + 1)
    r, g, b = Maze._rgb_list[rgb_idx]
    hexa_color = "#{:02x}{:02x}{:02x}".format(r, g, b)

    return hexa_color

def display_maze(MZ):
    Window_property._scale = 10  # 10px using to draw the maze
    margin = 20  # 20px using for margin
    Maze._max_number = find_max(MZ)
    # progress = Progressbar(window, orient = HORIZONTAL, length = 100, mode = 'determinate')
    # progress.pack(pady = 10)
    # Button(window, text = 'Start', command = bar).pack(pady = 10)

    padding_height = 50
    padding_width = 10
    height_maze = len(MZ[0])
    width_maze = len(MZ)
    height_window = window.winfo_screenheight()
    width_window = window.winfo_screenwidth()
    while height_maze * Window_property._scale - padding_width > height_window - margin or width_maze * Window_property._scale - padding_height > width_window - margin:
        Window_property._scale -= 1

    MyCanvas._my_canvas = Canvas(window, width=width_window - margin, height=height_window - margin, bg='ivory', borderwidth=0, highlightthickness=0)
    MyCanvas._my_canvas.place(x=padding_width, y=padding_height)

    # color the squares of the maze
    for y in range(len(MZ)):
        for x in range(len(MZ[0])):
            if MZ[y][x] == -1:
                MyCanvas._my_canvas.create_rectangle(x * Window_property._scale, y * Window_property._scale, (x + 1) * Window_property._scale, (y + 1) * Window_property._scale, fill="black", outline="")
            else:
                MyCanvas._my_canvas.create_rectangle(x * Window_property._scale, y * Window_property._scale, (x + 1) * Window_property._scale, (y + 1) * Window_property._scale, fill=sub_to_hexa(MZ, MZ[y][x]), outline="")
            if userinput._show_display == 1:
                MyCanvas._my_canvas.update()
                sleep(userinput._waiting_time)

def display_maze_randomisation():
    previous = copy.deepcopy(Maze._maze_dict["MZ_numerised"])
    # myCanvas = display_maze(previous)
    for key, value in Maze._random_dict.items():
        for coordonates in value:
            x = coordonates[1]
            y = coordonates[2]
            x_bis = coordonates[3]
            y_bis = coordonates[4]
            merge_cells_canvas_update(previous, x_bis, y_bis, x, y)
            MyCanvas._my_canvas.update()
            sleep(userinput._waiting_time * 10)

def merge_cells_canvas_update(MZ, x, y, x_bis, y_bis):
    if MZ[y][x] != MZ[y_bis][x_bis] and MZ[y_bis][x_bis] != -1:
        MZ[int((y + y_bis) / 2)][int((x + x_bis) / 2)] = MZ[y][x]
        replace_matches_in_maze_canvas_update(MZ, MZ[y][x], MZ[y_bis][x_bis])

def replace_matches_in_maze_canvas_update(MZ, value, match):
    for y in range(len(MZ)):
        for x in range(len(MZ[0])):
            if MZ[y][x] == value:
                MZ[y][x] = match
                MyCanvas._my_canvas.create_rectangle(x * Window_property._scale, y * Window_property._scale, (x + 1) * Window_property._scale, (y + 1) * Window_property._scale, fill=sub_to_hexa(16777215, MZ[y][x]), outline="")

def draw_solution():
    x = 0
    y = 1
    MZ_sorted = copy.deepcopy(Maze._maze_dict["MZ_sorted"])
    while MZ_sorted[y][x] > 1:
        if MZ_sorted[y - 1][x] == MZ_sorted[y][x] - 1:
            y -= 1
        if MZ_sorted[y + 1][x] == MZ_sorted[y][x] - 1:
            y += 1
        if MZ_sorted[y][x - 1] == MZ_sorted[y][x] - 1:
            x -= 1
        if MZ_sorted[y][x + 1] == MZ_sorted[y][x] - 1:
            x += 1
        MyCanvas._my_canvas.create_rectangle(x * Window_property._scale, y * Window_property._scale, (x + 1) * Window_property._scale, (y + 1) * Window_property._scale, fill="green", outline="")
        sleep(0.005)
        MyCanvas._my_canvas.update()

def show_maze(key):
    if key == "MZ_randomised" and userinput._show_display == 1:
        display_maze_randomisation()
    else:
        display_maze(Maze._maze_dict[key])

def generate_maze(height_maze, width_maze):
    height_maze = check_input(height_maze.get())
    if height_maze < 0:
        return height_maze
    width_maze = check_input(width_maze.get())
    if width_maze < 0:
        return width_maze
    if Maze._max_number > 0:
        Maze._max_number = 0
        Maze._rgb_list = []

    maze_dict = {}

    MZ_init = init_MZ(height_maze, width_maze)
    Maze._maze_dict["MZ_init"] = MZ_init

    MZ_numerised = generate_number_maze(copy.deepcopy(MZ_init), Maze)
    Maze._maze_dict["MZ_numerised"] = MZ_numerised

    MZ_randomised = generate_random_maze(copy.deepcopy(MZ_numerised), Maze)
    Maze._maze_dict["MZ_randomised"] = MZ_randomised

    MZ_escaped = create_escape_maze(copy.deepcopy(MZ_randomised), Maze)
    Maze._maze_dict["MZ_escaped"] = MZ_escaped

    MZ_equalised = generate_equal_number_maze(copy.deepcopy(MZ_escaped), 0)
    Maze._maze_dict["MZ_equalised"] = MZ_equalised

    MZ_sorted = solve_square(copy.deepcopy(MZ_equalised), Maze)
    Maze._maze_dict["MZ_sorted"] = MZ_sorted

    print(Maze._maze_dict)

    return maze_dict 

if __name__ == "__main__":
    userinput = UserInput()
    window = Tk()
    window.attributes("-fullscreen", True)
    # height_window = window.winfo_screenheight()
    # width_window = window.winfo_screenwidth()

    # Exit button
    Button(window, text="Exit", command=window.destroy).grid(column=99)

    # maze dimensions
    label_height = Label(window, text='height')
    text_height = StringVar()
    height_maze = Entry(window, textvariable=text_height)
    label_width = Label(window, text='width')
    text_width = StringVar()
    width_maze = Entry(window, textvariable=text_width)

    label_height.grid(column=0, row=0)
    height_maze.grid(column=1, row=0)
    label_width.grid(column=0, row=1)
    width_maze.grid(column=1, row=1)

    Button(window, text='generate', command=partial(generate_maze, height_maze, width_maze)).grid(column=2, row=0)

    # handle the maze displaying
    lb_time_display = Label(window, text='displaying time:').grid(column=4, row=0)
    text_time = IntVar()
    displaying_time = Entry(window, textvariable=text_time)
    displaying_time.grid(column=5, row=0)
    Label(window, text='seconds').grid(column=6, row=0)
    cb_show_display = IntVar()
    Checkbutton(window, text="show display", variable=cb_show_display, command=partial(userinput.update_show_display, displaying_time)).grid(column=3, row=0)

    # display initialisation of maze
    Button(window, text="show init", command=partial(show_maze, "MZ_init")).grid(column=3, row=1)

    # display numerisation of maze
    Button(window, text="show numerisation", command=partial(show_maze, "MZ_numerised")).grid(column=4, row=1)

    # display randomisation of maze
    Button(window, text="show randomisation", command=partial(show_maze, "MZ_randomised")).grid(column=5, row=1)

    # display start finish of maze
    Button(window, text="show escape", command=partial(show_maze, "MZ_escaped")).grid(column=6, row=1)

    # display white maze
    Button(window, text="show white", command=partial(show_maze, "MZ_equalised")).grid(column=7, row=1)

    # display sorted maze
    Button(window, text="show sorted", command=partial(show_maze, "MZ_sorted")).grid(column=8, row=1)

    # display solution maze
    Button(window, text="show solution", command=partial(draw_solution)).grid(column=9, row=1)

    window.mainloop()
