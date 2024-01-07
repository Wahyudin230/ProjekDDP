from tkinter import *
from time import *

def updite():
    time_string = strftime("%I : %M : %S :%p")
    time_Label.config(text=time_string)
    
    time_Label.after(1000,updite)
    

window = Tk()

time_Label = Label(window,font=("Arial",50),fg="#00FF00",bg="black")
time_Label.pack()

updite()

window.mainloop()