# Steps to build message encode – decode python project
#
# Import module
# Create display window
# Define function
# Define labels and buttons

from tkinter import *
import base64 #function to encode the binary data to ASCII characters

# Initialise the window

root = Tk()

root.geometry('400x400')
root.resizable(0, 0) # won't be able to minimize
root.title("Message Encode and Decode")
#
Label(root, text='ENCODE DECODE', font='arial 20 bold').pack()
#
Label(root, text='Dhrey', font='arial 10 bold').pack(side=BOTTOM)

# Define variables
message = StringVar()
private_key = StringVar()
mode = StringVar()
result = StringVar()

# define function to encode
def Encode(key, message):
    enc=[]
    
    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

# define function to deode



root.mainloop()