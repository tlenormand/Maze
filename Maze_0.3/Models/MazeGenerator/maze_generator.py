#!/usr/bin/python3
import random
import copy
from tkinter import *
from Models import *
from Models.MazeSolver.maze_solver import *
from Models.MazeGenerator.maze_utils import *
from Models.MazeDisplay.colors import *
from Models.Storage.Progressbar import *
import time


def print_maze(MZ):
    """
    function that print a maze

    Arguments:
        MZ: the maze to print

    Returns:
        None
    """
    for line in MZ:
        print(line)

def init_MZ(height_maze, width_maze):
    """
    function that initialise a maze

    Arguments:
        height_maze: the height of the maze to init
        width_maze: the width of the maze to init

    Returns:
        the maze initialised
    """
    MZ = []
    for y in range(height_maze):
        MZ.append([])
        for x in range(width_maze):
            if y % 2 == 0 or x % 2 == 0:
                MZ[y].append(-1)
            else:
                MZ[y].append(0)   
    return MZ

def generate_number_maze(MZ):
    """
    function that numerise a maze while adding different number
        for each box of the maze

    Arguments:
        MZ: the maze to numerised

    Returns:
        the maze numerised
    """
    new_MZ = MZ.copy()
    nb = 5
    for y in range(len(new_MZ)):
        for x in range(len(new_MZ[0])):
            if new_MZ[y][x] != -1:
                new_MZ[y][x] = nb
                nb += 1
    Maze_class._max_number = nb + 1
    return new_MZ

def generate_random_maze(MZ):
    """
    function that randomise a maze and create a random maze

    Arguments:
        MZ: the maze to randomised

    Returns:
        the maze randomised
    """
    iteration = 0
    while is_finish(MZ) == 1:
        Maze_class._random_dict[iteration] = []
        list_coordonates = []
        generate_list_coordonates(MZ, list_coordonates)
        random.shuffle(list_coordonates)
        # try implement a step, can reduce time ?
        for y, x in list_coordonates:
            direction = random.randint(1, 4)
            if direction == 1:
                if y - 2 < 0:
                    y += 2
                y_bis = y - 2
                x_bis = x
            elif direction == 2:
                if x + 2 > len(MZ[0]) - 1:
                    x -= 2
                x_bis = x + 2
                y_bis = y
            elif direction == 3:
                if y + 2 > len(MZ) - 1:
                    y -= 2
                y_bis = y + 2
                x_bis = x
            else:
                if x - 2 < 0:
                    x += 2
                x_bis = x - 2
                y_bis = y
            merge_cells(iteration, MZ, direction, x, y, x_bis, y_bis)
        list_coordonates.clear()
        iteration += 1
    return MZ

def generate_list_coordonates(MZ, list_coordonates):
    """
    function that generate a list of coordonates for each box of the maze

    Arguments:
        MZ: the maze
        list_coordonates: a list of coordonates from the maze

    Returns:
        the list of coordonates
    """
    index = 0
    for y in range(len(MZ)):
        for x in range(len(MZ[0])):
            if MZ[y][x] != -1 and x % 2 == 1 and y % 2 == 1:
                list_coordonates.append([])
                list_coordonates[index].append(y)
                list_coordonates[index].append(x)
                index += 1
    return list_coordonates

def is_finish(MZ):
    """
    function that check if each boxe of the maze is the same. If one box is different
        then the maze isn't generate entierely

    Arguments:
        MZ: the maze to check

    Returns:
        0 if each box are the same
        1 otherwise
    """
    nb = MZ[1][1]
    for row in MZ:
        for value in row:
            if value != nb and value != -1:
                return 1
    return 0

