#!/usr/bin/python3


def find_max(MZ):
    """
    function that find the max value in a maze

    Arguments:
        MZ: the maze
    
    Returns:
        the max value found
    """
    max = 0
    for y in range(len(MZ)):
        for x in range(len(MZ[0])):
            if MZ[y][x] > max:
                max = MZ[y][x]
    return max
