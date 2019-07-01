import tkinter as tk
from tkinter import filedialog

def open_handler():
    name = tk.filedialog.askopenfilename(filetypes=(("file","*.jpg"),("All Files","*.*") ))
    print(name)

def button_hanadler(r_v):
    print(r_v)

mainwindow=tk.Tk()
mainwindow.geometry("640x340")
mainwindow.title("sensor data ")

menubar=tk.Menu(mainwindow)
sub_menu=tk.Menu(menubar, tearoff=0)
sub_menu.add_command(label="Open File ", command=open_handler)
sub_menu.add_separator()
menubar.add_cascade(label="File", menu=sub_menu)

r_v=tk.IntVar()


r=tk.Radiobutton(mainwindow, text="Keep me Logged in",variable=r_v, value=1, command=lambda:button_hanadler(r_v.get()))
r.pack()

r1=tk.Radiobutton(mainwindow, text="Save Password",variable=r_v, value=2, command=lambda:button_hanadler(r_v.get()))
r1.pack()




mainwindow.config(menu=menubar)
mainwindow.mainloop()