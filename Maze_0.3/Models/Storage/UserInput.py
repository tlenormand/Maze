#!/usr/bin/python3

from Models import *

class UserInput():
    _show_display = 0
    _displaying_time = 0
    _waiting_time = 0

    def update_show_display(self, Maze_class, cb_show_display, displaying_time):
        self._show_display = cb_show_display.get()
        self._displaying_time = int(displaying_time.get())
        self._waiting_time = float(self._displaying_time / float(len(Maze_class._maze_dict["MZ_init"]) * len(Maze_class._maze_dict["MZ_init"][0])))

    def check_input(self, value):
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
