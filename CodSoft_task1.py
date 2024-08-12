# Task 1 :- T0-do List
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
import json

def load_tasks():
    try:
        with open("tasks.json", "r") as f:
            tasks = json.load(f)
        for task in tasks:
            lb.insert(END, task)
    except FileNotFoundError:
        pass

def save_tasks():
    tasks = lb.get(0, END)
    with open("tasks.json", "w") as f:
        json.dump(tasks, f)

def new_task():
    task = my_entry.get()
    priority = priority_var.get()
    if task != "":
        task_number = lb.size() + 1  # Task numbers start from 1
        formatted_task = f"[{task_number}] {task} - Priority: {priority}"
        lb.insert(END, formatted_task)
        my_entry.delete(0, "end")
        save_tasks()
    else:
        messagebox.showwarning("warning", "Please enter some task.")

def delete_task():
    try:
        selected_task_index = lb.curselection()  # Get the index of the selected task
        if not selected_task_index:
            raise Exception("No task selected")
        lb.delete(selected_task_index)  # Delete the selected task
        update_task_numbers()  # Update the task numbers
        save_tasks()
    except Exception as e:
        messagebox.showwarning("warning", str(e))

def edit_task():
    try:
        selected_task_index = lb.curselection()
        if not selected_task_index:
            raise Exception("No task selected")
        selected_task = lb.get(selected_task_index)
        my_entry.delete(0, END)
        my_entry.insert(0, selected_task.split(" - ")[0].split(" ", 1)[1])
        lb.delete(selected_task_index)
        update_task_numbers()
        save_tasks()
    except Exception as e:
        messagebox.showwarning("warning", str(e))

def update_task_numbers():
    tasks = lb.get(0, END)
    lb.delete(0, END)
    for i, task in enumerate(tasks, start=1):
        task_desc = task.split(" ", 1)[1]  # Keep the rest of the task description unchanged
        lb.insert(END, f"[{i}] {task_desc}")

def search_task():
    search_query = simpledialog.askstring("Search", "Enter search query:")
    if search_query:
        for index in range(lb.size()):
            task = lb.get(index)
            if search_query.lower() in task.lower():
                lb.selection_set(index)
                lb.see(index)
                break

ws = Tk()
ws.geometry('600x600+500+200')
ws.title('My Task Manager')  # Title
ws.config(bg='#F0F0F0')
ws.resizable(width=False, height=False)

# Outer frame for the listbox and scrollbar
outer_frame = Frame(ws, bg='#F0F0F0')
outer_frame.pack(pady=10)

# Frame for the listbox and scrollbar with light greyish-black border
inner_frame = Frame(outer_frame, bg='#F0F0F0')
inner_frame.pack(padx=10, pady=10)

lb = Listbox(
    inner_frame,
    width=35,
    height=12,
    font=('Helvetica', 14),
    bd=1,
    fg='black',
    highlightthickness=2,
    highlightbackground='#4B4B4B',  # Light greyish-black color
    selectbackground='#ADD8E6',
    activestyle="none",
)
lb.pack(side=LEFT, fill=BOTH)

sb = Scrollbar(inner_frame, bd=1, highlightthickness=2, highlightbackground='#4B4B4B')
sb.pack(side=RIGHT, fill=Y)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

# Frame for the entry widget with light greyish-black border
entry_frame = Frame(ws, bg='#F0F0F0')
entry_frame.pack(pady=20)

my_entry = Entry(
    entry_frame,
    font=('Helvetica', 24),
    bg='#FFFFFF',
    fg='black',
    borderwidth=2,
    highlightthickness=2,
    highlightbackground='#4B4B4B',  # Light greyish-black color
)
my_entry.pack(pady=20, padx=20, fill=BOTH)

# Priority selection
priority_var = StringVar(value="Medium")
priority_frame = Frame(ws, bg='#F0F0F0')
priority_frame.pack(pady=10)
priority_label = Label(priority_frame, text="Priority:", bg='#F0F0F0')
priority_label.pack(side=LEFT, padx=5)
priority_options = OptionMenu(priority_frame, priority_var, "High", "Medium", "Low")
priority_options.pack(side=LEFT)

# Frame for buttons with light greyish-black border
button_frame = Frame(ws, bg='#F0F0F0')
button_frame.pack(pady=20)

add_task_btn = Button(
    button_frame,
    text='Add Task',
    font=('Helvetica', 16),
    bg='#90EE90',
    fg='black',
    padx=30,
    pady=15,
    command=new_task,
    borderwidth=2,
    highlightthickness=2,
    highlightbackground='#4B4B4B',  # Light greyish-black color
    activebackground='#98FB98',
)
add_task_btn.pack(fill=BOTH, expand=True, side=LEFT, padx=10)

del_task_btn = Button(
    button_frame,
    text='Delete Task',
    font=('Helvetica', 16),
    bg='#FFB6C1',
    fg='black',
    padx=30,
    pady=15,
    command=delete_task,
    borderwidth=2,
    highlightthickness=2,
    highlightbackground='#4B4B4B',  # Light greyish-black color
    activebackground='#FFC0CB',
)
del_task_btn.pack(fill=BOTH, expand=True, side=LEFT, padx=10)

edit_task_btn = Button(
    button_frame,
    text='Edit Task',
    font=('Helvetica', 16),
    bg='#ADD8E6',
    fg='black',
    padx=30,
    pady=15,
    command=edit_task,
    borderwidth=2,
    highlightthickness=2,
    highlightbackground='#4B4B4B',  # Light greyish-black color
    activebackground='#B0E0E6',
)
edit_task_btn.pack(fill=BOTH, expand=True, side=LEFT, padx=10)

search_task_btn = Button(
    button_frame,
    text='Search Task',
    font=('Helvetica', 16),
    bg='#FFD700',
    fg='black',
    padx=30,
    pady=15,
    command=search_task,
    borderwidth=2,
    highlightthickness=2,
    highlightbackground='#4B4B4B',  # Light greyish-black color
    activebackground='#FFC107',
)
search_task_btn.pack(fill=BOTH, expand=True, side=LEFT, padx=10)

load_tasks()
ws.mainloop()
