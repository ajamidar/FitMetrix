import tkinter as tk
from tkinter import PhotoImage
from tkinter import messagebox
from tkinter import *
from PIL import Image, ImageTk
import Main_Menu as MainMenu
import YourProgress_Menu as YourProgress
import UpdateProgress as UpdateYourProgress
import Calculations_menu as Calculations

#Creating the window.
class App(tk.Tk):
    def __init__(self):

        #main setup
        super().__init__()
        self.title("Update progress menu")
        self.geometry("800x500")
        self.configure(bg="#B9D3EE")

        #widgets
        self.options=Options(self)
        self.main=Main(self)

        #run
        self.mainloop()

#Creating the Options frame.
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
        self.back_button = tk.Button(self, bg="#8B8989", text="Back", font=("Arial Black", 14), command=self.back)

        #placing widgets
        self.back_button.place(x=45, y=20)

#Creating the back button.
    def back(self):
        try:
            self.master.destroy()
            YourProgress.App()
        except:
            pass

#Creating the Main frame.
class Main(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.configure(bg="#FFFACD", highlightbackground="black", highlightthickness=1)
        self.pack(side=tk.LEFT)
        self.propagate(False)
        self.configure(width=800, height=500)

        self.create_labels()
        self.create_buttons()

#Creating the labels.
    def create_labels(self):
        self.main_label = tk.Label(self, text = "Update your\nprogress", bg="#98FB98", fg="#000000", font=("Arial", 40), highlightbackground="black", highlightthickness=1)
        self.main_label.place(relx=.50, rely=.15, anchor=CENTER)

#Creating the buttons.   
    def create_buttons(self):
        self.update_progress_button = tk.Button(self, text="Upload your\nprogress", bg="#CDC9C9", font=("Arial black", 18), height=3, width=12, command=self.updateProgress)
        self.update_progress_button.place(relx=.25, rely=.50,anchor=CENTER)
        self.calculations_button = tk.Button(self, text="Calculations", bg="#CDC9C9", font=("Arial black", 18), height=3, width=12, command=self.Calculations)
        self.calculations_button.place(relx=.75, rely=.50,anchor=CENTER)

#Opening the update progress page.
    def updateProgress(self):
        try:
            self.master.destroy()
            UpdateYourProgress.App()
        except:
            pass

#Opening the calculations page.  
    def Calculations(self):
        try:
            self.master.destroy()
            Calculations.App()
        except:
            pass