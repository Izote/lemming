import tkinter as tk
from tkinter.ttk import Notebook
from .button import button
from .frame import frame
from .text_input import text_input
from .label import label
from .tab import tab


def ui():
    root = tk.Tk()
    root.title("lemming")
    root.geometry("160x240")

    tab_control = Notebook(root)
    root_tab = tab(tab_control, "Root")

    label(root_tab, "IPA", [0, 0])
    ipa_input = text_input(root_tab, [1, 0], 5, lines=1)

    frame1 = frame(root_tab, [0, 1], 4, "w")

    label(frame1, "Insert", [0, 0])
    button_str = ["ʼ", "ʔ", "ː"]
    for i in range(3):
        button(frame1, button_str[i], [i + 1, 0], 2, entry=ipa_input)

    label(root_tab, "Gloss", [0, 2])
    gloss_input = text_input(root_tab, [1, 2], 5, lines=1)

    frame2 = frame(root_tab, [0, 3], 4, "w")

    label(frame2, "Data", [0, 0])
    button_dict = {"Check": [1, 6],
                   "Save": [2, 4],
                   "Clear": [3, 6]}

    for key in ["Check", "Save", "Clear"]:
        value = button_dict[key]
        button(frame2, key, [value[0], 0], value[1])

    return root
