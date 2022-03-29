#!/usr/bin/python3

from time import sleep
import sys
sys.setrecursionlimit(10000)

def solve_square(MZ, maze_class):
    """coordonate of the exit : MZ[len(MZ) - 1][len(MZ[0]) - 2]"""
    way = 1
    y = len(MZ) - 1
    x = len(MZ[0]) - 2
    direction = 0
    loop_way(MZ, way + 1, x, y - 1, direction, maze_class)
    return MZ

def loop_way(MZ, way, x, y, direction, maze_class):
        MZ[y][x] = way
        way += 1
        if y < len(MZ) - 1 and y > 0:
            if direction != 2 and y > 0 and MZ[y - 1][x] != -1:
                if way > maze_class._max_solved:
                    maze_class._max_solved = way
                loop_way(MZ, way, x, y - 1, 0, maze_class)
            if direction != 3 and y < len(MZ) and MZ[y][x + 1] != -1:
                if way > maze_class._max_solved:
                    maze_class._max_solved = way
                loop_way(MZ, way, x + 1, y, 1, maze_class)
            if direction != 0 and x < len(MZ[0]) and MZ[y + 1][x] != -1:
                if way > maze_class._max_solved:
                    maze_class._max_solved = way
                loop_way(MZ, way, x, y + 1, 2, maze_class)
            if direction != 1 and x > 0 and MZ[y][x - 1] != -1:
                if way > maze_class._max_solved:
                    maze_class._max_solved = way
                loop_way(MZ, way, x - 1, y, 3, maze_class)

# def solve_square2(MZ):
#     way = 2
#     y = len(MZ) - 2
#     x = len(MZ[0]) - 2
#     MZ[y][x] = way
#     way += 1
#     while x - 1 > 0 or y - 1 > 0: