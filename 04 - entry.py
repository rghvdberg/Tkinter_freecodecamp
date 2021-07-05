from tkinter import *

root = Tk()

e = Entry(root)
e.pack()
e.insert(0,"Enter Your Name: ") # default text

def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()


myButton = Button(root, text="Enter your name", command=myClick)
myButton.pack()

root.mainloop()
