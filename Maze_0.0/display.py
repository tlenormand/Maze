#!/usr/bin/python3
from tkinter import *


def display_maze(MZ):
    fenetre = Tk()

    # width = fenetre.winfo_screenwidth()
    # height = fenetre.winfo_screenheight()
    # print(width)
    # print(height)

    widht_fenetre = len(MZ) * 10 + 40
    height_fenetre = len(MZ) * 10 + 40
    str_fenetre = f"{widht_fenetre}x{height_fenetre}"

    fenetre.geometry(str_fenetre)

    monCanvas = Canvas(fenetre, width=widht_fenetre, height=height_fenetre, bg='ivory', borderwidth=0, highlightthickness=0)
    monCanvas.place(x=20,y=20)

    # color the squares of the maze
    for y in range(len(MZ)):
        for x in range(len(MZ)):
            if MZ[x][y] == 1:
                monCanvas.create_rectangle(x * 10, y * 10, (x + 1) * 10, (y + 1) * 10, fill="black")
            else:
                monCanvas.create_rectangle(x * 10, y * 10, (x + 1) * 10, (y + 1) * 10, fill="white")

    fenetre.mainloop()
