from tkinter import *
import random, string

# import pyperclip

root = Tk()
root.geometry("400x400")
root.resizable(0, 0)
root.title("Password Generator")

Label(root, text='PASSWORD GENERATOR', font='arial 10 bold').pack()
# Label(root, text='', font='arial 15 bold').pack(side=BOTTOM)

pass_label = Label(root, text='PASSWORD LENGTH', font='arial 8 bold 10').pack()
pass_len = IntVar()
length = Spinbox(root, from_ = 8, to_ = 32, textvariable=pass_len, width = 15).pack()

root.mainloop()
