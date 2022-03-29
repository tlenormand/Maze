#!/usr/bin/python3
from check_input import check_input
from maze_generator import *
from maze_solver import *
from display import display_maze


if __name__ == "__main__":
    height_maze = input("Enter width of the maze: ")
    height_maze = check_input(height_maze)
    width_maze = input("Enter height of the maze: ")
    width_maze = check_input(width_maze)

    MZ = init_MZ(height_maze, width_maze)
    print_maze(MZ)

    generate_number_maze(MZ)
    print("numberized:")
    print_maze(MZ)

    generate_random_maze(MZ)
    print("randomized:")
    print_maze(MZ)

    print("entry + exit:")
    create_entry_exit_maze(MZ)
    print_maze(MZ)

    print("Equalized:")
    generate_equal_number_maze(MZ, 0)
    print_maze(MZ)

    print("classed:")
    class_square(MZ)
    print_maze(MZ)

    display_maze(MZ)
