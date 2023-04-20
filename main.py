import time
from tkinter import *
from tkinter import ttk, messagebox
import pyperclip

listbox_recovered = None
listbox_recovery = None


def always_on_display():
    window.attributes("-topmost", not window.attributes("-topmost"))


def resize_window():
    window.resizable(not window.resizable(width=True, height=True))


def write_data_to_file(filename):
    with open(filename, 'w') as f:
        f.write(f"RECOVERED:\n")
        f.write(f"Count {listbox_recovered.size()}\n")
        for every in range(listbox_recovered.size()):
            f.write(f"{listbox_recovered.get(every)} \n")
        f.write(f"Time {listbox_recovered.size() * 12}\n")

        f.write(f"\nRECOVERY:\n")
        f.write(f"Count {listbox_recovery.size()}\n")
        for every in range(listbox_recovery.size()):
            f.write(f"{listbox_recovery.get(every)} \n")
        f.write(f"Time {listbox_recovery.size() * 12}\n")

        f.write(f"\nMONITORING:\n")
        f.write(f"Count {40 - listbox_recovered.size() - listbox_recovery.size()}\n")
        f.write(f"https://gta-monitor.fm.intel.com/d/ti2bxWsnz/remote-recovery-scratchwork?orgId=1&refresh=3m\n")
        f.write(f"Count {(40 - listbox_recovered.size() - listbox_recovery.size()) * 12}\n")


def save_every_20_mins():
    while True:
        write_data_to_file('data.txt')
        time.sleep(20 * 60)  # Wait for 20 minutes before running again


def close_window():
    answer = messagebox.askquestion("Uwaga",
                                    "Czy na pewno chcesz zamknąć okno?\nDane zostaną zapisane do pliku dane.txt")
    if answer == 'yes':
        write_data_to_file('data.txt')
        window.destroy()


def add_item():
    item = pyperclip.paste()
    listbox_inprogress.insert(END, item)
    listbox_inprogress.selection_clear(0, END)
    listbox_inprogress.selection_set(END)


def remove_item_inprogress():
    listbox_inprogress.delete(END)
    listbox_inprogress.selection_set(END)


def move_left():
    selection = listbox_inprogress.curselection()
    if selection:
        item = listbox_inprogress.get(selection)
        listbox_inprogress.delete(selection)
        listbox_recovered.insert(END, item)
        listbox_inprogress.selection_set(END)
        update_recovered_label()
        update_monitoring_label()


def move_right():
    selection = listbox_inprogress.curselection()
    if selection:
        item = listbox_inprogress.get(selection)
        listbox_inprogress.delete(selection)
        listbox_recovery.insert(END, item)
        listbox_inprogress.selection_set(END)
        update_recovery_label()
        update_monitoring_label()


def copy_elements_from_recovered_to_clipboard():
    window.clipboard_clear()
    items = [listbox_recovered.get(i) for i in range(listbox_recovered.size())]
    clip_text = " ".join(items)
    window.clipboard_append(clip_text)


def copy_elements_from_recovery_to_clipboard():
    window.clipboard_clear()
    items = [listbox_recovery.get(i) for i in range(listbox_recovery.size())]
    clip_text = " ".join(items)
    window.clipboard_append(clip_text)


def copy_address_to_clipboard():
    window.clipboard_clear()
    window.clipboard_append(
        "https://gta-monitor.fm.intel.com/d/ti2bxWsnz/remote-recovery-scratchwork?orgId=1&refresh=3m"
    )


def update_recovered_label():
    value_label.config(text=listbox_recovered.size())
    time_label.config(text=listbox_recovered.size() * 12)


def update_recovery_label():
    value_label.config(text=listbox_recovery.size())
    time_label.config(text=listbox_recovery.size() * 12)



def update_monitoring_label():
    value_label.config(text=40 - listbox_recovered.size() - listbox_recovery.size())
    time_label.config(text=(40 - listbox_recovered.size() - listbox_recovery.size()) * 12)


def create_listbox(frame, label_text, bg_color, button_command):
    label = Label(frame, text=label_text, font=("Arial", 14), bg=bg_color)
    label.grid(row=0, column=0, padx=40, pady=10)

    listbox = Listbox(frame, bg="#f7ffde", font=("Arial", 10), width=20, justify='center')
    listbox.grid(row=1, column=0)
    listbox.config(height=listbox.size())

    button_remove = Button(frame, text="Usuń ostatni", font=("Constantia", 10), command=button_command)
    button_remove.grid(row=2, column=0, pady=10)

    return listbox