def merge_cells(iteration, MZ, direction, x, y, x_bis, y_bis):
    """
    function that merge two boxes if thez are differents and merge the wall between them

    Arguments:
        iteration: number of iteration previously did in order to separate each iteration in the dict
        MZ: the maze to merge boxes
        direction: the direction where e want to control the next box
        x: x coordonate of the curent position in the maze
        y: y coordonate of the curent position in the maze
        x_bis: x coordonate where we want to check
        y_bis: y coordonate where we want to check

    Returns:
        None
    """
    if MZ[y][x] != MZ[y_bis][x_bis] and MZ[y_bis][x_bis] != -1:
        MZ[int((y + y_bis) / 2)][int((x + x_bis) / 2)] = MZ[y][x]
        replace_matches_in_maze(MZ, MZ[y][x], MZ[y_bis][x_bis])
        Maze_class._random_dict[iteration].append([direction, x, y, x_bis, y_bis])

# def replace_matches_in_maze(MZ, x, y, value):
#     if x > 0 and MZ[y][x - 1] != value:
#         MZ[y][x - 1] == value
#         replace_matches_in_maze(MZ, x - 1, y, value)
#     if y > 0 and MZ[y - 1][x] != value:
#         MZ[y - 1][x] == value
#         replace_matches_in_maze(MZ, x, y - 1, value)
#     if x < len(MZ[0]) - 1 and MZ[y][x + 1] != value:
#         MZ[y][x + 1] == value
#         replace_matches_in_maze(MZ, x + 1, y, value)
#     if y < len(MZ) - 1 and MZ[y + 1][x] != value:
#         MZ[y + 1][x] == value
#         replace_matches_in_maze(MZ, x, y + 1, value)

def replace_matches_in_maze(MZ, value, match):
    """
    function that replace all matching value in the maze

    Arguments:
        MZ: the maze we want to replace values
        value: the value we want to replace
        match: the value we want to put

    Returns:
        None
    """
    for y in range(len(MZ)):
        for x in range(len(MZ[0])):
            if MZ[y][x] == value:
                MZ[y][x] = match

def generate_equal_number_maze(MZ, nb):
    """
    function that replace all value in the maze by a number

    Arguments:
        MZ: the maze we want to replace values
        nb: the number we want to put in all boxes in the maze

    Returns:
        the new maze
    """
    match = MZ[1][1]
    for y in range(len(MZ)):
        for x in range(len(MZ[0])):
            if MZ[y][x] == match:
                MZ[y][x] = nb
    return MZ

def create_escape_maze(MZ):
    """
    function that create entry and exit in the maze

    Arguments:
        MZ: the maze we want to create entry/exit

    Returns:
        the new maze
    """
    x, y = new_escape(MZ)
    Maze_class._start = [x, y]
    MZ[y][x] = 0

    x, y = new_escape(MZ)
    Maze_class._stop = [x, y]
    MZ[y][x] = 0

    return (MZ)


def new_escape(MZ):
    """
    function that check if coordonates are valids entry point in the maze

    Arguments:
        MZ: the maze we want to create an entry

    Returns:
        the valids coordonates x, y
    """
    while True:
        x, y = random_escape()
        if x == 0 and MZ[y][x + 1] != -1:
            return (x, y)
        if x == (len(Maze_class._maze_dict["MZ_randomised"][0]) - 1) and MZ[y][x - 1] != -1:
            return (x, y)
        if y == 0 and MZ[y + 1][x] != -1:
            return (x, y)
        if y == (len(Maze_class._maze_dict["MZ_randomised"]) - 1) and MZ[y - 1][x] != -1:
            return (x, y)

def random_escape():
    """
    function that generate random coordonates for an entry in the maze

    Returns:
        random coordonates x, y
    """
    side = random.randint(1, 4)
    if side % 2 == 1:  # left or right
        y = random.randint(1, len(Maze_class._maze_dict["MZ_randomised"]) - 2)
        if side == 1:
            x = 0
        else:
            x = len(Maze_class._maze_dict["MZ_randomised"][0]) - 1
    else:
        x = random.randint(1, len(Maze_class._maze_dict["MZ_randomised"][0]) - 2)
        if side == 2:
            y = 0
        else:
            y = len(Maze_class._maze_dict["MZ_randomised"]) - 1

    return (x, y)

def reset_maze():
    """
    function that reset the Maze class

    Returns:
        None
    """
    Maze._maze_dict = {}
    Maze._maze_max_number = {}
    Maze._maze_rgb_dict = {}
    Maze._random_dict = {}
    Maze._solver_list = []
    Maze._start = []
    Maze._stop = []

