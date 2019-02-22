import tkinter as tk
from tkinter import messagebox

LARGE_FONT= ("Verdana", 12)
global food
food = []

class PageChanger(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne):

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

        self.my_label=tk.Label(self, text="Interview Test Solution",font=("arial",24))
        self.my_label.grid(row=0,column=0,pady=10,padx=10,sticky="nsew")

        self.l_u = tk.Label(self, text="User name", font=LARGE_FONT)
        self.l_u.grid(row=1,column=0,pady=10,padx=10)

        self.u_e = tk.Entry(self)
        self.u_e.grid(row=1, column=1, padx=10,pady=10, sticky="NSEW")

        self.l_p = tk.Label(self, text="Password", font=LARGE_FONT)
        self.l_p.grid(row=2,column=0,pady=10,padx=10)

        self.p_e=tk.Entry(self)
        self.p_e.grid(row=2, column=1, padx=10,pady=10, sticky="NSEW")

        self.button = tk.Button(self, text="Login",
                                command=lambda: self.button_handler())
        self.button.grid(row=3, column=1)

    def button_handler(self):

        e_u_v = self.u_e.get()
        e_p_v = self.p_e.get()
        print(e_p_v)
        print(e_u_v)

        if e_u_v == "admin" and e_p_v == "admin":
            self.controller.show_frame(PageOne)


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.label_title = tk.Label(self, text="enter name and food seperated by comma", font=LARGE_FONT)
        self.label_title.grid(row=0,column=0,pady=10,padx=10)


        self.label = tk.Label(self, text="enter name", font=LARGE_FONT)
        self.label.grid(row=1,column=0,pady=10,padx=10)


        self.user_name=tk.Entry(self)
        self.user_name.grid(row=1, column=1, pady=10, padx=10, sticky="nsew")


        self.button_user = tk.Button(self, text="submit", command=lambda : self.button_handler_user())
        self.button_user.grid(row=1,column=2,pady=10,padx=10,sticky="nsew")



        self.label_food = tk.Label(self, text="enter food", font=LARGE_FONT)
        self.label_food.grid(row=2,column=0,pady=10,padx=10)


        self.food = tk.Entry(self)
        self.food.grid(row=2,column=1,pady=10,padx=10,sticky="nsew")

        self.button_food = tk.Button(self, text="submit", command=lambda : self.button_handler_food())
        self.button_food.grid(row=2,column=2,pady=10,padx=10,sticky="nsew")



        self.user_list = []
        self.user_food = []


    def button_handler_user(self):

        user_name_value = self.user_name.get()

        if len(user_name_value) > 0:
            self.user_list.append(user_name_value)
            print(self.user_list)
        else:
            messagebox.showinfo(title="enter value ", text="enter value")



    def button_handler_food(self):

        user_food_value = self.food.get()

        if len(user_food_value) > 0:
            self.user_food.append(user_food_value)
            print(self.user_food)
        else:
            messagebox.showinfo(title="enter value ", text="enter value")



app = PageChanger()
app.mainloop()