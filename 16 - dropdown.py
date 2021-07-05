from tkinter import *

root = Tk()
root.title("Dropdown")
root.geometry("400x400")

my_var = StringVar()
my_var.set("Monday")
my_label = Label(root, text=my_var.get())


def show_selection(var):
    my_label.configure(text=var)


my_options = ["Monday",
              "Tuesday",
              "Wednesday",
              "Thursday",
              "Friday"]

my_var.set(my_options[0])

drop = OptionMenu(root, my_var, *my_options, command=lambda text:show_selection(text))
drop.pack()
my_label.pack()

root.mainloop()
