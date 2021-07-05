from tkinter import *

root = Tk()

# Creating Label Widgets
myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="My Name Is Rob")

# Grids are relative
myLabel1.grid(row=0,column=0)
myLabel2.grid(row=1,column=1) # column=5 would yield the same result

root.mainloop()