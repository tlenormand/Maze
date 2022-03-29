#!/usr/bin/python3

import Models
from Models import *
from Models.MazeDisplay.display import *
from Models.MazeGenerator.maze_generator import *
from tkinter import *
from functools import partial


if __name__ == "__main__":
    WindowProperty_class._window.attributes("-fullscreen", True)
    WindowProperty_class._my_canvas.place(x=WindowProperty_class._margin_left,y=WindowProperty_class._margin_top)

    # Exit button
    Button(WindowProperty_class._window, text="Exit", command=WindowProperty_class._window.destroy).grid(column=99)

    # maze dimensions
    label_height = Label(WindowProperty_class._window, text='height')
    text_height = StringVar(WindowProperty_class._window)
    height_maze = Entry(WindowProperty_class._window, textvariable=text_height)
    label_width = Label(WindowProperty_class._window, text='width')
    text_width = StringVar(WindowProperty_class._window)
    width_maze = Entry(WindowProperty_class._window, textvariable=text_width)

    label_height.grid(column=0, row=0)
    height_maze.grid(column=1, row=0)
    label_width.grid(column=0, row=1)
    width_maze.grid(column=1, row=1)

    Button(WindowProperty_class._window, text='generate', command=partial(generate_maze, height_maze, width_maze)).grid(column=2, row=0)

    # handle the maze displaying
    lb_time_display = Label(WindowProperty_class._window, text='displaying time:', textvariable=0).grid(column=4, row=0)
    text_time = IntVar(WindowProperty_class._window)
    displaying_time = Entry(WindowProperty_class._window, textvariable=text_time)
    displaying_time.grid(column=5, row=0)
    Label(WindowProperty_class._window, text='seconds').grid(column=6, row=0)
    cb_show_display = IntVar(WindowProperty_class._window)
    Checkbutton(
        WindowProperty_class._window,
        text="show display",
        variable=cb_show_display,
        command=partial(
            UserInput_class.update_show_display,
            Maze_class,
            cb_show_display,
            displaying_time
        )
    ).grid(column=3, row=0)

    # display initialisation of maze
    Button(WindowProperty_class._window, text="show init", command=partial(show_maze, "MZ_init")).grid(column=3, row=1)

    # display numerisation of maze
    Button(WindowProperty_class._window, text="show numerisation", command=partial(show_maze, "MZ_numerised")).grid(column=4, row=1)

    # display randomisation of maze
    Button(WindowProperty_class._window, text="show randomisation", command=partial(show_maze, "MZ_randomised")).grid(column=5, row=1)

    # display start finish of maze
    Button(WindowProperty_class._window, text="show escape", command=partial(show_maze, "MZ_escaped")).grid(column=6, row=1)

    # display white maze
    Button(WindowProperty_class._window, text="show maze", command=partial(show_maze, "MZ_equalised")).grid(column=7, row=1)

    # display sorted maze
    Button(WindowProperty_class._window, text="show sorted", command=partial(show_maze, "MZ_sorted")).grid(column=8, row=1)

    # display solution maze
    Button(WindowProperty_class._window, text="draw solution", command=partial(draw_solution)).grid(column=9, row=1)

    WindowProperty_class._window.mainloop()
