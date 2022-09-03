from email import message
from tkinter import *
from tkinter import messagebox
import tkinter
import pickle

root = Tk()
#Task getting added into Listbox
def AddTask():
    task = Textentry.get()
    if task != "":
        box.insert(tkinter.END , task)
    else:
        tkinter.messagebox.showwarning(title = "Enter a task!" , message = "Enter some text!")

def TaskDel():
    try:
        Tasksel = box.curselection()[0]
        box.delete(Tasksel)
    except:
        tkinter.messagebox.showwarning(title = "Select a Task!", message= "Select a task to delete!")

def SaveTasks():
    tasks = box.get(0 , box.size())
    pickle.dump(tasks , open("tasks.dat" , "wb"))

def LoadTasks():
    try:
        tasks = pickle.open(r"C:\Users\Suresh\Desktop\slashdev\tasks.dat" , "rb")
        box.delete(0 , tkinter.END)
        for task in tasks:
            box.insert(tkinter.END , tasks)
    except:
        tkinter.messagebox.showwarning(title = "File not found!" , message= "Could not find \"tasks.dat\" file!")





#GUI
root.geometry("300x200")
root.title("ToDo app")
frame_tasks = tkinter.Frame(root)
frame_tasks.pack()
menu = Menu(root)
item = Menu(menu)
item.add_command(label= "-x-")
menu.add_cascade(label= "Welcome" , menu=item)

menu.add_cascade(label= "to" , menu = item)

menu.add_cascade(label= "my" , menu = item)

menu.add_cascade(label= "app!" , menu = item)
root.config(menu=menu)

box = Listbox(root , height = 3 , width= 50)
box.pack()

Textentry = Entry(root , width= 50)
Textentry.pack()

button_task_add = Button(root , text= "Add Task" , width=50 , command = AddTask)
button_task_add.pack()

button_task_delete = Button(root , text= "Delete Task" , width=50, command= TaskDel)
button_task_delete.pack()

button_task_save = Button(root , text= "Save Tasks" , width=50, command= SaveTasks)
button_task_save.pack()

button_task_load = Button(root , text= "Load Tasks" , width=50, command= LoadTasks)
button_task_load.pack()

scrollbar = Scrollbar(root)
scrollbar.pack(side= tkinter.RIGHT , fill= tkinter.Y)

box.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=box.yview)



root.mainloop()