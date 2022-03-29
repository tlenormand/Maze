#!/usr/bin/python3
import random


def print_maze(MZ):
    for line in MZ:
        print(line)

def init_MZ(size):
    MZ = []
    for y in range(int(size)):
        MZ.append([])
        for x in range(int(size)):
            if y % 2 == 0 or x % 2 == 0:
                MZ[y].append(1)
            else:
                MZ[y].append(0)   
    return MZ 

def generate_number_maze(MZ):
    nb = 3
    for y in range(len(MZ)):
        for x in range(len(MZ)):
            if MZ[x][y] != 1:
                MZ[x][y] = nb
                nb += 1

def generate_random_maze(MZ):
    while is_finish(MZ) == 1:
        direction = random.randint(1, 4)
        if direction == 1:
            x = random.randrange(1, len(MZ))
            y = random.randrange(3, len(MZ))
        elif direction == 2:
            x = random.randrange(1, len(MZ) - 2)
            y = random.randrange(1, len(MZ))
        elif direction == 3:
            x = random.randrange(1, len(MZ))
            y = random.randrange(1, len(MZ) - 2)
        else:
            x = random.randrange(3, len(MZ))
            y = random.randrange(1, len(MZ))

        if MZ[x][y] != 1:
            randomize_maze(MZ, direction, x, y)

def is_finish(MZ):
    nb = MZ[1][1]
    for row in MZ:
        for value in row:
            if value != nb and value != 1:
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

    if MZ[x][y] != MZ[x_bis][y_bis] and MZ[x_bis][y_bis] != 1:
        MZ[int((x + x_bis) / 2)][int((y + y_bis) / 2)] = MZ[x][y]

        replace_matches_in_maze(MZ, MZ[x][y], MZ[x_bis][y_bis])

def replace_matches_in_maze(MZ, value, match):
    for x in range(len(MZ)):
        for y in range(len(MZ)):
            if MZ[x][y] == value:
                MZ[x][y] = match

def create_entry_exit_maze(MZ):
    MZ[0][1] = 98
    MZ[len(MZ) - 1][len(MZ) - 2] = 99
