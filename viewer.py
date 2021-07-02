from tkinter import *
# PIL needs to be installed with pip or package manager
from PIL import ImageTk, Image


def back():
    global image_index
    global image_list
    global my_label
    image_index -= 1
    # loop around
    image_index = image_index % len(image_list)

    # use this if you want to stop at 0
    # if image_index < 0:
    #     image_index = 0

    my_label.configure(image=image_list[image_index])


def forward():
    global image_index
    global image_list
    global my_label
    image_index += 1
    # loop around
    image_index = image_index % len(image_list)

    # use this if you want to stop at end of list
    # if image_index > len(image_list) - 1:
    #     image_index = len(image_list) -1

    my_label.configure(image=image_list[image_index])


root = Tk()
root.title("My Image Viewer")
image_index = 0


my_img1 = ImageTk.PhotoImage(Image.open("images/mario1.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("images/mario2.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("images/mario3.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("images/luigi1.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open("images/luigi2.jpg"))
image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]
my_label = Label(image=image_list[image_index])

button_back = Button(root, text="Prev", command=back)
button_forward = Button(root, text="Next", command=forward)
button_quit = Button(root, text="Exit Program", command=root.quit)

my_label.grid(column=0, row=0, columnspan=2)
button_back.grid(column=0, row=1)
button_forward.grid(column=1, row=1)
button_quit.grid(column=0, row=2, columnspan=2)

root.mainloop()
