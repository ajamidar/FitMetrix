import tkinter as tk
from tkinter import *
from tkinter import messagebox
import FindDietMenu as FindDietMenu
import GlobalVariables
import mySQL as SQL
import SavedDietPage as SavedDietPage

#Creating the window.
class App(tk.Tk):
    def __init__(self):

        #main setup
        super().__init__()
        self.title("Diets page")
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
            FindDietMenu.App()
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

        if GlobalVariables.dietLevel == 18:
            GlobalVariables.diet1Text = SQL.getDietPlan(1)
            GlobalVariables.diet1ID = 1
            GlobalVariables.diet2Text = SQL.getDietPlan(2)
            GlobalVariables.diet2ID = 2
        elif GlobalVariables.dietLevel == 17:
            GlobalVariables.diet1Text = SQL.getDietPlan(1)
            GlobalVariables.diet1ID = 1
            GlobalVariables.diet2Text = SQL.getDietPlan(2)
            GlobalVariables.diet2ID = 2
        elif GlobalVariables.dietLevel == 12:
            GlobalVariables.diet1Text = SQL.getDietPlan(3)
            GlobalVariables.diet1ID = 3           
            GlobalVariables.diet2Text = SQL.getDietPlan(4)
            GlobalVariables.diet2ID = 4
        elif GlobalVariables.dietLevel == 16:
            GlobalVariables.diet1Text = SQL.getDietPlan(3)
            GlobalVariables.diet1ID = 3           
            GlobalVariables.diet2Text = SQL.getDietPlan(4)
            GlobalVariables.diet2ID = 4
        elif GlobalVariables.dietLevel == 15:
            GlobalVariables.diet1Text = SQL.getDietPlan(3)
            GlobalVariables.diet1ID = 3           
            GlobalVariables.diet2Text = SQL.getDietPlan(4)
            GlobalVariables.diet2ID = 4
        elif GlobalVariables.dietLevel == 14:
            GlobalVariables.diet1Text = SQL.getDietPlan(3)
            GlobalVariables.diet1ID = 3           
            GlobalVariables.diet2Text = SQL.getDietPlan(4)
            GlobalVariables.diet2ID = 4
        elif GlobalVariables.dietLevel == 13:
            GlobalVariables.diet1Text = SQL.getDietPlan(3)
            GlobalVariables.diet1ID = 3           
            GlobalVariables.diet2Text = SQL.getDietPlan(4)
            GlobalVariables.diet2ID = 4
        elif GlobalVariables.dietLevel == 11:
            GlobalVariables.diet1Text = SQL.getDietPlan(3)
            GlobalVariables.diet1ID = 3           
            GlobalVariables.diet2Text = SQL.getDietPlan(4)
            GlobalVariables.diet2ID = 4
        elif GlobalVariables.dietLevel == 10:
            GlobalVariables.diet1Text = SQL.getDietPlan(3)
            GlobalVariables.diet1ID = 3           
            GlobalVariables.diet2Text = SQL.getDietPlan(4)
            GlobalVariables.diet2ID = 4
        elif GlobalVariables.dietLevel == 9:
            GlobalVariables.diet1Text = SQL.getDietPlan(3)
            GlobalVariables.diet1ID = 3           
            GlobalVariables.diet2Text = SQL.getDietPlan(4)
            GlobalVariables.diet2ID = 4
        elif GlobalVariables.dietLevel == 8:
            GlobalVariables.diet1Text = SQL.getDietPlan(3)
            GlobalVariables.diet1ID = 3           
            GlobalVariables.diet2Text = SQL.getDietPlan(4)
            GlobalVariables.diet2ID = 4
        elif GlobalVariables.dietLevel == 7:
            GlobalVariables.diet1Text = SQL.getDietPlan(3)
            GlobalVariables.diet1ID = 3           
            GlobalVariables.diet2Text = SQL.getDietPlan(4)
            GlobalVariables.diet2ID = 4
        elif GlobalVariables.dietLevel == 6:
            GlobalVariables.diet1Text = SQL.getDietPlan(3)
            GlobalVariables.diet1ID = 3           
            GlobalVariables.diet2Text = SQL.getDietPlan(4)
            GlobalVariables.diet2ID = 4
        elif GlobalVariables.dietLevel == 5:
            GlobalVariables.diet1Text = SQL.getDietPlan(3)
            GlobalVariables.diet1ID = 3           
            GlobalVariables.diet2Text = SQL.getDietPlan(4)
            GlobalVariables.diet2ID = 4
        elif GlobalVariables.dietLevel == 4:
            GlobalVariables.diet1Text = SQL.getDietPlan(3)
            GlobalVariables.diet1ID = 3           
            GlobalVariables.diet2Text = SQL.getDietPlan(4)
            GlobalVariables.diet2ID = 4
        elif GlobalVariables.dietLevel == 3:
            GlobalVariables.diet1Text = SQL.getDietPlan(3)
            GlobalVariables.diet1ID = 3           
            GlobalVariables.diet2Text = SQL.getDietPlan(4)
            GlobalVariables.diet2ID = 4
        elif GlobalVariables.dietLevel == 2:
            GlobalVariables.diet1Text = SQL.getDietPlan(3)
            GlobalVariables.diet1ID = 3           
            GlobalVariables.diet2Text = SQL.getDietPlan(4)
            GlobalVariables.diet2ID = 4
        elif GlobalVariables.dietLevel == 1:
            GlobalVariables.diet1Text = SQL.getDietPlan(3)
            GlobalVariables.diet1ID = 3           
            GlobalVariables.diet2Text = SQL.getDietPlan(4)
            GlobalVariables.diet2ID = 4
        

        self.opt1_label = tk.Label(self, text = "Option 1", bg="#98FB98", fg="#000000", font=("Arial", 35), highlightbackground="black", highlightthickness=1)
        self.opt1_label.place(relx=.275, rely=.100, anchor=CENTER)
            
        self.opt2_label = tk.Label(self, text = "Option 2", bg="#98FB98", fg="#000000", font=("Arial", 35), highlightbackground="black", highlightthickness=1)
        self.opt2_label.place(relx=.715, rely=.100, anchor=CENTER)

        self.diet1_label = tk.Label(self, text=GlobalVariables.diet1Text, bg="#FFFFFF", font=("Arial black", 6), height=20, width=45,highlightbackground="black", highlightthickness=1)
        self.diet1_label.place(relx=.260, rely=.540,anchor=CENTER)
        self.diet2_label = tk.Label(self, text=GlobalVariables.diet2Text, bg="#FFFFFF", font=("Arial black", 6), height=20, width=45,highlightbackground="black", highlightthickness=1)
        self.diet2_label.place(relx=.730, rely=.540,anchor=CENTER)

