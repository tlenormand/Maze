#!/usr/bin/python3
import random


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

def generate_number_maze(MZ):
    nb = 5
    for y in range(len(MZ)):
        for x in range(len(MZ[0])):
            if MZ[y][x] != -1:
                MZ[y][x] = nb
                nb += 1

def generate_random_maze(MZ):
    while is_finish(MZ) == 1:
        direction = random.randint(1, 4)
        if direction == 1:
            x = random.randrange(1, len(MZ[0]))
            y = random.randrange(3, len(MZ))
        elif direction == 2:
            x = random.randrange(1, len(MZ[0]) - 2)
            y = random.randrange(1, len(MZ))
        elif direction == 3:
            x = random.randrange(1, len(MZ[0]))
            y = random.randrange(1, len(MZ) - 2)
        else:
            x = random.randrange(3, len(MZ[0]))
            y = random.randrange(1, len(MZ))

        if MZ[y][x] != -1:
            randomize_maze(MZ, direction, x, y)

def is_finish(MZ):
    nb = MZ[1][1]
    for row in MZ:
        for value in row:
            if value != nb and value != -1:
                return 1
    return 0

def randomize_maze(MZ, direction, x, y):
    x_bis = x
    y_bis = y
    if direction == 1:
        y_bis -= 2
    elif direction == 2:
        x_bis += 2
    elif direction == 3:
        y_bis += 2
    else:
        x_bis -= 2

    if MZ[y][x] != MZ[y_bis][x_bis] and MZ[y_bis][x_bis] != -1:
        MZ[int((y + y_bis) / 2)][int((x + x_bis) / 2)] = MZ[y][x]

        replace_matches_in_maze(MZ, MZ[y][x], MZ[y_bis][x_bis])

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

def create_entry_exit_maze(MZ):
    MZ[0][1] = len(MZ) * len(MZ[0])
    MZ[len(MZ) - 1][len(MZ[0]) - 2] = 1
