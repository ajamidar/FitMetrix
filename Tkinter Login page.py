import tkinter
from tkinter import messagebox
from tkinter import PhotoImage
from tkinter import *

#Setting up an interface.
window = tkinter.Tk()
window.title("Login interface")
window.geometry("800x500")
window.configure(bg="#C1FFC1")


#Adding login functionality to the interface.
def login():
    username = "johnsmith"
    password = "12345678"
    if username_entry.get()==username and password_entry.get()==password:
        messagebox.showinfo(title="Login Success", message="Successfully logged in.")#messagebox create a pop up message.
        #showinfo - displays info(positive outcome of a process)
        window.destroy()
        import Tkinter_Main_menu
    else:
        messagebox.showerror(title="Login Failure", message="Invalid login credentials")
        username_entry.delete(first=0, last=tkinter.END)
        password_entry.delete(first=0, last=tkinter.END)
        #showerror - displays error(negative outcome of a process)

#Adding registration functionality to the interface.
def register():
    Username_count=[]
    Password_count=[]
    NewUN=username_entry.get()
    NewUN=[*NewUN]#The method - [*NewUN] seperate the input to list of letters, eg: input -> ["i","n","p","u","t"]
    NewPass=password_entry.get()
    NewPass=[*NewPass]
    for x in NewUN:
        Username_count.append(x)
    for i in NewPass:
        Password_count.append(i)
    if len(Username_count)>=5 and len(Username_count)<10 and len(Password_count)>2:
        messagebox.showinfo(title="Registration Success", message="Successfully registered")
    else:
        messagebox.showerror(title="Registration Failure", message="Invalid login credentials")

        
#Defining the Logo.
logo=PhotoImage(file="C:/Users/iamar/OneDrive/Pictures/A LEVELS/NEA/LOGO FITMETRIX.png")       

#Creating a frame
#Frame - box inside the larger interface. For this change the parent from "window" to "Frame", and then place the Frame inside the interface.
Frame = tkinter.Frame(bg="#C1FFC1")


#Creating widgets
login_label = tkinter.Label(Frame, text = "FitMetrix", bg="#FCE6C9", fg="#000000", font=("Arial", 30))#fg = font colour ; font = font("fontType", size)
username_label = tkinter.Label(Frame, text = "Username", bg="#C1FFC1", fg="#000000", font=("Arial", 16))
password_label = tkinter.Label(Frame, text = "Password", bg="#C1FFC1", fg="#000000", font=("Arial", 16))
username_entry = tkinter.Entry(Frame, font=("Calibri", 18))
password_entry = tkinter.Entry(Frame, show = "*", font=("Calibri", 18))
login_button = tkinter.Button(Frame, text = "Login", bg="#A9A9A9", fg="#FFFFFF", font=("Arial", 16), command=login)
register_button = tkinter.Button(Frame, text = "Register", bg="#A9A9A9", fg="#FFFFFF", font=("Arial", 16), command=register)
logo_label = tkinter.Label(Frame, image=logo, bg="#C1FFC1")
#bg = background colour
#command - tells what to do once button is pressed.

#Placing widgets on the screen
login_label.grid(row=0, column=1, columnspan=1, sticky="news", pady=10)
#pad=padding ; pady = change in y-axis ; padx = change in x-axis.
#sticky - a property of the grid where u tell it to take as much space as possible in direction (news=north,east,west,south)
logo_label.grid(row=1, column=1, columnspan=1, sticky="news")
username_label.grid(row=2, column=0)
username_entry.grid(row=2, column=1, pady=10)
password_label.grid(row=3, column=0)
password_entry.grid(row=3, column=1, pady=10)
login_button.grid(row=4, column=0, columnspan=2, pady=20, sticky="n")
register_button.grid(row=4, column=0, columnspan=2, pady=20, sticky="e")

#Placing Frame inside interface.
Frame.place(relx=.5, rely=.5,anchor= CENTER)
Frame.pack()

window.mainloop()