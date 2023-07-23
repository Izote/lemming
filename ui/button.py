from tkinter.ttk import Button, Label


def button(parent, label, loc, width, entry=None, sticky="nsew"):
    if entry is not None:
        b = Button(
            master=parent,
            text=label,
            width=width,
            command=lambda: entry.insert("end", label)
        )
    else:
        b = Button(
            master=parent,
            text=label,
            width=width
        )

    b.grid(column=loc[0], row=loc[1], sticky=sticky)

    return b
