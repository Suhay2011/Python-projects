# Import necessary libraries
from tkinter import*
window = Tk()
window.title("Event Handler")
window.geometry("100x100")
def handle_click(event):
    print("\nThe button was clicked")

button = Button(text="Click Me!")
button.pack()

# Bind click event to handle_click()
button.bind("<Button1>", handle_click)
window.mainloop()