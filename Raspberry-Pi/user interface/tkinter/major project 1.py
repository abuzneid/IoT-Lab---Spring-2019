import tkinter as tk
import sqlite3
from tkinter import messagebox



LARGE_FONT= ("Verdana", 12)


class PageChanger(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, CreateUser):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self,parent)
        self.controller = controller

        self.l_title = tk.Label(self, text= " Login Page ", fg="red",font=("Arial",30))
        self.l_title.grid(row=0,column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        self.l_u = tk.Label(self, text="User name", font=LARGE_FONT)
        self.l_u.grid(row=1,column=0,pady=10,padx=10)

        self.u_e = tk.Entry(self)
        self.u_e.grid(row=1, column=1, padx=10,pady=10, sticky="NSEW")

        self.l_p = tk.Label(self, text="Password", font=LARGE_FONT)
        self.l_p.grid(row=2,column=0,pady=10,padx=10)

        self.p_e=tk.Entry(self,show="*")
        self.p_e.grid(row=2, column=1, padx=10,pady=10, sticky="NSEW")

        self.button = tk.Button(self, text="Login",
                                command=lambda: self.button_handler(),highlightbackground='#3E4149')
        self.button.grid(row=3, column=1, padx=10,pady=10, sticky="NSEW")


        b_create_account = tk.Button(self, text="New User",command=lambda:self.controller.show_frame(CreateUser),
                                     highlightbackground='#3E4149')
        b_create_account.grid(row=4, column=1,columnspan=1, padx=10,pady=10, sticky="NSEW")


    def button_handler(self):

        e_u_v = self.u_e.get()
        e_p_v = self.p_e.get()

        conn = sqlite3.connect('login.db')
        cursor = conn.cursor()

        cursor.execute("SELECT username,password FROM login")
        val = cursor.fetchall()

        if len(val) > 1:
            for x in val:
                if e_u_v in x[0] and e_p_v in x[1]:
                    self.controller.show_frame(PageOne)
        else:
            messagebox.showinfo(title=None ,message="Error")


    def data_base(self):
        connect = sqlite3.connect("login.db")
        cursor  = connect.cursor()
        cursor.execute(""" CREATE TABLE IF NOT EXISTS login (username TEXT, password TEXT)""")

        #cursor.execute("""INSERT INTO login (username, password) VALUES (? , ?) """, ("admin", "admin"))

        connect.commit()
        cursor.close()
        connect.close()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="IoT", font=("Arial",32))
        label.grid(row=0,column=0,columnspan=2, pady=10,padx=10,sticky="NSEW")

        b_on=tk.Button(self, text="On",fg="red", highlightbackground='#3E4149', height=3, width=10)
        b_on.grid(row=2, column=0, padx=10, pady=10,sticky="NSEW")

        b_off=tk.Button(self, text="off", fg="red", highlightbackground='#3E4149', height=3, width=10)
        b_off.grid(row=2, column=1, padx=10, pady=10,sticky="NSEW")


        button1 = tk.Button(self,text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.grid(row=4,column=1 ,padx=10, pady=10,sticky="NSEW")


class CreateUser(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller=controller

        self.label = tk.Label(self, text="New User", font=("Arial",30))
        self.label.grid(row=0,column=1,pady=10,padx=2)

        self.l_username = tk.Label(self, text= "Username")
        self.l_username.grid(row=1, column=0, padx=10, pady=10,sticky="nsew")

        self.e_user_name=tk.Entry(self)
        self.e_user_name.grid(row=1, column=1, padx=10, pady=2,sticky="nsew")

        self.l_pass = tk.Label(self, text="Password")
        self.l_pass.grid(row=2,column=0, padx=2, pady=10,sticky="nsew")

        self.e_pas =tk.Entry(self)
        self.e_pas.grid(row=2, column=1, padx=2, pady=10,sticky="nsew")

        self.button1 = tk.Button(self, text="submit",
                                 command=lambda : self.button_handler_submit())
        self.button1.grid(row=3,column=1, padx=10, pady=10,sticky="nsew")


    def button_handler_submit(self):

        e_user_name_v = self.e_user_name.get()
        e_pas_v = self.e_pas.get()
        print(e_pas_v)


        conn = sqlite3.connect("login.db")
        cursor = conn.cursor()

        #cursor.execute("""CREATE TABLE IF NOT EXIST login (username TEXT,password TEXT) """)

        cursor.execute(""" INSERT INTO login (username, password) VALUES  (?,?)""",(e_user_name_v,e_pas_v))

        conn.commit()
        cursor.close()
        conn.close()

        messagebox.showinfo(title="Added User on DataBase",message="user {}  and password {} created ".format(e_user_name_v,e_pas_v))
        self.controller.show_frame(StartPage)



app = PageChanger()
app.mainloop()
