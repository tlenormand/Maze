#!/usr/bin/env

from tkinter import *
from tkinter import ttk


class ProgressBar(Canvas):
    def __init__(self):
        self.progress_window = Tk()
        self.progress_window.title('Generation')
        self.progress_var=ttk.Progressbar(self.progress_window,orient=HORIZONTAL,length=400,mode='determinate')
        self.labeltask = Label(self.progress_window, text="initialisation")
        self.progress_var.pack()
        self.labeltask.pack()
        self.progress_window.update()

    def increment(self, text_var, progress_var):
        self.progress_var['value'] += progress_var
        self.labeltask['text'] = text_var
        self.progress_window.update()
