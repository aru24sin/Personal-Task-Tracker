import tkinter as tk
from tkinter import *
from tkmacosx import Button
import sv_ttk

# Initialize the main window
root = Tk()
root.title('Task Tracker')
root.geometry('450x450+400+100')
root.resizable(True, True)

# VSCode-like dark theme colors
bg_color = "#1e1e1e"  # Dark background like VSCode
task_entry_bg = "#252526"  # Slightly lighter for task entry
text_color = "#d4d4d4"  # Light gray for text
button_bg = "#007acc"  # Blue color for buttons like VSCode accent
button_fg = "#ffffff"  # White text on buttons
highlight_color = "#3a3d41"  # Highlight color for listbox

# Set the background color
root.configure(bg=bg_color)

sv_ttk.set_theme("dark")

# List to store tasks
tasks = []

# Function to update the listbox with current tasks
def update_task_listbox():
    listbox.delete(0, END)
    for task in tasks:
        listbox.insert(END, task)

# Function to add a task
def add_task():
    task_text = taskEntry.get()
    if task_text != "":
        tasks.append(task_text)
        update_task_listbox()
        taskEntry.delete(0, END)

# Function to delete a selected task
def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        tasks.pop(selected_task_index)
        update_task_listbox()
    except IndexError:
        pass  # No task selected

# Set icon image for the window
imgIcon = PhotoImage(file="/Users/aru/Downloads/cc005054a4a30e2e44fb4ff12a17c1d4.png")
root.iconphoto(False, imgIcon)

# Heading label with VSCode-like dark background and light text
heading = Label(root, text="Task Tracker", font=("Helvetica bold", 20), fg=button_bg, bg="#1e1e1e")
heading.place(x=160, y=10)

# Frame for task entry with darker background
frame = Frame(root, width=400, height=50, bg=task_entry_bg)
frame.place(x=25, y=60)

# Entry field for task input with dark background and light text
task = StringVar()
taskEntry = Entry(frame, width=18, font="Consolas 18", bd=0, textvariable=task, bg="#1e1e1e", fg="#007acc")
taskEntry.place(x=10, y=7)

# Button to add task with VSCode accent color
addButton = Button(root, text="Add Task", font="Consolas 16", width=135, bg="#1e1e1e", fg="#20a4e6", bd=0, command=add_task)
addButton.place(x=25, y=120)

# Listbox to display tasks with dark background and light text
listbox = Listbox(root, font="Consolas 16", width=25, height=10, bg=task_entry_bg, bd=0, fg=text_color, selectbackground="#1e1e1e", selectforeground=text_color)
listbox.place(x=25, y=160)

# Button to delete task with VSCode accent color
deleteButton = Button(root, text="Delete Task", font="Consolas 16", width=135, bg="#1e1e1e", fg="#20a4e6", bd=0, command=delete_task)
deleteButton.place(x=25, y=380)

# Start the GUI main loop
root.mainloop()


