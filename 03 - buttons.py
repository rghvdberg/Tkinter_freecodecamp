from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root,text="Look! I clicked a button!")
    myLabel.pack()

myButton = Button(root,text="Click Me!", command=myClick, fg="yellow",background="#000000") # no () after function name
myButton.pack()

root.mainloop()