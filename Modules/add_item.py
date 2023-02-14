from tkinter import *

import pyperclip

from main import listbox_inprogress


def add_item():
    item = pyperclip.paste()
    listbox_inprogress.insert(END, item)
