from tkinter import END


def clear(target):
    for t in target:
        t.delete(0, END)
