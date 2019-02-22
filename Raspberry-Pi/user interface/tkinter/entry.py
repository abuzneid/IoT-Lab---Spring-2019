import tkinter as tk
from tkinter import filedialog

def open_handler():
    name = tk.filedialog.askopenfilename(filetypes=(("file","*.jpg"),("All Files","*.*") ))
    print(name)

def button_hanadler(e_v):
    print(e.get())
    print(e_v)

mainwindow=tk.Tk()
mainwindow.geometry("640x340")
mainwindow.title("sensor data ")

menubar=tk.Menu(mainwindow)
sub_menu=tk.Menu(menubar, tearoff=0)
sub_menu.add_command(label="Open File ", command=open_handler)
sub_menu.add_separator()
menubar.add_cascade(label="File", menu=sub_menu)

e_v=tk.StringVar()
e=tk.Entry(mainwindow)
e.grid(row=0, column=0)

b=tk.Button(mainwindow,text="Submit",command=lambda : button_hanadler(e_v))
b.grid(row=0, column=1 )


mainwindow.config(menu=menubar)
mainwindow.mainloop()