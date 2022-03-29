#!/usr/bin/python3
from Models import *
from Models.MazeGenerator.maze_utils import *
from Models.MazeDisplay.colors import *
from tkinter import *
from time import sleep
import copy


def show_maze(key):
    """
    function that check what type of display we should use

    Arguments:
        key: an index in a maze dictionnary

    Return:
        None
    """
    WindowProperty_class._my_canvas.delete("all")
    if key == "MZ_randomised" and UserInput_class._show_display == 1:
        display_maze("MZ_numerised")
        display_maze_randomisation()
    elif key == "MZ_sorted" and UserInput_class._show_display == 1:
        display_maze("MZ_escaped")
        display_maze_solver()
    else:
        display_maze(key)


def display_maze(key):
    """
    function that display a maze at index "key" in a maze dictionnary

    Arguments:
        key: an index in a maze dictionnary

    Return:
        None
    """
    scale = WindowProperty_class._scale  # 10px using to draw the maze
    margin_LR = WindowProperty_class._margin_left + WindowProperty_class._margin_right
    margin_TB = WindowProperty_class._margin_top + WindowProperty_class._margin_bottom

    height_maze = len(Maze_class._maze_dict[key])
    width_maze = len(Maze_class._maze_dict[key][0])
    height_window = WindowProperty_class._height_window
    width_window = WindowProperty_class._width_window
    while height_maze * scale > height_window - margin_TB or width_maze * scale > width_window - margin_LR:
        scale -= 1
    WindowProperty_class._scale = scale

    str_fenetre = f"{width_window}x{height_window}"
    WindowProperty_class._window.geometry(str_fenetre)

    # color the squares of the maze
    # black for walls and other for the maze
    for y in range(len(Maze_class._maze_dict[key])):
        for x in range(len(Maze_class._maze_dict[key][0])):
            if Maze_class._maze_dict[key][y][x] == -1:
                WindowProperty_class._my_canvas.create_rectangle(
                    x * scale, y * scale,
                    (x + 1) * scale,
                    (y + 1) * scale,
                    fill="black",
                    outline=""
                )
            else:
                WindowProperty_class._my_canvas.create_rectangle(
                    x * scale, y * scale,
                    (x + 1) * scale,
                    (y + 1) * scale,
                    fill=sub_to_hexa(key, Maze_class._maze_dict[key][y][x]),
                    outline=""
                )
            if UserInput_class._show_display == 1:
                WindowProperty_class._my_canvas.update()
                sleep(UserInput_class._waiting_time)


def display_maze_randomisation():
    """
    function that display the maze randomised step by step
        when checkbox display is activated

    Arguments:
        None

    Return:
        None
    """
    previous = copy.deepcopy(Maze_class._maze_dict["MZ_numerised"])
    for key, value in Maze_class._random_dict.items():
        for coordonates in value:
            merge_cells_canvas_update(
                previous,        # MZ
                coordonates[3],  # x
                coordonates[4],  # y
                coordonates[1],  # x_bis
                coordonates[2]   # y_bis
            )
            WindowProperty_class._my_canvas.update()
            sleep(UserInput_class._waiting_time)


def merge_cells_canvas_update(MZ, x, y, x_bis, y_bis):
    """
    function that check if MZ[y][x] and MZ[y_bis][x_bis] contain the same value

    Arguments:
        MZ: the maze where values are compared
        x: current x position in the maze
        y: current y position in the maze
        x_bis: next x position in the maze
        y_bis: ext y position in the maze

    Return:
        None
    """
    if MZ[y][x] != MZ[y_bis][x_bis] and MZ[y_bis][x_bis] != -1:
        MZ[int((y + y_bis) / 2)][int((x + x_bis) / 2)] = MZ[y][x]
        delete_canvas_rectangle(MZ, MZ[y_bis][x_bis])
        replace_matches_in_maze_canvas_update(MZ, MZ[y][x], MZ[y_bis][x_bis])


def delete_canvas_rectangle(MZ, match):
    """
    function that delete canvas rectangle previousily created. It allow to be
        more efficient during creation of new merged rectangle

    Arguments:
        MZ: the maze where match are compared
        match: value we refer to to delete canvas rectangle

    Return:
        None
    """
    for y in range(len(MZ)):
        for x in range(len(MZ[0])):
            if MZ[y][x] == match:
                WindowProperty_class._my_canvas.delete(f"y{y}x{x}")


def replace_matches_in_maze_canvas_update(MZ, value, match):
    """
    function that replace all value that match with "match" in the maze

    Arguments:
        MZ: maze where "value" are replaced
        value: values replaced by "match"
        match: value used to replace all "value"

    Return:
        None
    """
    for y in range(len(MZ)):
        for x in range(len(MZ[0])):
            if MZ[y][x] == value or MZ[y][x] == match:
                MZ[y][x] = match
                WindowProperty_class._my_canvas.create_rectangle(
                    x * WindowProperty_class._scale,
                    y * WindowProperty_class._scale,
                    (x + 1) * WindowProperty_class._scale,
                    (y + 1) * WindowProperty_class._scale,
                    fill=sub_to_hexa("MZ_numerised", MZ[y][x]),
                    outline="",
                    tags=f"y{y}x{x}"
                )


def display_maze_solver():
    """
    function that display the sorted maze step by step
        when checkbox display is activated

    Arguments:
        None

    Return:
        None
    """
    scale = WindowProperty_class._scale
    for idx in Maze._solver_list:
        WindowProperty_class._my_canvas.create_rectangle(
            idx[0] * scale, idx[1] * scale,
            (idx[0] + 1) * scale,
            (idx[1] + 1) * scale,
            fill=sub_to_hexa("MZ_sorted", Maze_class._maze_dict["MZ_sorted"][idx[1]][idx[0]]),
            outline=""
        )
        WindowProperty_class._my_canvas.update()
        sleep(UserInput_class._waiting_time)


def draw_solution():
    """
    function that draw the solution of the maze

    Arguments:
        None

    Return:
        None
    """
    x = Maze_class._stop[0]
    y = Maze_class._stop[1]
    MZ_sorted = copy.deepcopy(Maze_class._maze_dict["MZ_sorted"])
    while MZ_sorted[y][x] >= 0:
        WindowProperty_class._my_canvas.delete(f"y{y}x{x}")
        WindowProperty_class._my_canvas.create_rectangle(
            x * WindowProperty_class._scale,
            y * WindowProperty_class._scale,
            (x + 1) * WindowProperty_class._scale,
            (y + 1) * WindowProperty_class._scale,
            fill="yellow",
            outline=""
        )
        if MZ_sorted[y - 1][x] == MZ_sorted[y][x] - 1:
            y -= 1
        elif MZ_sorted[y + 1][x] == MZ_sorted[y][x] - 1:
            y += 1
        elif MZ_sorted[y][x - 1] == MZ_sorted[y][x] - 1:
            x -= 1
        elif MZ_sorted[y][x + 1] == MZ_sorted[y][x] - 1:
            x += 1
        sleep(UserInput_class._waiting_time)
        WindowProperty_class._my_canvas.update()
