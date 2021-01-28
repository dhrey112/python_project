# Steps to build message encode – decode python project
#
# Import module
# Create display window
# Define function
# Define labels and buttons

from tkinter import *
import base64

# Initialise the window

root = Tk()

root.geometry('400x400')
root.resizable(0, 0) # won't be able to minimize
root.title("Message Encode and Decode")
#
Label(root, text='ENCODE DECODE', font='arial 20 bold').pack()
#
Label(root, text='Dhrey', font='arial 10 bold').pack(side=BOTTOM)

root.mainloop()