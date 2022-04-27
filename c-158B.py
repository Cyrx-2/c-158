"""from tkinter import *
root= Tk()
root.title("Geometry Error")
root.geometry("600")
root.mainloop()"""

from tkinter import *
root= Tk()
root.title("Geometry Error")
root.geometry("600")
try:
    root.geometry("600")
except:
    print("Bad geometry error, ony one dimesion passed in geometry instead of two")
root.mainloop()

