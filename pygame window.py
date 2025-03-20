#import necessary libraries
from tkinter import *
from datetime import date

# Create Window
root = Tk()
root.title('Getting Started With Widgets')
root.geometry('400x300')

# Add widgets
# Add Label
lbl = Label(text="Hey There!", fg="white", bg="#eb4034", height=1, width=300)
lbl.pack()

#Add Label for getting name as input from user
# Use Entry Widget to create a text box for user to enter details
name_lbl = Label(text="Full Name", bg="#2ea69a")
name_lbl.pack()


name_entry = Entry()
name_entry.pack()

# Function to display a Message

# Add a Text Widget to display information/messages
text_box = Text(height=3)
def display():

# Add button and give value of cmommand as name of the function
# Press button, display function will be called automatically

  name = name_entry.get()
  global Message
  Message = "Welcome to the Account Creation page! \nTodays Date:" +str(date.today())
  greet = "Hello "+name+"\n"
  text_box.insert(END, greet)
  text_box.insert(END, Message)

# Add button and give value of command as name of the function
# Press button, display function will be called automatically
btn = Button(text="Begin", command=display, height=1, bg="#1261A0", fg="white")

btn.pack()
text_box.pack()

root.mainloop()