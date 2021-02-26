import tkinter
from PIL import Image, ImageTk
import random

window = tkinter.Tk()
window.geometry('300x300')
window.title('Roll the Dice')

blank_line = tkinter.Label(window, text="")
blank_line.pack()

# adding label with different font and formatting
heading_label = tkinter.Label(window, text='Hello!', fg='light green', bg='dark red', font='Helvetica 16 bold italic')
heading_label.pack()

# image
dice = ['die1.png', 'die2.png', 'die3.png',
        'die4.png', 'die5.png', 'die6.png']

# simulating the dice with random numbers between
# 0 to 6 and generating image

dice_image = ImageTk.PhotoImage(Image.open(random.choice(dice)))

# Constructing a label for image, adding a button and assigning functionality

# construct a label widget for image
image_label = tkinter.Label(window, image=dice_image)
image_label.image = dice_image
image_label.pack(expand=True)  # packing a widget in the parent widget


# function activated by button
def rolling_dice():
    dice_image = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    # update image
    image_label.configure(image=dice_image)
    # keep a reference
    image_label.image = dice_image


# adding button, and command will use rolling_dice function
button = tkinter.Button(window, text='Roll the Dice', fg='blue', command=rolling_dice)

# pack a widget in the parent widget
button.pack(expand=True)

window.mainloop()
