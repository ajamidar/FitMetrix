import tkinter as tk
from tkinter import *
from tkinter import messagebox
import FindWorkoutMenu as FindWorkoutMenu
import GlobalVariables
import mySQL as SQL
import SavedWorkoutPage as SavedWorkoutPage

#Creating the window.
class App(tk.Tk):
    def __init__(self):

        #main setup
        super().__init__()
        self.title("Workouts page")
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
            FindWorkoutMenu.App()
        except:
            pass


#Creating the Main frame.
class Main(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.configure(bg="#98F5FF", highlightbackground="black", highlightthickness=1)
        self.pack(side=tk.LEFT)
        self.propagate(False)
        self.configure(width=800, height=500)

        self.create_labels()
        self.create_buttons()

#Creating the labels.
    def create_labels(self):

        if GlobalVariables.workoutLevel == 20:
            GlobalVariables.workout1Text = SQL.getWorkoutPlan(5)
            GlobalVariables.workout1ID = 5
            GlobalVariables.workout2Text = SQL.getWorkoutPlan(6)
            GlobalVariables.workout2ID = 6
        elif GlobalVariables.workoutLevel == 18:
            GlobalVariables.workout1Text = SQL.getWorkoutPlan(3)
            GlobalVariables.workout1ID = 3
            GlobalVariables.workout2Text = SQL.getWorkoutPlan(4)
            GlobalVariables.workout2ID = 4
        elif GlobalVariables.workoutLevel == 16:
            GlobalVariables.workout1Text = SQL.getWorkoutPlan(1)
            GlobalVariables.workout1ID = 1
            GlobalVariables.workout2Text = SQL.getWorkoutPlan(7)
            GlobalVariables.workout2ID = 7
        elif GlobalVariables.workoutLevel == 14:
            GlobalVariables.workout1Text = SQL.getWorkoutPlan(2)
            GlobalVariables.workout1ID = 2
            GlobalVariables.workout2Text = SQL.getWorkoutPlan(8)
            GlobalVariables.workout2ID = 8
        elif GlobalVariables.workoutLevel == 12:
            GlobalVariables.workout1Text = SQL.getWorkoutPlan(2)
            GlobalVariables.workout1ID = 2
            GlobalVariables.workout2Text = SQL.getWorkoutPlan(8)
            GlobalVariables.workout2ID = 8
        elif GlobalVariables.workoutLevel == 10:
            GlobalVariables.workout1Text = SQL.getWorkoutPlan(2)
            GlobalVariables.workout1ID = 2
            GlobalVariables.workout2Text = SQL.getWorkoutPlan(8)
            GlobalVariables.workout2ID = 8
        elif GlobalVariables.workoutLevel == 8:
            GlobalVariables.workout1Text = SQL.getWorkoutPlan(2)
            GlobalVariables.workout1ID = 2
            GlobalVariables.workout2Text = SQL.getWorkoutPlan(8)
            GlobalVariables.workout2ID = 8           
        elif GlobalVariables.workoutLevel == 6:
            GlobalVariables.workout1Text = SQL.getWorkoutPlan(2)
            GlobalVariables.workout1ID = 2
            GlobalVariables.workout2Text = SQL.getWorkoutPlan(8)
            GlobalVariables.workout2ID = 8
        elif GlobalVariables.workoutLevel == 4:
            GlobalVariables.workout1Text = SQL.getWorkoutPlan(2)
            GlobalVariables.workout1ID = 2
            GlobalVariables.workout2Text = SQL.getWorkoutPlan(8)
            GlobalVariables.workout2ID = 8
        elif GlobalVariables.workoutLevel == 2:
            GlobalVariables.workout1Text = SQL.getWorkoutPlan(2)
            GlobalVariables.workout1ID = 2
            GlobalVariables.workout2Text = SQL.getWorkoutPlan(8)
            GlobalVariables.workout2ID = 8

        self.opt1_label = tk.Label(self, text = "Option 1", bg="#98FB98", fg="#000000", font=("Arial", 35), highlightbackground="black", highlightthickness=1)
        self.opt1_label.place(relx=.275, rely=.100, anchor=CENTER)
            
        self.opt2_label = tk.Label(self, text = "Option 2", bg="#98FB98", fg="#000000", font=("Arial", 35), highlightbackground="black", highlightthickness=1)
        self.opt2_label.place(relx=.715, rely=.100, anchor=CENTER)

        self.workout1_label = tk.Label(self, text=GlobalVariables.workout1Text, bg="#FFFFFF", font=("Arial black", 6), height=30, width=47,highlightbackground="black", highlightthickness=1)
        self.workout1_label.place(relx=.260, rely=.540,anchor=CENTER)
        self.workout2_label = tk.Label(self, text=GlobalVariables.workout2Text, bg="#FFFFFF", font=("Arial black", 6), height=30, width=47,highlightbackground="black", highlightthickness=1)
        self.workout2_label.place(relx=.730, rely=.540,anchor=CENTER)

#Creating the buttons.   
    def create_buttons(self):
        self.save1_button = tk.Button(self, text = "Save", bg="#C0C0C0",font=("Arial black", 10), height=1, width=5,highlightbackground="black", highlightthickness=1,command=self.saveworkout1)
        self.save1_button.place(relx=.260, rely= .935, anchor=CENTER)

        self.save2_button = tk.Button(self, text = "Save", bg="#C0C0C0",font=("Arial black", 10), height=1, width=5,highlightbackground="black", highlightthickness=1,command=self.saveworkout2)
        self.save2_button.place(relx=.730, rely= .935, anchor=CENTER)

#Saving the workout presented as Option 1.
    def saveworkout1(self):
        messagebox.showinfo(title="Workout Saved", message="Your workout has been saved\nTo save a different workout\nmake sure to delete the saved workout first.")
        SQL.addWorkoutID(GlobalVariables.username,GlobalVariables.workout1ID)        
        self.master.destroy()
        SavedWorkoutPage.App()

#Saving the workout presented as Option 2.   
    def saveworkout2(self):
        messagebox.showinfo(title="Workout Saved", message="Your workout has been saved\nTo save a different workout\nmake sure to delete the saved workout first.")        
        SQL.addWorkoutID(GlobalVariables.username,GlobalVariables.workout2ID)
        self.master.destroy()
        SavedWorkoutPage.App()

