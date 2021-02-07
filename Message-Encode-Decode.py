# Steps to build message encode – decode python project
#
# Import module
# Create display window
# Define function
# Define labels and buttons

from tkinter import *
import base64  # function to encode the binary data to ASCII characters

# Initialise the window

root = Tk()

root.geometry('400x400')
root.resizable(0, 0)  # won't be able to minimize
root.title("Message Encode and Decode")
#
Label(root, text='ENCODE DECODE', font='arial 20 bold').pack()
#
Label(root, text='Dhrey', font='arial 10 bold').pack(side=BOTTOM)

# Define variables
text = StringVar()
private_key = StringVar()
mode = StringVar()
result = StringVar()


# define function to encode
def encode(key, message):
    enc = []

    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()


# define function to decode
def decode(key, message):
    dec = []
    message = base64.urlsafe_b64decode(message).decode()

    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i]) - ord(key_c)) % 256))

    return "".join(dec)


# function to set mode
def mode():
    if mode.get() == 'e':
        result.set(encode(private_key.text.get()))
    elif mode.get() == 'd':
        result.set(decode(private_key.text.get()))
    else:
        result.set('Invalid Mode')


# function to exit window
def close_window():
    root.destroy()


# function to reset window, it will set all variable to empty string
def reset():
    text.set("")
    private_key.set("")
    mode.set("")
    result.set("")


# Labels and Button
Label(root, font='arial 12 bold', text='MESSAGE').place(x=60, y=60)
Entry(root, font='arial 10', textvariable=text, bg='ghost white').place(x=290, y=60)

root.mainloop()
