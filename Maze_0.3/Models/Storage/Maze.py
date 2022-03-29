#!/usr/bin/python3
"""Module the contain the Maze class"""


class Maze():
    """
    Maze class

    Attributes:
        _maze_dict (dict): contain all diferents mazes generated during the generation
        _maze_max_number (dict): contain all max numbers of mazes generated during the generation
        _maze_rgb_dict (dict): contain all rgb color codes of mazes generated during the generation
        _random_dict (dict): contain all the coordonates generated an checked during the randomisation of a maze
        _solver_list (list): contain all the way used to solve a maze
        _start (list): contain list of coordonate for the start
        _stop (list): contain list of coordonate for the end
    """
    _maze_dict = {}
    _maze_max_number = {}
    _maze_rgb_dict = {}
    _random_dict = {}
    _solver_list = []
    _start = []
    _stop = []
