#!/usr/bin/python3
from tkinter import *
# from tkinter.ttk import *
from time import sleep


def bar(window, progress, value):
    progress['value'] = value
    window.update_idletasks()

def display_maze(MZ):
    scale = 10  # 10px using to draw the maze
    margin = 20  # 20px using for margin
    window = Tk()

    # progress = Progressbar(window, orient = HORIZONTAL, length = 100, mode = 'determinate')
    # progress.pack(pady = 10)
    # Button(window, text = 'Start', command = bar).pack(pady = 10)

    height_maze = len(MZ[0])
    width_maze = len(MZ)
    height_window = window.winfo_screenheight()
    width_window = window.winfo_screenwidth()
    while height_maze * scale > height_window - margin or width_maze * scale > width_window - margin:
        scale -= 1

    str_fenetre = f"{width_window}x{height_window}"

    window.geometry(str_fenetre)

    myCanvas = Canvas(window, width=width_window - margin, height=height_window - margin, bg='ivory', borderwidth=0, highlightthickness=0)
    myCanvas.place(x=20,y=20)

    # color the squares of the maze
    for y in range(len(MZ)):
        for x in range(len(MZ[0])):
            if MZ[y][x] == -1:
                myCanvas.create_rectangle(x * scale, y * scale, (x + 1) * scale, (y + 1) * scale, fill="black")
            else:
                myCanvas.create_rectangle(x * scale, y * scale, (x + 1) * scale, (y + 1) * scale, fill="white")
        # bar(window, progress, y / len(MZ[0]))

    window.mainloop()
