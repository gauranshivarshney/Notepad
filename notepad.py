from tkinter import *
from tkinter import messagebox as msg
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

root = Tk()
root.geometry("900x600")
root.title("Untiled - Notepad")

def new_file():
    global file
    root.title("Untitled - Notepad")
    file = None
    text_area.delete(1.0, END)

def open_file():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All files", "*.*"), ("Text documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        text_area.delete(1.0, END)
        f = open(file, "r")
        text_area.insert(1.0, f.read())
        f.close()
    
def save_file():
    global file
    if file == None:
        file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt", filetypes=[("All files", "*,*"), ("Text documents", "*.txt")])
        if file == "":
            file = None
        else:
            f = open(file, "w")
            f.write(text_area.get(1.0, END))
            f.close()
                
            root.title(os.path.basename(file) + " - Notepad")
            print("File saved")
    else:
        f = open(file, "w")
        f.write(text_area.get(1.0, END))
        f.close()

def exit_file():
    root.destroy()

def cut():
    text_area.event_generate(("<<Cut>>"))

def copy():
    text_area.event_generate(("<<Copy>>"))

def paste():
    text_area.event_generate(("<<Paste>>"))

def about():
    msg.showinfo("Notepad", "Notepad by Gauranshi")

text_area = Text(root)
file = None
text_area.pack(expand=True, fill=BOTH)
menu_bar = Menu(root)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_file)
menu_bar.add_cascade(label="File", menu=file_menu)

edit_menu = Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)
edit_menu.add_cascade(label="Edit", menu=edit_menu)

help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="Abou Notepad", command=about)
help_menu.add_cascade(label="Help", menu=menu_bar)

scroll_bar = Scrollbar(text_area)
scroll_bar.pack(side=RIGHT, fill=Y)
scroll_bar.config(command=text_area.yview)
text_area.config(yscrollcommand=scroll_bar.set)

root.config(menu=menu_bar)

root.mainloop()