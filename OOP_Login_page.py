#This is the code to create a basic tkinter window.
import tkinter
from tkinter import messagebox
from tkinter import PhotoImage
from tkinter import *

#Setting up an interface.
window = tkinter.Tk()
window.title("Login interface")
window.geometry("800x500")
window.configure(bg="#C1FFC1")

class Login:

    def __init__(self, master):
            
        #Defining the Logo.
        self.logo=PhotoImage(file="C:/Users/iamar/OneDrive/Pictures/A LEVELS/NEA/LOGO FITMETRIX.png")       

        #Creating a frame
        #Frame - box inside the larger interface. For this change the parent from "window" to "Frame", and then place the Frame inside the interface.
        Frame = tkinter.Frame(master, bg="#C1FFC1")


        #Creating widgets
        self.login_label = tkinter.Label(Frame, text = "FitMetrix", bg="#FCE6C9", fg="#000000", font=("Arial", 30), highlightbackground="black", highlightthickness=1, highlightcolor="black")#fg = font colour ; font = font("fontType", size)
        self.username_label = tkinter.Label(Frame, text = "Username", bg="#C1FFC1", fg="#000000", font=("Arial", 16))
        self.password_label = tkinter.Label(Frame, text = "Password", bg="#C1FFC1", fg="#000000", font=("Arial", 16))
        self.username_entry = tkinter.Entry(Frame, font=("Calibri", 18))
        self.password_entry = tkinter.Entry(Frame, show = "*", font=("Calibri", 18))
        self.login_button = tkinter.Button(Frame, text = "Login", bg="#A9A9A9", fg="#FFFFFF", font=("Arial", 16), command=self.login)
        self.register_button = tkinter.Button(Frame, text = "Register", bg="#A9A9A9", fg="#FFFFFF", font=("Arial", 16), command=self.register)
        self.logo_label = tkinter.Label(Frame, image=self.logo, bg="#C1FFC1")
        #bg = background colour
        #command - tells what to do once the button is pressed.

        #Placing widgets on the screen
        self.login_label.grid(row=0, column=1, columnspan=1, sticky="news", pady=10)
        #pad=padding ; pady = change in y-axis ; padx = change in x-axis.
        #sticky - a property of the grid where u tell it to take as much space as possible in direction (news=north,east,west,south)
        self.logo_label.grid(row=1, column=1, columnspan=1, sticky="news")
        self.username_label.grid(row=2, column=0)
        self.username_entry.grid(row=2, column=1, pady=10)
        self.password_label.grid(row=3, column=0)
        self.password_entry.grid(row=3, column=1, pady=10)
        self.login_button.grid(row=4, column=0, columnspan=2, pady=20, sticky="n")
        self.register_button.grid(row=4, column=0, columnspan=2, pady=20, sticky="e")

        #Placing Frame inside interface.
        Frame.place(relx=.5, rely=.5,anchor= CENTER)
        Frame.pack()

    #Adding login functionality to the interface.
    def login(self):
        username = "johnsmith"
        password = "12345678"
        if self.username_entry.get()==username and self.password_entry.get()==password:
            messagebox.showinfo(title="Login Success", message="Successfully logged in.")#messagebox create a pop up message.
            #showinfo - displays info(positive outcome of a process)
            window.destroy()
            import OOP_Tkinter_Main_menu
        else:
            messagebox.showerror(title="Login Failure", message="Invalid login credentials")
            #showerror - displays error(negative outcome of a process)

        #Adding registration functionality to the interface.
    def register(self):
        Username_count=[]
        Password_count=[]
        NewUN=self.username_entry.get()
        NewUN=[*NewUN]#The method - [*NewUN] separate the input to list of letters, eg: input -> ["i","n","p","u","t"]
        NewPass=self.password_entry.get()
        NewPass=[*NewPass]
        for x in NewUN:
            Username_count.append(x)
        for i in NewPass:
            Password_count.append(i)
        if len(Username_count)>=5 and len(Username_count)<10 and len(Password_count)>2:
            messagebox.showinfo(title="Registration Success", message="Successfully registered")
        else:
            messagebox.showerror(title="Registration Failure", message="Invalid login credentials")

e = Login(window)

window.mainloop()