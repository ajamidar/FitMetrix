import tkinter as tk
from tkinter import PhotoImage
from tkinter import messagebox
from tkinter import *
from PIL import Image, ImageTk
import Main_Menu as MainMenu
import UpdateProgress_Menu as UpdateProgress
import Calculate_Bodyfat as Calculate_Bodyfat
import Calculate_BMI as Calculate_BMI


#Creating the window.
class App(tk.Tk):
    def __init__(self):

        #main setup
        super().__init__()
        self.title("Calculations")
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
 
    def back(self):
        try:
            self.master.destroy()
            UpdateProgress.App()
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
        self.main_label = tk.Label(self, text = "Calculations", bg="#98FB98", fg="#000000", font=("Arial", 40), highlightbackground="black", highlightthickness=1)
        self.main_label.place(relx=.50, rely=.15, anchor=CENTER)

        
#Creating the buttons.    
    def create_buttons(self):
        self.bodyfat_button = tk.Button(self, text="Body fat\npercentage", bg="#CDC9C9", font=("Arial black", 18), height=3, width=12, command=self.Bodyfat)
        self.bodyfat_button.place(relx=.25, rely=.50,anchor=CENTER)
        self.BMI_button = tk.Button(self, text="BMI Score", bg="#CDC9C9", font=("Arial black", 18), height=3, width=12, command=self.BMI)
        self.BMI_button.place(relx=.75, rely=.50,anchor=CENTER)

#Opening the bodyfat calculator.
    def Bodyfat(self):
        try:
            self.master.destroy()
            Calculate_Bodyfat.App()
        except:
            pass

#Opening the BMI calculator.    
    def BMI(self):
        try:
            self.master.destroy()
            Calculate_BMI.App()
        except:
            pass