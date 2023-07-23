from tkinter.ttk import Frame


def tab(parent, label):
    t = Frame(parent)
    t.columnconfigure("all", weight=1)
    t.grid(column=0, row=0)

    parent.add(t, text=label)
    parent.pack()

    return t
