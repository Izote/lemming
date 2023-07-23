from tkinter import Text
from tkinter.ttk import Entry


def text_input(parent, loc, width, lines=1):
    if not lines >= 1:
        raise ValueError("`lines` attribute >= 1 is required.")

    if lines > 1:
        raise NotImplementedError("`lines` attribute > 1 not yet supported")

    x, y = loc
    e = Entry(master=parent)
    e.grid(column=x, row=y, columnspan=width, rowspan=lines, sticky="w")

    return e
