from tkinter import *
import parser
from math import factorial

window = Tk()
window.title('Calculator')

#adding the input field
display = Entry(window)
display.grid(row=1, columnspan=6, sticky=N+E+W+S)


#Code to add buttons to the Calculator
Button(window, text="1",command=lambda:get_variables(1)).grid(row=2, column=0, sticky=N+S+E+W)

Button(window, text="2",command=lambda:get_variables(2)).grid(row=2, column=1, sticky=N+S+E+W)

Button(window, text="3",command=lambda:get_variables(3)).grid(row=2, column=2, sticky=N+S+E+W)

Button(window, text="4",command=lambda:get_variables(3)).grid(row=2, column=3, sticky=N+S+E+W)
# i keeps the track of current position on the input text field
i = 0
# Receives the digit as parameter and display it on the input field

def get_variables(num):
    global i
    display.insert(i, num)
    i+=1
window.mainloop()
