from tkinter import *
import pyperclip


def always_on_display():
    if window.attributes("-topmost"):
        window.attributes("-topmost", False)
    else:
        window.attributes("-topmost", True)


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

menu = Menu(window)
window.config(menu=menu)

options_menu = Menu(menu)
menu.add_cascade(label="Options", menu=options_menu)

aod_var = BooleanVar()
options_menu.add_checkbutton(label="Always On Display", variable=aod_var, command=always_on_display)

recovered = Frame(window, bg='#2ab85c', width=200, height=400)
left_inprogress = Frame(window, bg='#4681e0', width=20, height=400)
inprogress = Frame(window, bg='#4681e0', width=300, height=400)
right_inprogress = Frame(window, bg='#4681e0', width=20, height=400)
recovery = Frame(window, bg='#cf4f21', width=200, height=400)

# RECOVERED
recovered_label = Label(recovered, text="Recovered", font=("Arial", 28), bg="#2ab85c")
recovered_label.pack(padx=40)

listbox_recovered = Listbox(recovered,
                            bg="#f7ffde",
                            font=("Arial", 12),
                            width=12
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
inprogress_label = Label(inprogress, text="In Progress", font=("Arial", 28), bg="#4681e0")
inprogress_label.pack(padx=70)

listbox_inprogress = Listbox(inprogress,
                             bg="#f7ffde",
                             font=("Constantia", 20),
                             width=12
                             )

listbox_inprogress.pack()
listbox_inprogress.config(height=listbox_inprogress.size())

button_add = Button(inprogress, text="Add Item", command=add_item)
button_add.pack(pady=10)

button_remove = Button(inprogress, text="Remove Last", command=remove_item_inprogress)
button_remove.pack(pady=10)

# RIGHT IN PROGRESS
move_right = Button(right_inprogress, text=">", command=move_right)
move_right.pack(side='right', padx=20)

# RECOVERY
recovery_label = Label(recovery, text="Recovery", font=("Arial", 28), bg="#cf4f21")
recovery_label.pack(padx=40)

listbox_recovery = Listbox(recovery,
                           bg="#f7ffde",
                           font=("Arial", 12),
                           width=12
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
