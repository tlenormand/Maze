#!/usr/bin/python3
import random
from maze import Maze
from maze import UserInput



def print_maze(MZ):
    for line in MZ:
        print(line)

def init_MZ(height_maze, width_maze):
    MZ = []
    for y in range(height_maze):
        MZ.append([])
        for x in range(width_maze):
            if y % 2 == 0 or x % 2 == 0:
                MZ[y].append(-1)
            else:
                MZ[y].append(0)   
    return MZ

def generate_number_maze(MZ, maze_class):
    new_MZ = MZ.copy()
    nb = 5
    for y in range(len(new_MZ)):
        for x in range(len(new_MZ[0])):
            if new_MZ[y][x] != -1:
                new_MZ[y][x] = nb
                nb += 1
    maze_class._max_number = nb + 1
    return new_MZ

def generate_random_maze(MZ, maze_class):
    iteration = 0
    while is_finish(MZ) == 1:
        maze_class._random_dict[iteration] = []
        list_coordonates = []
        generate_list_coordonates(MZ, list_coordonates)
        random.shuffle(list_coordonates)
        # try implement a step
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
            merge_cells(maze_class, iteration, MZ, direction, x, y, x_bis, y_bis)
        list_coordonates.clear()
        iteration += 1
    return MZ

def generate_list_coordonates(MZ, list_coordonates):
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
    nb = MZ[1][1]
    for row in MZ:
        for value in row:
            if value != nb and value != -1:
                return 1
    return 0

def merge_cells(maze_class, iteration, MZ, direction, x, y, x_bis, y_bis):
    if MZ[y][x] != MZ[y_bis][x_bis] and MZ[y_bis][x_bis] != -1:
        MZ[int((y + y_bis) / 2)][int((x + x_bis) / 2)] = MZ[y][x]
        replace_matches_in_maze(MZ, MZ[y][x], MZ[y_bis][x_bis])
        maze_class._random_dict[iteration].append([direction, x, y, x_bis, y_bis])

def replace_matches_in_maze(MZ, value, match):
    for y in range(len(MZ)):
        for x in range(len(MZ[0])):
            if MZ[y][x] == value:
                MZ[y][x] = match

def generate_equal_number_maze(MZ, nb):
    match = MZ[1][1]
    for y in range(len(MZ)):
        for x in range(len(MZ[0])):
            if MZ[y][x] == match:
                MZ[y][x] = nb
    return MZ

def create_escape_maze(MZ, maze_class):
    MZ[1][0] = Maze._max_number + 1
    MZ[len(MZ) - 1][len(MZ[0]) - 2] = 1
    return MZ
