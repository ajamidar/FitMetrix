import tkinter as tk
from tkinter import PhotoImage
from tkinter import messagebox
from tkinter import *
from PIL import Image, ImageTk
import Workout_Menu as WorkoutMenu
import GlobalVariables
import ShowWorkoutsPage as ShowWorkoutsPage

#Creating the window.
class App(tk.Tk):
    def __init__(self):

        #main setup
        super().__init__()
        self.title("Find workouts menu")
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
            WorkoutMenu.App()
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
        self.create_dropList()
        self.create_entries()
        self.create_button()

#Creating the labels.
    def create_labels(self):
        self.main_label = tk.Label(self, text = "Your requirements", bg="#98FB98", fg="#000000", font=("Arial", 25), highlightbackground="black", highlightthickness=1)
        self.main_label.place(relx=.59, rely=.1, anchor=CENTER)

        self.goal_label=tk.Label(self, text="Select goal", bg="#98F5FF")
        self.goal_label.place(relx=.17, rely=0.225)

        self.height_label=tk.Label(self, text="Height(cm)", bg="#98F5FF")
        self.height_label.place(relx=0.19,rely=0.345)

        self.weight_label=tk.Label(self, text="Weight(kg)", bg="#98F5FF")
        self.weight_label.place(relx=0.19,rely=0.453)

        self.age_label=tk.Label(self, text="Age", bg="#98F5FF")
        self.age_label.place(relx=0.2,rely=0.56)

        self.preference_label=tk.Label(self, text="Activity\nlevel", bg="#98F5FF")
        self.preference_label.place(relx=0.19, rely=0.66)

#Creating the drop down lists.    
    def create_dropList(self):
        self.goal_options=["Cut","Bulk","Body recomposition"]
        self.clicked_goal=StringVar()
        self.clicked_goal.set("Select a goal")
        self.goal_drop=OptionMenu(self, self.clicked_goal, *self.goal_options)
        self.goal_drop.config(width=50)
        self.goal_drop.place(relx=.6, rely=0.25, anchor=CENTER)

        self.preference_options=["2-3 days a week","3-4 days a week","5-6 days a week"]
        self.clicked_preference=StringVar()
        self.clicked_preference.set("Select a goal")
        self.activity_drop=OptionMenu(self, self.clicked_preference, *self.preference_options)
        self.activity_drop.config(width=50)
        self.activity_drop.place(relx=.6, rely=0.7, anchor=CENTER)

#Creating the entries.
    def create_entries(self):
        self.height=tk.Entry(self, font=("Calibri",18))
        self.height.config(width=28)
        self.height.place(relx=.328, rely=0.335)

        self.weight=tk.Entry(self, font=("Calibri",18))
        self.weight.config(width=28)
        self.weight.place(relx=.328, rely=0.445)

        self.age=tk.Entry(self, font=("Calibri",18))
        self.age.config(width=28)
        self.age.place(relx=.328, rely=0.555)

#Creating the submit button.
    def create_button(self):
        submit=tk.Button(self, text="Submit", font=("Calibri", 12), command=self.info)
        submit.place(relx=0.5, rely=0.8)

#Implementing the info function which sets workout level based on the user's input.
    def info(self):
        try:
            if int(self.age.get())>15 and int(self.age.get())<60:
                if self.clicked_goal.get() == "Cut":
                    if self.clicked_preference.get() == "2-3 days a week":

                            GlobalVariables.workoutLevel = 18

                    elif self.clicked_preference.get() == "3-4 days a week":

                            GlobalVariables.workoutLevel = 16

                    elif self.clicked_preference.get() == "5-6 days a week":

                            GlobalVariables.workoutLevel = 14

                elif self.clicked_goal.get() == "Bulk":
                    if self.clicked_preference.get() == "2-3 days a week":

                            GlobalVariables.workoutLevel = 12

                    elif self.clicked_preference.get() == "3-4 days a week":

                            GlobalVariables.workoutLevel = 10

                    elif self.clicked_preference.get() == "5-6 days a week":

                            GlobalVariables.workoutLevel = 8

                elif self.clicked_goal.get() == "Body recomposition":
                    if self.clicked_preference.get() == "2-3 days a week":

                            GlobalVariables.workoutLevel = 6

                    elif self.clicked_preference.get() == "3-4 days a week":

                            GlobalVariables.workoutLevel = 4
                            
                    elif self.clicked_preference.get() == "5-6 days a week":

                            GlobalVariables.workoutLevel = 2
            elif int(self.age.get())<15 and int(self.age.get())>60:
                GlobalVariables.workoutLevel = 20
                messagebox.showwarning(title="Notice", message="As you fall into the sensitive age group of our guidelines,\nwe advise you to only follow our plan for a maximum of 3 days.")
            
            self.master.destroy()
            ShowWorkoutsPage.App()

        except:
             messagebox.showerror(title="Error",message="Invalid inputs")