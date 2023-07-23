from tkinter.ttk import Button, Label
from data.check import check
from data.clear import clear
from data.save import save


def button(parent, label, loc, width, target=None, window=None, sticky="nsew"):
    b = Button(master=parent, text=label, width=width)

    if isinstance(target, list) and target[1] == "insert":
        b.configure(command=lambda: target[0].insert("end", label))
    elif isinstance(target, list) and target[1] == "check":
        b.configure(command=lambda: check(target[0], window))
    elif isinstance(target, list) and target[1] == "clear":
        b.configure(command=lambda: clear(target[0]))
    elif isinstance(target, list) and target[1] == "save_to_root":
        b.configure(command=lambda: save(target, "Root"))
    else:
        pass

    b.grid(column=loc[0], row=loc[1], sticky=sticky)

    return b
