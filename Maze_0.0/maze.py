#!/usr/bin/python3
from check_input import check_input
from maze_generator import *
from display import display_maze


if __name__ == "__main__":
    size = input("Enter size of the maze: ")
    size = check_input(size)

    MZ = init_MZ(size)
    print_maze(MZ)

    generate_number_maze(MZ)
    print("numberized:")
    print_maze(MZ)

    generate_random_maze(MZ)
    print("randomized:")
    print_maze(MZ)

    create_entry_exit_maze(MZ)
    display_maze(MZ)
