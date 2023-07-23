import tkinter as tk
from tkinter.ttk import Notebook
from .button import button
from .frame import frame
from .text_input import text_input
from .label import label
from .tab import tab


def app():
    ui = tk.Tk()
    ui.title("lemming")

    tab_control = Notebook(ui)
    root_tab = tab(tab_control, "Root")

    label(root_tab, "IPA", [0, 0])
    ipa_input = text_input(root_tab, [1, 0], 5, lines=1)

    frame1 = frame(root_tab, [0, 1], 4, "w")

    label(frame1, "Insert", [0, 0])
    button_str = ["ʼ", "ʔ", "ʃ", "ː"]
    for i in range(len(button_str)):
        button(frame1, button_str[i], [i + 1, 0], 2, [ipa_input, "insert"])

    label(root_tab, "Gloss", [0, 2])
    gloss_input = text_input(root_tab, [1, 2], 5, lines=1)

    frame2 = frame(root_tab, [0, 3], 4, "w")

    label(frame2, "Data", [0, 0])
    button_dict = {"Check": [1, 6, [ipa_input, "check"]],
                   "Save": [2, 4, [[ipa_input, gloss_input], "save_to_root"]],
                   "Clear": [3, 6, [[ipa_input, gloss_input], "clear"]]}

    for key in ["Check", "Save", "Clear"]:
        value = button_dict[key]
        button(frame2, key, [value[0], 0], value[1], value[2], window=ui)

    return ui
