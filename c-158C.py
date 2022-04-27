"""from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Addition")
root.geometry("600x400")
inputBox = Entry(root)
inputBox.pack()
def addition():
    number = 5
    getInput = inputBox.get()
    messagebox.showinfo("Error","Cannot add two different data type: integer and string")
button = Button(root, text = "addition",command = addition)
button.pack()

root.mainloop()"""

from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Addition")
root.geometry("600x400")
inputBox = Entry(root)
inputBox.pack()
def addition():
    number = 5
    getInput = inputBox.get()
    try:
        print(number + getInput)
    except(TypeError):
        messagebox.showinfo("Error","Cannot add two different data type: integer and string")
button = Button(root, text = "addition",command = addition)
button.pack()

root.mainloop()