import tkinter as tk
from tkinter import PhotoImage
from tkinter import messagebox
from tkinter import *
import Login_Page as Login
import Workout_Menu as Workout
import Diet_Menu as DietMenu
import YourDetails_Page as YourDetails
import YourProgress_Menu as YourProgress


#Creating the window.
class App(tk.Tk):
    def __init__(self):

        #main setup
        super().__init__()
        self.title("Main menu")
        self.geometry("800x500")
        self.configure(bg="#B9D3EE")

        #widgets
        self.options=Options(self)
        self.main=Main(self)

        #run
        self.mainloop()

#Creating Options Frame.
class Options(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.configure(bg="#CDC9C9", highlightbackground="black", highlightthickness=1)
        self.pack(side=tk.LEFT)
        self.pack_propagate(False)
        self.configure(width=170, height=500)

        self.create_widgets()

    def create_widgets(self):
        #creating widgets
        self.logout_button = tk.Button(self, bg="#8B8989", text="Logout", font=("Arial Black", 14), command=self.logout)
        self.yourdetails_button = tk.Button(self, bg="#8B8989", text="Your details", font=("Arial Black", 14), command=self.yourdetails)
        
        #placing widgets
        self.logout_button.place(x=35, y=20)
        self.yourdetails_button.place(x=10, y=425)

    def logout(self):
        messagebox.showinfo(title="Logout", message="Successfully logged out")
        try:
            self.master.destroy()
            Login.Login()
        except:
            pass

    def yourdetails(self):
        try:
            self.master.destroy()
            YourDetails.App()
        except:
            pass

#Creating Main frame.
class Main(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.configure(bg="#B9D3EE", highlightbackground="black", highlightthickness=1)
        self.pack(side=tk.LEFT)
        self.propagate(False)
        self.configure(width=800, height=500)

        self.create_labels()
        self.create_buttons()

#Creating the labels.
    def create_labels(self):
        self.logo=PhotoImage(file="C:/Users/iamar/OneDrive/Pictures/A LEVELS/NEA/LOGO FITMETRIX BLUE.png") 
        self.main_label = tk.Label(self, text = "FitMetrix", bg="#FCE6C9", fg="#000000", font=("Arial", 30), highlightbackground="black", highlightthickness=1)
        self.main_label.place(relx=.47, rely=.1, anchor=CENTER)
        self.logo_label = tk.Label(self, image=self.logo, bg="#B9D3EE")
        self.logo_label.place(relx=.47, rely=.28,anchor=CENTER)

#Creating the buttons.    
    def create_buttons(self):
        self.diet_button = tk.Button(self, text="Diet plans", bg="#CDC9C9", font=("Arial black", 18), height=3, command=self.dietplans)
        self.diet_button.place(relx=.15, rely=.55,anchor=CENTER)
        self.workout_button = tk.Button(self, text="Workout plans", bg="#CDC9C9", font=("Arial black", 18), height=3, command=self.workoutplans)
        self.workout_button.place(relx=.465, rely=.55,anchor=CENTER)
        self.progress_button = tk.Button(self, text="Your progress", bg="#CDC9C9", font=("Arial black", 18), height=3, command=self.progress)
        self.progress_button.place(relx=.82, rely=.55,anchor=CENTER)

#Opening diet menu.
    def dietplans(self):
        try:
            self.master.destroy()
            DietMenu.App()
        except:
            pass

#Opening workout menu.
    def workoutplans(self):
        try:
            self.master.destroy()
            Workout.App()
        except:
            pass

#Opening your progress menu.
    def progress(self):
        try:
            self.master.destroy()
            YourProgress.App()
        except:
            pass
