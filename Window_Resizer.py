from tkinter import *

root = Tk()
root.geometry("250x200")

def window_resize():
    width_value = window_width.get()
    height_value = window_height.get()
    root.geometry(f"{width_value}x{height_value}")

root.title(" Resizer")
l1 = Label(text="Window Resizer", font="comicsansms 11 bold", pady=20)
l1.grid(column=2)

l2 = Label(text="Width: ", font="comicsansms 11")
l2.grid(row=1, column=1)

l3 = Label(text="Height: ", font="comicsansms 11")
l3.grid(row=2, column=1)

window_width = StringVar()
window_height = StringVar()

width_entry = Entry(root, textvariable = window_width).grid(row=1, column=2)
height_entry = Entry(root, textvariable = window_height).grid(row=2, column=2)

Button(text="Change Window Size ", command=window_resize, pady=2, font="comicsansms 11").grid(column=2)

root.mainloop()