window = Tk()
window.title(string='Raport dzienny')
window.resizable(width=False, height=False)

menu = Menu(window)
window.config(menu=menu)

options_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="Opcje", menu=options_menu)

aod_var = BooleanVar()
r_window = BooleanVar()
options_menu.add_checkbutton(label="Always On Display", variable=aod_var, command=always_on_display)

notebook = ttk.Notebook(window)
progress = Frame(notebook)
doRCP = Frame(notebook)

notebook.add(progress, text="In Progress")
notebook.add(doRCP, text="do RCP")
notebook.grid(row=0, column=0, sticky="nsew")

recovered = Frame(progress, bg='#2ab85c', width=100, height=400)
inprogress = Frame(progress, bg='#4681e0', width=100, height=400)
recovery = Frame(progress, bg='#cf4f21', width=100, height=400)

# RECOVERED
listbox_recovered = create_listbox(recovered, "Recovered", "#2ab85c", lambda: [listbox_recovered.delete(END), update_recovered_label()])

# IN PROGRESS
button_left = Button(inprogress, text="<", font=("Arial Black", 15), command=move_left)
button_left.grid(row=0, column=0, padx=10)
button_right = Button(inprogress, text=">", font=("Arial Black", 15), command=move_right)
button_right.grid(row=0, column=1, padx=10)
listbox_inprogress = create_listbox(inprogress, "In Progress", "#4681e0", remove_item_inprogress)

button_add = Button(inprogress, text="Dodaj", font=("Constantia", 12), bg="#45d634", fg="black", activebackground="#45d634", activeforeground="black", command=add_item)
button_add.grid(row=1, column=1, pady=10)


# RECOVERY
listbox_recovery = create_listbox(recovery, "Recovery", "#cf4f21", lambda: [listbox_recovery.delete(END), update_recovery_label()])


# END

recovered.grid(row=0, column=0, sticky="nsew")
inprogress.grid(row=0, column=2, sticky="nsew")
recovery.grid(row=0, column=4, sticky="nsew")

for i in range(4):
    progress.grid_rowconfigure(i, weight=1)
for i in range(2):
    progress.grid_columnconfigure(i, weight=1)

recovered_RCP = Frame(doRCP, bg='#2ab85c', width=400, height=50)
recovery_RCP = Frame(doRCP, bg='#cf4f21', width=400, height=50)
monitoring_RCP = Frame(doRCP, bg='#4681e0', width=400, height=50)

for i in range(3):
    doRCP.grid_columnconfigure(i, weight=1)

