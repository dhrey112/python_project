from tkinter import *
import random, string
import pyperclip

root = Tk()
root.geometry("400x400")
root.resizable(0, 0)
root.title("Password Generator")

Label(root, text='PASSWORD GENERATOR', font='arial 10 bold').pack()
# Label(root, text='', font='arial 15 bold').pack(side=BOTTOM)

pass_label = Label(root, text='PASSWORD LENGTH', font='arial 8 bold').pack()
pass_len = IntVar()
length = Spinbox(root, from_=8, to_=32, textvariable=pass_len, width=15).pack()

# Function to Generate Password

pass_str = StringVar()
def generator():
    password = ''

    for _ in range(4):
        password = \
            random.choice(string.ascii_uppercase) + \
            random.choice(string.ascii_lowercase) + \
            random.choice(string.digits) + \
            random.choice(string.punctuation)
    for _ in range(pass_len.get() - 4):
        password += random.choice(
            string.ascii_uppercase
            + string.ascii_lowercase
            + string.digits
            + string.punctuation
        )

    pass_str.set(password)


Button(root, text = "Generate Password", command = generator).pack(pady=5)
Entry(root , textvariable = pass_str).pack()
def Copy_password():
    pyperclip.copy(pass_str.get())
Button(root, text = 'COPY TO CLIPBOARD', command = Copy_password).pack(pady=5)

root.mainloop()