def generate_maze(height_maze, width_maze):
    """
    main function used to generate a maze step by step

    Arguments:
        height_maze: height of the maze we want to create
        width_maze: width of the maze we want to create

    Returns:
        None
    """
    height_maze = UserInput_class.check_input(height_maze.get())
    if height_maze < 0:
        return height_maze
    width_maze = UserInput_class.check_input(width_maze.get())
    if width_maze < 0:
        return width_maze

    reset_maze()
    progress = ProgressBar()
    previous = time.time()

    MZ_init = init_MZ(height_maze, width_maze)
    Maze_class._maze_dict["MZ_init"] = MZ_init
    Maze_class._maze_max_number["MZ_init"] = find_max(MZ_init)
    Maze_class._maze_rgb_dict["MZ_init"] = generate_gradient_rgbs(Maze_class._maze_max_number["MZ_init"])
    print(f"time execution for Initialisation: {time.time() - previous} seconds")
    previous = time.time()
    progress.increment("Numerisation", 20)

    MZ_numerised = generate_number_maze(copy.deepcopy(MZ_init))
    Maze_class._maze_dict["MZ_numerised"] = MZ_numerised
    Maze_class._maze_max_number["MZ_numerised"] = find_max(MZ_numerised)
    Maze_class._maze_rgb_dict["MZ_numerised"] = generate_gradient_rgbs(Maze_class._maze_max_number["MZ_numerised"] + 1)
    print(f"time execution for Numerisation: {time.time() - previous} seconds")
    previous = time.time()
    progress.increment("Randomisation", 20)

    MZ_randomised = generate_random_maze(copy.deepcopy(MZ_numerised))
    Maze_class._maze_dict["MZ_randomised"] = MZ_randomised
    Maze_class._maze_max_number["MZ_randomised"] = find_max(MZ_randomised)
    Maze_class._maze_rgb_dict["MZ_randomised"] = generate_gradient_rgbs(Maze_class._maze_max_number["MZ_randomised"] + 1)
    print(f"time execution for Randomisation: {time.time() - previous} seconds")
    previous = time.time()
    progress.increment("Create entry, exit", 20)

    MZ_escaped = create_escape_maze(copy.deepcopy(MZ_randomised))
    Maze_class._maze_dict["MZ_escaped"] = MZ_escaped
    Maze_class._maze_max_number["MZ_escaped"] = find_max(MZ_escaped)
    Maze_class._maze_rgb_dict["MZ_escaped"] = generate_gradient_rgbs(Maze_class._maze_max_number["MZ_escaped"] + 1)
    print(f"time execution to create entry, exit: {time.time() - previous} seconds")
    previous = time.time()
    progress.increment("Equalisation", 20)

    MZ_equalised = generate_equal_number_maze(copy.deepcopy(MZ_escaped), 0)
    Maze_class._maze_dict["MZ_equalised"] = MZ_equalised
    Maze_class._maze_max_number["MZ_equalised"] = find_max(MZ_equalised)
    Maze_class._maze_rgb_dict["MZ_equalised"] = generate_gradient_rgbs(Maze_class._maze_max_number["MZ_equalised"] + 1)
    print(f"time execution for Equalisation: {time.time() - previous} seconds")
    previous = time.time()
    progress.increment("Solve maze", 20)

    MZ_sorted = solve_square(copy.deepcopy(MZ_equalised))
    Maze_class._maze_dict["MZ_sorted"] = MZ_sorted
    Maze_class._maze_max_number["MZ_sorted"] = find_max(MZ_sorted)
    Maze_class._maze_rgb_dict["MZ_sorted"] = generate_gradient_rgbs(Maze_class._maze_max_number["MZ_sorted"] + 1)
    print(f"time execution to Solve maze: {time.time() - previous} seconds")
    previous = time.time()
    progress.progress_window.destroy()

    for maze, dict in Maze_class._maze_dict.items():
        print(maze, dict, "\n")