# # Recovered
#
# title_recovered = Label(recovered_RCP, text="Recovered ", font=("Arial", 12), bg="#2ab85c")
# title_recovered.grid(row=0, column=0, padx=10, pady=10, sticky="e")
#
# value_recovered = Label(recovered_RCP, text=listbox_recovered.size(), font=("Arial", 10), bg="#2ab85c",
#                         fg="black")
# value_recovered.grid(row=0, column=1, padx=10, pady=10)
#
# button_comment_1 = Button(recovered_RCP,
#                           text="Podniesione",
#                           command=copy_elements_from_recovered_to_clipboard,
#                           font=("Arial", 10),
#                           bg="#2ab85c",
#                           fg="black",
#                           activebackground="#2ab85c",
#                           activeforeground="black",
#                           takefocus=False,
#                           width=30)
# button_comment_1.grid(row=0, column=2, padx=10, pady=10)
#
# value_recovered_time = Label(recovered_RCP,
#                              text=listbox_recovered.size(),
#                              font=("Arial", 10),
#                              bg="#2ab85c",
#                              fg="black")
# value_recovered_time.grid(row=0, column=3, padx=10, pady=10, sticky="w")
#
# # Recovery
#
# title_recovery = Label(recovery_RCP,
#                        text="Recovery    ",
#                        font=("Arial", 12),
#                        bg="#cf4f21")
# title_recovery.grid(row=0, column=0, padx=10, pady=10, sticky="e")
#
# value_recovery = Label(recovery_RCP,
#                        text=listbox_recovery.size(),
#                        font=("Arial", 10),
#                        bg="#cf4f21",
#                        fg="black")
# value_recovery.grid(row=0, column=1, padx=10, pady=10)
#
# button_comment_2 = Button(recovery_RCP,
#                           text="Posłane w cholere",
#                           command=copy_elements_from_recovery_to_clipboard,
#                           font=("Arial", 10),
#                           bg="#cf4f21",
#                           fg="black",
#                           activebackground="#cf4f21",
#                           activeforeground="black",
#                           takefocus=False,
#                           width=30)
# button_comment_2.grid(row=0, column=2, padx=10, pady=10)
#
# value_recovery_time = Label(recovery_RCP,
#                             text=listbox_recovery.size(),
#                             font=("Arial", 10),
#                             bg="#cf4f21",
#                             fg="black")
# value_recovery_time.grid(row=0, column=3, padx=10, pady=10, sticky="w")
#
# # Monitoring
#
# title_monitoring = Label(monitoring_RCP, text="Monitoring", font=("Arial", 12), bg="#4681e0")
# title_monitoring.grid(row=0, column=0, padx=10, pady=10, sticky="e")
#
# value_monitoring = Label(monitoring_RCP, text=40 - listbox_recovery.size() - listbox_recovered.size(),
#                          font=("Arial", 10),
#                          bg="#4681e0",
#                          fg="black")
# value_monitoring.grid(row=0, column=1, padx=10, pady=10)
#
# button_comment_3 = Button(monitoring_RCP,
#                           text="Link z D",
#                           command=copy_address_to_clipboard,
#                           font=("Arial", 10),
#                           bg="#4681e0",
#                           fg="black",
#                           activebackground="#4681e0",
#                           activeforeground="black",
#                           takefocus=False,
#                           width=30)
# button_comment_3.grid(row=0, column=2, padx=10, pady=10)
#
# value_monitoring_time = Label(monitoring_RCP,
#                               text=480,
#                               font=("Arial", 10),
#                               bg="#4681e0",
#                               fg="black")
# value_monitoring_time.grid(row=0, column=3, padx=10, pady=10, sticky="w")
#
# recovered_RCP.grid(row=0, column=1, sticky="ew")
# recovery_RCP.grid(row=1, column=1, sticky="ew")
# monitoring_RCP.grid(row=2, column=1, sticky="ew")
#
# window.mainloop()


sections = [
    {
        'label_text': 'Recovered',
        'label_bg': '#2ab85c',
        'value_text': listbox_recovered.size(),
        'button_text': 'Podniesione',
        'button_command': copy_elements_from_recovered_to_clipboard,
        'button_bg': '#2ab85c'
    },
    {
        'label_text': 'Recovery',
        'label_bg': '#cf4f21',
        'value_text': listbox_recovery.size(),
        'button_text': 'Posłane w cholere',
        'button_command': copy_elements_from_recovery_to_clipboard,
        'button_bg': '#cf4f21'
    },
    {
        'label_text': 'Monitoring',
        'label_bg': '#4681e0',
        'value_text': 40 - listbox_recovery.size() - listbox_recovered.size(),
        'button_text': 'Link z D',
        'button_command': copy_address_to_clipboard,
        'button_bg': '#4681e0'
    }
]

for i, section in enumerate(sections):
    label = Label(
        master=window,
        text=section['label_text'] + ' ',
        font=('Arial', 12),
        bg=section['label_bg']
    )
    label.grid(row=i, column=0, padx=10, pady=10, sticky='e')

    value_label = Label(
        master=window,
        text=section['value_text'],
        font=('Arial', 10),
        bg=section['label_bg'],
        fg='black'
    )
    value_label.grid(row=i, column=1, padx=10, pady=10)

    button = Button(
        master=window,
        text=section['button_text'],
        command=section['button_command'],
        font=('Arial', 10),
        bg=section['button_bg'],
        fg='black',
        activebackground=section['button_bg'],
        activeforeground='black',
        takefocus=False,
        width=30
    )
    button.grid(row=i, column=2, padx=10, pady=10)

    time_label = Label(
        master=window,
        text=listbox_recovered.size(),
        font=('Arial', 10),
        bg=section['label_bg'],
        fg='black'
    )
    time_label.grid(row=i, column=3, padx=10, pady=10, sticky='w')

window.protocol("WM_DELETE_WINDOW", close_window)
window.mainloop()
