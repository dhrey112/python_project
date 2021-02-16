from tkinter import *
#from gtts import gTTS
from playsound import playsound

"""Convert your Text into Voice with Python and Google APIs"""

# initializing the window
root = Tk()
root.geometry("350x300")
root.configure(bg='ghost white')
root.title("TEXT TO SPEECH")

label(root, text = "TEXT_TO_SPEECH", font = "arial 20 bold", bg='white smoke').pack()
label(text="Dhrey", font = 'arial 15 bold', bg ='white smoke' , width = '20').pack(side = 'bottom')

msg = StringVar()
Label(root,text ="Enter Text", font = 'arial 15 bold', bg ='white smoke').place(x=20,y=60)

entry_field = Entry(root, textvariable = msg, width='50')
entry_field.place(x=20, y=100)

root.mainloop()