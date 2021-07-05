# Open File Dialog

from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("Open Files Dialog Box")


def open():
    global my_image
    root.filename = filedialog.askopenfilename(
        initialdir="./images", title="Select A File",
        filetypes=(("jpg files", "*.jpg"), ("all files", "*.*")))
    Label(root, text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    Label(root, image=my_image).pack()


# note that clicking the button a second time will clear the previous image, 
# but the previous image will not be removed from the window
my_btn = Button(root, text="Open File", command=open).pack()

root.mainloop()
