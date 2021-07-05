# popup.py
from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Popup")

# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
# not covered in video:  askyesnocancel, askretrycancel


def showPopup():
    # messagebox.showinfo("This is my Popup", "Hello World!")
    # messagebox.showwarning("This is my Popup", "Hello World!")
    # messagebox.showerror("This is my Popup", "Hello World!")
    response = messagebox.askquestion("This is my Popup", "Hello World!")
    # messagebox.askokcancel("This is my Popup", "Hello World!")
    #response = messagebox.askyesno("This is my Popup", "Hello World!")
    #response = messagebox.askyesnocancel("Tihs is my Popup", "Hello World!")
    # messagebox.askretrycancel("This is my Popup!", "Hello World!")
    print(response)
    if response == "yes":
        Label(root, text="You clicked yes.").pack()
    if response == "no":
        Label(root, text="You clicked no.").pack()


Button(root, text="Popup", command=showPopup).pack(padx=20, pady=20)

root.mainloop()
