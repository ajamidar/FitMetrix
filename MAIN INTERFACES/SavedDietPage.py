import tkinter as tk
from tkinter import *
import Diet_Menu as DietMenu
import GlobalVariables
import mySQL as SQL

#Creating the window.
class App(tk.Tk):
    def __init__(self):

        #main setup
        super().__init__()
        self.title("Saved diet")
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
            DietMenu.App()
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

        GlobalVariables.SavedDiet = SQL.getSavedDietPlan(GlobalVariables.username)

        self.main_label = tk.Label(self, text = "Saved diet plan", bg="#98FB98", fg="#000000", font=("Arial", 30), highlightbackground="black", highlightthickness=1)
        self.main_label.place(relx=.5, rely=.100, anchor=CENTER)         

        self.diet_label = tk.Label(self, text=GlobalVariables.SavedDiet, bg="#FFFFFF", font=("Arial black", 6), height=20, width=45,highlightbackground="black", highlightthickness=1)
        self.diet_label.place(relx=.5, rely=.500,anchor=CENTER)

#Creating the delete button.   
    def create_buttons(self):
        self.delete_button = tk.Button(self, text = "Delete", bg="#FF0000",font=("Arial black", 10), height=1, width=5,highlightbackground="black", highlightthickness=1, command=self.deleteDiet)
        self.delete_button.place(relx=.5, rely= .825, anchor=CENTER)

#Deleting the saved diet.   
    def deleteDiet(self):
        SQL.deleteSavedDiet(GlobalVariables.username)
        self.diet_label.destroy()