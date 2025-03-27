#Import necessary libraries
from tkinter import *
from tkinter import messagebox
 
# Setup Tkinter Window
root = Tk()
root.geometry("200x200")

def msg():
    messagebox.askokcancel ("Alert", "Stop! Virus Found")

button = Button(root, text="Scan for Virus", command=msg)
button.place(x=40, y=80)

def msg2():
    messagebox.showwarning( "Do You Want To Remove The Virus Found?")

button2 = Button2(root, text="Remove  Virus?", command=msg2)
button.place(x=60, y=120)

def msg3():
    messagebox.showsolution("Alert", "Remove all Virus Now?" )

button3 = Button3(root, text=" Remove Virus?"
, command=msg3)
button.place(x=60, y=120)

# Entering main event loop
root.mainloop()