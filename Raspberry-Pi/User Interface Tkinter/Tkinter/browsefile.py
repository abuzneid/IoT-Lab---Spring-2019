from tkinter import filedialog
import tkinter as tk


def button_handler():
    name=tk.filedialog.askopenfilename(filetypes=(("file","*.jpg"),("All Files","*.*") ))
    print(name)


mainwindow=tk.Tk()
mainwindow.geometry("640x340")

b = tk.Button(mainwindow ,text ="browse", command=lambda : button_handler())
b.pack()

mainwindow.mainloop()