from tkinter.ttk import Label


def label(parent, text, loc):
    Label(master=parent, text=text).\
        grid(column=loc[0], row=loc[1], sticky="nsw")
