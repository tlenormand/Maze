#!/usr/bin/python3


def check_input(value):
    try:
        value = int(value)
        if value < 1:
            print(f"you type \"{value}\": please enter a positive number")
            return -2

        if value % 2 == 0:
            value += 1

    except Exception:
        print(f"you type \"{value}\": please enter an integer number")
        return -1

    return value