#Creating the buttons.    
    def create_buttons(self):
        self.save1_button = tk.Button(self, text = "Save", bg="#C0C0C0",font=("Arial black", 10), height=1, width=5,highlightbackground="black", highlightthickness=1,command=self.saveDiet1)
        self.save1_button.place(relx=.260, rely= .935, anchor=CENTER)

        self.save2_button = tk.Button(self, text = "Save", bg="#C0C0C0",font=("Arial black", 10), height=1, width=5,highlightbackground="black", highlightthickness=1,command=self.saveDiet2)
        self.save2_button.place(relx=.730, rely= .935, anchor=CENTER)

#Saving the diet presented as Option 1.
    def saveDiet1(self):
        SQL.addDietID(GlobalVariables.username,GlobalVariables.diet1ID)
        messagebox.showinfo(title="Diet Saved", message="Your diet has been saved\nTo save a different diet\nmake sure to delete the saved diet first.")
        self.master.destroy()
        SavedDietPage.App()

#Saving the diet presented as Option 2.
    def saveDiet2(self):
        SQL.addDietID(GlobalVariables.username,GlobalVariables.diet2ID)
        messagebox.showinfo(title="Diet Saved", message="Your diet has been saved\nTo save a different diet\nmake sure to delete the saved diet first.")        
        self.master.destroy()
        SavedDietPage.App()