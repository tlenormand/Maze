#!/usr/bin/python3

from time import sleep


def class_square(MZ):
    """coordonate of the exit : MZ[len(MZ) - 1][len(MZ[0]) - 2]"""
    way = 1
    y = len(MZ) - 1
    x = len(MZ[0]) - 2
    direction = 0
    loop_way(MZ, way + 1, x, y - 1, direction)

def loop_way(MZ, way, x, y, direction):
    if MZ[y][x] != -1:
        MZ[y][x] = way
        way += 1
        if y < len(MZ) - 1 and y > 0:
            if direction != 2 and y > 0:
                loop_way(MZ, way, x, y - 1, 0)
            if direction != 3 and y < len(MZ):
                loop_way(MZ, way, x + 1, y, 1)
            if direction != 0 and x < len(MZ[0]):
                loop_way(MZ, way, x, y + 1, 2)
            if direction != 1 and x > 0:
                loop_way(MZ, way, x - 1, y, 3)
