from tkinter import *
from gtts import gTTS
from playsound import playsound

"""Convert your Text into Voice with Python and Google APIs"""

# initializing the window
root = Tk()
root.geometry("350x300")
root.configure(bg='ghost white')
root.title("TEXT TO SPEECH")

label(root, text = "TEXT_TO_SPEECH", font = "arial 20 bold", bg='white smoke').pack()
label(text)

root.mainloop()