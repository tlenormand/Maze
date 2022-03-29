#!/usr/bin/python3

from tkinter import *


class WindowProperty(Canvas):
    def __init__(self):
        self._scale = 10
        self._margin_left = 10
        self._margin_right = 10
        self._margin_top = 60
        self._margin_bottom = 10
        self._window = Tk()
        self._width_window = self._window.winfo_screenwidth()
        self._height_window = self._window.winfo_screenheight()
        self._my_canvas = Canvas(
                            self._window,
                            width=self._width_window - (self._margin_left + self._margin_right),
                            height=self._height_window - (self._margin_top + self._margin_bottom),
                            bg='ivory',
                            borderwidth=0,
                            highlightthickness=0
                        )

    def update(self):
        super().update(self)
