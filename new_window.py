# new_window.py
from tkinter import *
from PIL import ImageTk, Image


def open():
    global my_img  # needs global , otherwise the image won't open
    top = Toplevel()
    top.title("Hello Mario!")
    my_img = ImageTk.PhotoImage(Image.open("images/mario1.jpg"))
    Label(top, image=my_img).pack()
    Button(top, text="Close Window", command=top.destroy).pack(padx=10, pady=10)


root = Tk()
root.title("New Window Demo")
Label(root, text="root window", padx=20, pady=20).pack(padx=20, pady=20)
Button(root, text="Open Second Window", command=open).pack(padx=10, pady=10)

root.mainloop()
