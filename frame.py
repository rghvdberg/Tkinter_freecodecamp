# Frame Demo
# frame itself is using pack but the buttons inside the frame use grid


from tkinter import *

root = Tk()
root.title("Frame Demo")

# padding INSIDE of the frame
frame = LabelFrame(root, text="This Is A Frame",
                   padx=15, pady=15, labelanchor=N)

# padding OUTSIDE of the frame
frame.pack(padx=100, pady=100)

b1 = Button(frame, text="Button 1")
b2 = Button(frame, text="Button 2")

b1.grid(column=0, row=0, padx=10, pady=10)
b2.grid(column=1, row=0, padx=10, pady=10)

root.mainloop()
