from tkinter import *

root = Tk()
root.title("Checkboxes")
root.geometry("400x400")

my_var1 = IntVar()
my_var2 = StringVar()

my_var1.set(0)
my_var2.set("Off") # if this is not set the checkbox is grayed out

myLabel = Label(root, text=my_var1.get())


def on_checkbutton_clicked(val):
    myLabel.configure(text=val)


check_button1 = Checkbutton(root, text="Check it out.",
                            variable=my_var1,
                            command=lambda: on_checkbutton_clicked(my_var1.get()))

check_button2 = Checkbutton(root, text="And this!", variable=my_var2,
                            onvalue="Checkbutton 2 is on",
                            offvalue="Checkbutton 2 is off", 
                            command=lambda: on_checkbutton_clicked(my_var2.get()))
# optional
#check_button1.deselect()
#check_button2.deselect()

check_button1.pack(padx=20, pady=20)
check_button2.pack(padx=20, pady=20)
myLabel.pack()

root.mainloop()
