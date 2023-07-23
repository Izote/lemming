from tkinter import Toplevel
from tkinter.ttk import Label
from .client import client


def check(obj, window):
    value = obj.get()
    table = "Root"
    response = client.table(table).select("ipa").execute()

    exists = value in [row["ipa"] for row in response.data]

    title = "Result"
    text = f"WARNING: '{value}' already exists in `{table}`." if exists \
        else f"GOOD NEWS: '{value}' does not exist in `{table}`."

    top = Toplevel(window)
    top.title(title)
    Label(top, text=text).pack()
