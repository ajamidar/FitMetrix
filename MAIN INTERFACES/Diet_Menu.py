import tkinter as tk
from tkinter import PhotoImage
from tkinter import messagebox
from tkinter import *
from PIL import Image, ImageTk
import Main_Menu as MainMenu
import FindDietMenu as FindDietMenu
import SavedDietPage as SavedDiet

#Creating the window.
class App(tk.Tk):
    def __init__(self):

        #main setup
        super().__init__()
        self.title("Diet menu")
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
            MainMenu.App()
        except:
            pass


#Creating the Main frame.
class Main(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.configure(bg="#FFE4E1", highlightbackground="black", highlightthickness=1)
        self.pack(side=tk.LEFT)
        self.propagate(False)
        self.configure(width=800, height=500)

        self.create_labels()
        self.create_buttons()

#Creating the labels.
    def create_labels(self):
        self.main_label = tk.Label(self, text = "Diet plans", bg="#98FB98", fg="#000000", font=("Arial", 40), highlightbackground="black", highlightthickness=1)
        self.main_label.place(relx=.50, rely=.15, anchor=CENTER)

        self.diet_photo=Image.open("C:/Users/iamar/OneDrive/Pictures/A LEVELS/NEA/DIET PHOTO NEA.png")
        self.diet_photo=self.diet_photo.resize((120,120))
        self.diet_photo=ImageTk.PhotoImage(self.diet_photo)
        self.diet_photo_label=tk.Label(self,image=self.diet_photo)
        self.diet_photo_label.place(relx=.50, rely=.50,anchor=CENTER)
        
#Creating the buttons.   
    def create_buttons(self):
        self.find_diet_button = tk.Button(self, text="Find diet plans", bg="#CDC9C9", font=("Arial black", 18), height=3, width=12, command=self.finddiet)
        self.find_diet_button.place(relx=.20, rely=.50,anchor=CENTER)
        self.view_dietplans_button = tk.Button(self, text="View saved\ndiet plan", bg="#CDC9C9", font=("Arial black", 18), height=3, width=12, command=self.saveddiet)
        self.view_dietplans_button.place(relx=.80, rely=.50,anchor=CENTER)

#Opening the find diets menu.
    def finddiet(self):
        try:
            self.master.destroy()
            FindDietMenu.App()
        except:
            pass

#Opening the saved diet menu.    
    def saveddiet(self):
        try:
            self.master.destroy()
            SavedDiet.App()
        except:
            pass