# slider.py
from tkinter import *

root = Tk()
root.title("Slider")
root.geometry("200x200")
my_label = Label(root, text="", padx=10, pady=10)

# function needs a parameter otherwise we get:
# typeError: slider_changed() takes 0 positional arguments but 1 was given
def slider_changed(event):
    my_label.configure(text=str(my_slider.get()))


my_slider = Scale(root, from_=0, to=200, orient=HORIZONTAL,
                  command=slider_changed)
# alternative is to use:
# current_value = DoubleVar()
# and in the Scale() widget use:
# variable=current_var
# see https://www.pythontutorial.net/tkinter/tkinter-slider/

my_slider.pack(pady=30)
my_label.pack()

root.mainloop()
