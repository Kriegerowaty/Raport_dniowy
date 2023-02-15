from tkinter import *
from tkinter import ttk
import pyperclip

from Modules import always_on_display
# from Modules import add_item


# def always_on_display():
#     if window.attributes("-topmost"):
#         window.attributes("-topmost", False)
#     else:
#         window.attributes("-topmost", True)


def add_item():
    item = pyperclip.paste()
    listbox_inprogress.insert(END, item)


def remove_item_recovered():
    listbox_recovered.delete(END)


def remove_item_inprogress():
    listbox_inprogress.delete(END)


def remove_item_recovery():
    listbox_recovery.delete(END)


def move_left():
    selection = listbox_inprogress.curselection()
    if selection:
        item = listbox_inprogress.get(selection)
        listbox_inprogress.delete(selection)
        listbox_recovered.insert(END, item)


def move_right():
    selection = listbox_inprogress.curselection()
    if selection:
        item = listbox_inprogress.get(selection)
        listbox_inprogress.delete(selection)
        listbox_recovery.insert(END, item)


def copy_elements_from_recovered_to_clipboard():
    items = [listbox_recovered.get(i) for i in range(listbox_recovered.size())]
    clip_text = " ".join(items)
    window.clipboard_append(clip_text)


def copy_elements_from_recovery_to_clipboard():
    items = [listbox_recovery.get(i) for i in range(listbox_recovery.size())]
    clip_text = " ".join(items)
    window.clipboard_append(clip_text)


window = Tk()
window.title(string='Raport dzienny')
window.iconbitmap('intel.ico')
window.resizable(width=False, height=False)

menu = Menu(window)
window.config(menu=menu)

options_menu = Menu(menu)
menu.add_cascade(label="Options", menu=options_menu)

aod_var = BooleanVar()
options_menu.add_checkbutton(label="Always On Display", variable=aod_var, command=always_on_display)

notebook = ttk.Notebook(window)
progress = Frame(notebook)
doRCP = Frame(notebook)

notebook.add(progress, text="In Progress")
notebook.add(doRCP, text="do RCP")
notebook.pack(expand=True, fill="both")

recovered = Frame(progress, bg='#2ab85c', width=100, height=400)
left_inprogress = Frame(progress, bg='#4681e0', width=10, height=400)
inprogress = Frame(progress, bg='#4681e0', width=80, height=400)
right_inprogress = Frame(progress, bg='#4681e0', width=10, height=400)
recovery = Frame(progress, bg='#cf4f21', width=100, height=400)

# RECOVERED
recovered_label = Label(recovered, text="Recovered", font=("Arial", 14), bg="#2ab85c")
recovered_label.pack(padx=40)

listbox_recovered = Listbox(recovered,
                            bg="#f7ffde",
                            font=("Arial", 10),
                            width=20,
                            justify='center'

                            )
listbox_recovered.pack()
listbox_recovered.config(height=listbox_recovered.size())

button_remove = Button(recovered, text="Remove Last", command=remove_item_recovered)
button_remove.pack(pady=10)

button_copy_all = Button(recovered, text="Copy ALL", command=copy_elements_from_recovered_to_clipboard)
button_copy_all.pack(pady=10)

# LEFT IN PROGRESS
move_left = Button(left_inprogress, text="<", command=move_left)
move_left.pack(side='left', padx=20)

# IN PROGRESS
inprogress_label = Label(inprogress, text="In Progress", font=("Arial", 14), bg="#4681e0")
inprogress_label.pack(padx=70)

listbox_inprogress = Listbox(inprogress,
                             bg="#f7ffde",
                             font=("Constantia", 10),
                             width=20,
                             justify='center'
                             )

listbox_inprogress.pack()
listbox_inprogress.config(height=listbox_inprogress.size())

button_add = Button(inprogress, text="Add Item", command=add_item)
button_add.pack(pady=10)
listbox_inprogress.config(height=listbox_inprogress.size())

button_remove = Button(inprogress, text="Remove Last", command=remove_item_inprogress)
button_remove.pack(pady=10)

# RIGHT IN PROGRESS
move_right = Button(right_inprogress, text=">", command=move_right)
move_right.pack(side='right', padx=20)

# RECOVERY
recovery_label = Label(recovery, text="Recovery", font=("Arial", 14), bg="#cf4f21")
recovery_label.pack(padx=40)

listbox_recovery = Listbox(recovery,
                           bg="#f7ffde",
                           font=("Arial", 10),
                           width=20,
                           justify='center'
                           )
listbox_recovery.pack()
listbox_recovery.config(height=listbox_recovery.size())

button_remove = Button(recovery, text="Remove Last", command=remove_item_recovery)
button_remove.pack(pady=10)

button_copy_all = Button(recovery, text="Copy ALL", command=copy_elements_from_recovery_to_clipboard)
button_copy_all.pack(pady=10)

# END
recovered.pack(side='left', fill='both', expand=True)
left_inprogress.pack(side='left', fill='both', expand=True)
inprogress.pack(side='left', fill='both', expand=True)
right_inprogress.pack(side='left', fill='both', expand=True)
recovery.pack(side='right', fill='both', expand=True)

window.mainloop()
