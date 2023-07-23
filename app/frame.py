from tkinter.ttk import Frame


def frame(parent, loc, width, sticky="w"):
    f = Frame(master=parent)
    f.columnconfigure("all", weight=1)
    f.grid(column=loc[0], row=loc[1], columnspan=width, sticky=sticky)

    return f
