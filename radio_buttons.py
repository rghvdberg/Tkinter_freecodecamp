# Radio Buttons

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Radio Buttons")

TOPPINGS = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion"),
]

pizza = StringVar()
# if there's no default value set than all radio buttons are greyed out
pizza.set("Pepperoni")

# my_label has to be defined before 'clicked' function otherwise my_label.configure() doesn't work
my_label = Label(root, text=pizza.get())

for txt, topping in TOPPINGS:
    Radiobutton(root, text=txt, variable=pizza,
                value=topping).pack(anchor=W, pady=5)

bt_order = Button(root, text="Place Order",
                  command=lambda: clicked(pizza.get())).pack(padx=20)


def clicked(value):
    global my_label
    my_label.configure(text=value)


my_label.pack()

# it looks like one can just call mainloop() instead of root.mainloop()?
mainloop()
