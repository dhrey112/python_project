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
label(text="Dhrey", font = 'arial 15 bold', bg ='white smoke' , width = '20').pack(side = 'bottom')

msg = StringVar()
Label(root,text ="Enter Text", font = 'arial 15 bold', bg ='white smoke').place(x=20,y=60)

entry_field = Entry(root, textvariable = msg, width='50')
entry_field.place(x=20, y=100)

# Function to Convert Text to Speech in Python
def Text_to_speech():
    message = entry_field.get()
    speech = gTTS(text = message)
    speech.save('sound.mp3')
    playsound('sound.mp3')
    speech.close('sound.mp3')
    
def exit():
    root.destroy()
    
def reset():
    msg.set("")

# Defining Function for buttons

Button(root, text = "PLAY", font = 'arial 15 bold' , command = Text_to_speech ,width = '4').place(x=25,y=140)
Button(root, font = 'arial 15 bold',text = 'EXIT', width = '4' , command = Exit, bg = 'OrangeRed1').place(x=100 , y = 140)
Button(root, font = 'arial 15 bold',text = 'RESET', width = '6' , command = Reset).place(x=175 , y = 140)

root.mainloop()