import tkinter as tk
from tkinter.ttk import Button, Entry, Frame, Label, Notebook
from .tab import create_tab


def ui():
    root = tk.Tk()
    root.title("lemming")

    tab_control = Notebook(root)
    root_tab = create_tab(tab_control, "Root")

    root_frame = Frame(master=root_tab)
    root_frame.grid(column=0, row=0)

    Label(master=root_frame, text="IPA").grid(column=0, row=0, columnspan=1)
    ipa_entry = Entry(master=root_frame)
    ipa_entry.grid(column=1, row=0, columnspan=6, sticky="ew")

    Label(master=root_frame, text="Insert").grid(column=0, row=1, columnspan=1)
    in_button1 = Button(master=root_frame, text="ʼ")
    in_button1.grid(column=1, row=1, columnspan=2)

    in_button2 = Button(master=root_frame, text="ʔ")
    in_button2.grid(column=3, row=1, columnspan=2)

    in_button3 = Button(master=root_frame, text="ː")
    in_button3.grid(column=5, row=1, columnspan=2)

    Label(master=root_frame, text="Gloss").grid(column=0, row=2, columnspan=1)
    gloss_entry = Entry(master=root_frame)
    gloss_entry.grid(column=1, row=2, columnspan=6, sticky="ew")

    db_button1 = Button(master=root_frame, text="Check")
    db_button1.grid(column=1, row=3, columnspan=2)

    db_button2 = Button(master=root_frame, text="Save")
    db_button2.grid(column=3, row=3, columnspan=2)

    db_button3 = Button(master=root_frame, text="Clear")
    db_button3.grid(column=5, row=3, columnspan=2)

    return root
