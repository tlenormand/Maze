#!/usr/bin/python3

from Models import Maze_class
import sys
sys.setrecursionlimit(10000)

# if direction != 3 and y < len(MZ) and MZ[y][x + 1] != -1:

def solve_square(MZ):
    """
    function that solve a maze while sorting it. It count all cases of the maze
        beggining by one escape

    Arguments:
        MZ: the maze to solve

    Returns:
        a maze sorted
    """
    way = 0
    x, y = Maze_class._start
    if x == 0 and MZ[y][x + 1] != -1:
        loop_way(MZ, way + 1, x + 1, y, 1)
    if x == (len(Maze_class._maze_dict["MZ_randomised"][0]) - 1) and MZ[y][x - 1] != -1:
        loop_way(MZ, way + 1, x - 1, y, 3)
    if y == 0 and MZ[y + 1][x] != -1:
        loop_way(MZ, way + 1, x, y + 1, 2)
    if y == (len(Maze_class._maze_dict["MZ_randomised"]) - 1) and MZ[y - 1][x] != -1:
        loop_way(MZ, way + 1, x, y - 1, 0)
    return MZ

def loop_way(MZ, way, x, y, direction):
    """
    recursive function that count all cases of the maze

    Arguments:
        MZ: the maze to solve
        way: the counter of cases which indicate the solution
        x: x coordonate in the maze
        y: y coordonate in the maze
        direction: the direction where checked the next case

    Returns:
        None
    """
    MZ[y][x] = way
    way += 1
    Maze_class._solver_list.append([x, y])
    if y < len(MZ) - 1 and y > 0:
        if direction != 2 and y > 0 and MZ[y - 1][x] != -1:
            loop_way(MZ, way, x, y - 1, 0)
        if direction != 3 and y < len(MZ) and x < len(MZ[0]) - 1 and MZ[y][x + 1] != -1:
            loop_way(MZ, way, x + 1, y, 1)
        if direction != 0 and x < len(MZ[0]) and MZ[y + 1][x] != -1:
            loop_way(MZ, way, x, y + 1, 2)
        if direction != 1 and x > 0 and MZ[y][x - 1] != -1:
            loop_way(MZ, way, x - 1, y, 3)
