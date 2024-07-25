from tkinter import *
from tkinter import messagebox

def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, END)
    else:
        messagebox.showwarning("Warning", "Please enter some task.")

def deleteTask():
    try:
        index = lb.curselection()[0]
        task = lb.get(index)
        confirm = messagebox.askyesno("Confirmation", f"Are you sure you want to delete the task: {task}?")
        if confirm:
            lb.delete(index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def updateTask():
    try:
        index = lb.curselection()[0]
        task = my_entry.get()
        if task != "":
            lb.delete(index)
            lb.insert(index, task)
            my_entry.delete(0, END)
        else:
            messagebox.showwarning("Warning", "Please enter some task.")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to update.")

ws = Tk()
ws.geometry('500x450+500+200')
ws.title('Python To-Do List')
ws.config(bg="#808080")
ws.resizable(width=False, height=False)

frame = Frame(ws)
frame.pack(pady=10)

lb = Listbox(
    frame,
    width=25,
    height=8,
    font=('Times', 18),
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none",
)
lb.pack(side=LEFT, fill=BOTH)

task_list = [
    'Eat apple',
    'Drink water',
    'Go to the gym',
    'Write software',
    'Write documentation',
    'Take a nap',
    'Learn something',
]

for item in task_list:
    lb.insert(END, item)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry = Entry(
    ws,
    font=('Times', 24)
)
my_entry.pack(pady=20)

button_frame = Frame(ws)
button_frame.pack(pady=20)

addTask_btn = Button(
    button_frame,
    text='Add Task',
    font=('Times 14'),
    bg='#c5f776',
    padx=20,
    pady=10,
    command=newTask
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

delTask_btn = Button(
    button_frame,
    text='Delete Task',
    font=('Times 14'),
    bg='#ff8b61',
    padx=20,
    pady=10,
    command=deleteTask
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

updateTask_btn = Button(
    button_frame,
    text='Update Task',
    font=('Times 14'),
    bg='#f2f2f2',
    padx=20,
    pady=10,
    command=updateTask
)
updateTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

ws.mainloop()