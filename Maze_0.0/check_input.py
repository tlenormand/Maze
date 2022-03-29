#!/usr/bin/python3


def check_input(value):
    try:
        value = int(value)
        if value % 2 == 0:
            value += 1
    except Exception:
        print(f"{value}: please enter an integer number")
        exit(-1)

    if value < 1:
        print(f"{value}: please enter a positive number")
        exit(-1)

    return value
