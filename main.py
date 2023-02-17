from tkinter import *
from tkinter import ttk
import pyperclip


def always_on_display():
    if window.attributes("-topmost"):
        window.attributes("-topmost", False)
    else:
        window.attributes("-topmost", True)


def add_item():
    item = pyperclip.paste()
    listbox_inprogress.insert(END, item)
    listbox_inprogress.selection_clear(0, END)
    listbox_inprogress.selection_set(END)


def remove_item_recovered():
    listbox_recovered.delete(END)


def remove_item_inprogress():
    listbox_inprogress.delete(END)
    listbox_inprogress.selection_set(END)


def remove_item_recovery():
    listbox_recovery.delete(END)


def move_left():
    selection = listbox_inprogress.curselection()
    if selection:
        item = listbox_inprogress.get(selection)
        listbox_inprogress.delete(selection)
        listbox_recovered.insert(END, item)
        listbox_inprogress.selection_set(END)


def move_right():
    selection = listbox_inprogress.curselection()
    if selection:
        item = listbox_inprogress.get(selection)
        listbox_inprogress.delete(selection)
        listbox_recovery.insert(END, item)
        listbox_inprogress.selection_set(END)


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

options_menu = Menu(menu, tearoff=0)
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
button_left = Button(left_inprogress, text="<", font=("Arial Black", 15), command=move_left)
button_left.pack(side='left', padx=20)

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
button_right = Button(right_inprogress, text=">", font=("Arial Black", 15), command=move_right)
button_right.pack(side='right', padx=20)

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

recovered_RCP = Frame(doRCP, bg='#2ab85c', width=400, height=50)
recovery_RCP = Frame(doRCP, bg='#cf4f21', width=400, height=50)
monitoring_RCP = Frame(doRCP, bg='#4681e0', width=400, height=50)

doRCP.grid_columnconfigure(0, weight=1)
doRCP.grid_columnconfigure(1, weight=1)
doRCP.grid_columnconfigure(2, weight=1)
doRCP.grid_rowconfigure(0, weight=1)

title_label = Label(recovered_RCP, text="Tytuł", font=("Arial", 12), bg="red", fg="white")
title_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

value1_label = Label(recovered_RCP, text="Wartość 1", font=("Arial", 10), bg="red", fg="white")
value1_label.grid(row=0, column=1, padx=10, pady=10)

button = Button(recovered_RCP, text="Przycisk", font=("Arial", 10), bg="white", fg="red")
button.grid(row=0, column=2, padx=10, pady=10)

value2_label = Label(recovered_RCP, text="Wartość 2", font=("Arial", 10), bg="red", fg="white")
value2_label.grid(row=0, column=3, padx=10, pady=10, sticky="w")


recovered_RCP.grid(row=1, column=0, sticky="nsew")
recovery_RCP.grid(row=2, column=0, sticky="nsew")
monitoring_RCP.grid(row=3, column=0, sticky="nsew")

window.mainloop()
