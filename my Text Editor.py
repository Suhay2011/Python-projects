#Import necessary packages
from tkinter import*
from tkinter.filedialog import askopenfilename, asksaveasfilename

#Setup Root Window
window = Tk()
window.title("Codingal's Text Editor")
window.geometry("600x500")

#Function to Open a File
def open_file():
    filepath = askopenfilename(
        filetypes=[("Text Files", "*,txt"), ("All Files", "*")]
    )
    if not filepath:
        return
    txt_edit.delete(1,0, END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(END, text)
        input_file.closed


#Function to save a file
def save_file():
    #Save the current file as a new file
    filepath = asksaveasfilename(
        defaulttextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    with open(filepath, "w") as outut_file:
    #Read the edited content and update in the output file
     text = txt_edit.get(1,0, END)
    output_file.write(text)



#Add widgets  in the application
txt_edit = Text(window)
fr_buttons = Frame(window, relief=RAISED, bd=2)
btn_open = Button(fr_buttons, text="open", command=open_file)
btn_save = Button(fr_buttons, text="Save As...", command=save_file)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)

fr_buttons.grid(roe=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()