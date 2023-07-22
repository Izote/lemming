from tkinter.ttk import Frame


def create_tab(parent, label):
    tab = Frame(parent)
    tab.columnconfigure([0, 1, 2, 3, 4, 5, 6], minsize=1)
    tab.rowconfigure([0, 1, 2, 3], minsize=1)
    parent.add(tab, text=label)
    parent.pack()

    return tab
