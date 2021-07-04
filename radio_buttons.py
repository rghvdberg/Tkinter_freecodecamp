# Radio Buttons

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Radio Buttons")

r = IntVar()
r.set(1)
# my_label has to be defined before 'clicked' function otherwise my_label.configure() doesn't work
my_label = Label(root, text=r.get())

def clicked(value):
    global my_label
    print(value)
    my_label.configure(text=str(value))


Radiobutton(root, text="Option 1", variable=r, value=1,
            command=lambda: clicked(r.get())).pack()
Radiobutton(root, text="Option 2", variable=r, value=2,
            command=lambda: clicked(r.get())).pack()

# my_label = Label(root, text=r.get()).pack()
my_label.pack()

mainloop()
