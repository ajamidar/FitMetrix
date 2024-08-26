import tkinter as tk
from tkinter import PhotoImage
from tkinter import messagebox
from tkinter import *
from HashingAlgorithm import *
import Main_Menu as MainMenu
import mySQL as SQL
import UserInfo_Page as UserInfo
import GlobalVariables

#Creating the window.
class Login(tk.Tk):
    def __init__(self):

        #main setup
        super().__init__()
        self.title("Login page")
        self.geometry("800x500")
        self.configure(bg="#C1FFC1")
        
        self.main=Main(self)

        self.mainloop()

#Creating Main frame.
class Main(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.configure(bg="#C1FFC1")
        self.place(relx=.5, rely=.5,anchor= CENTER)
        self.pack()

        self.check_db_existense()
        self.create_widgets()

    def create_widgets(self):
        self.login_label = tk.Label(self, text = "FitMetrix", bg="#FCE6C9", fg="#000000", font=("Arial", 30), highlightbackground="black", highlightthickness=1, highlightcolor="black")#fg = font colour ; font = font("fontType", size)
        self.username_label = tk.Label(self, text = "Username", bg="#C1FFC1", fg="#000000", font=("Arial", 16))
        self.password_label = tk.Label(self, text = "Password", bg="#C1FFC1", fg="#000000", font=("Arial", 16))
        self.username_entry = tk.Entry(self, font=("Calibri", 18))
        self.password_entry = tk.Entry(self, show = "*", font=("Calibri", 18))
        self.login_button = tk.Button(self, text = "Login", bg="#A9A9A9", fg="#FFFFFF", font=("Arial", 16), command=self.login)
        self.register_button = tk.Button(self, text = "Register", bg="#A9A9A9", fg="#FFFFFF", font=("Arial", 16), command=lambda: self.register())
        self.logo=PhotoImage(file="C:/Users/iamar/OneDrive/Pictures/A LEVELS/NEA/LOGO FITMETRIX.png")       
        self.logo_label = tk.Label(self, image=self.logo, bg="#C1FFC1")

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
    
    #Checking database exists or not. If yes, database is opened otherwise database is created and data is added into the database.
    def check_db_existense(self):
        try:
            f = open("credentials_book.db")
        except:
            SQL.create_users()
            SQL.addDietPlan(1,GlobalVariables.diet1)
            SQL.addDietPlan(2,GlobalVariables.diet2)
            SQL.addDietPlan(3,GlobalVariables.diet3)
            SQL.addDietPlan(4,GlobalVariables.diet4)
            SQL.addWorkoutPlan(1,GlobalVariables.workout1)
            SQL.addWorkoutPlan(2,GlobalVariables.workout2)
            SQL.addWorkoutPlan(3,GlobalVariables.workout3)
            SQL.addWorkoutPlan(4,GlobalVariables.workout4)
            SQL.addWorkoutPlan(5,GlobalVariables.workout5) 
            SQL.addWorkoutPlan(6,GlobalVariables.workout6)
            SQL.addWorkoutPlan(7,GlobalVariables.workout7)
            SQL.addWorkoutPlan(8,GlobalVariables.workout8)
            SQL.create_UserDiet()
            SQL.create_UserWorkout()
            SQL.create_UserProfile()

    #Adding login functionality to the interface.
    def login(self):
        hashedpass = SQL.getHashedPassword(self.username_entry.get())
        if self.username_entry.get()==SQL.Username_get2(self.username_entry.get()):
            if int(custom_hash(self.password_entry.get())) == int(hashedpass):
                messagebox.showinfo(title="Login Success", message="Successfully logged in.")#messagebox create a pop up message.
                #showinfo - displays info(positive outcome of a process)
                GlobalVariables.username = self.username_entry.get()

                self.master.destroy()
                MainMenu.App()
            else:
                messagebox.showerror(title="Login Failure", message="Incorrect password")
                #showerror - displays error(negative outcome of a process)
        else:
            messagebox.showerror(title="Login Failure", message="Username does not exist")

    #Adding register functionality to the interface.
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
        if len(Username_count)>=5 and len(Username_count)<=11 and len(Password_count)>2 and len(Password_count)<20:
            if SQL.Username_get(self.username_entry.get()) == []:
                messagebox.showinfo(title="Registration Success", message="Successfully registered\nNow we just need to know a bit more about you.")
                hashedpass=custom_hash(self.password_entry.get())
                SQL.register_users(self.username_entry.get(),hashedpass,"","","","","")
                GlobalVariables.username = self.username_entry.get()

                self.master.destroy()
                UserInfo.App()
            else:
                messagebox.showerror(title="Registration Failure", message="Username exists")
                self.username_entry.delete(first=0, last=END)
                self.password_entry.delete(first=0, last=END)
        else:
            messagebox.showerror(title="Registration Failure", message="Invalid login credentials")        
    
if __name__ == "__main__":
    Login()