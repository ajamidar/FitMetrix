import tkinter as tk
from tkinter import *
import Diet_Menu as DietMenu
import GlobalVariables
from tkinter import messagebox
import ShowDietsPage as ShowDiets

#Creating the window.
class App(tk.Tk):
    def __init__(self):

        #main setup
        super().__init__()
        self.title("Find diets menu")
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
#Creating the back buttons.
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
        self.create_dropList()
        self.create_entries()
        self.create_button()

#Creating the labels.
    def create_labels(self):
        self.main_label = tk.Label(self, text = "Your requirements", bg="#98FB98", fg="#000000", font=("Arial", 25), highlightbackground="black", highlightthickness=1)
        self.main_label.place(relx=.59, rely=.1, anchor=CENTER)

        self.goal_label=tk.Label(self, text="Select goal", bg="#FFE4E1")
        self.goal_label.place(relx=.17, rely=0.225)

        self.height_label=tk.Label(self, text="Height(cm)", bg="#FFE4E1")
        self.height_label.place(relx=0.19,rely=0.345)

        self.weight_label=tk.Label(self, text="Weight(kg)", bg="#FFE4E1")
        self.weight_label.place(relx=0.19,rely=0.453)

        self.age_label=tk.Label(self, text="Age", bg="#FFE4E1")
        self.age_label.place(relx=0.2,rely=0.56)

        self.preference_label=tk.Label(self, text="Dietary\npreference", bg="#FFE4E1")
        self.preference_label.place(relx=0.17, rely=0.66)

#Creating the drop-down list.    
    def create_dropList(self):
        self.goal_options=["Cut","Bulk","Body recomposition"]
        self.clicked_goal=StringVar()
        self.clicked_goal.set("Select a goal")
        self.goal_drop=OptionMenu(self, self.clicked_goal, *self.goal_options)
        self.goal_drop.config(width=50)
        self.goal_drop.place(relx=.6, rely=0.25, anchor=CENTER)

        self.preference_options=["Vegetarian","Non-vegetarian","Vegan"]
        self.clicked_preference=StringVar()
        self.clicked_preference.set("Select a goal")
        self.preference_drop=OptionMenu(self, self.clicked_preference, *self.preference_options)
        self.preference_drop.config(width=50)
        self.preference_drop.place(relx=.6, rely=0.7, anchor=CENTER)
 
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
        self.submit=tk.Button(self, text="Submit", font=("Calibri", 12), command=self.info)
        self.submit.place(relx=0.5, rely=0.8)

#Implementing the info function to set diet levels based on the user's inputs.
    def info(self):
        try:
            if self.clicked_goal.get() == "Cut":
                if self.clicked_preference.get() == "Non-vegetarian":
                    if int(self.height.get())>=170 and int(self.weight.get())>=70 and int(self.age.get())>=15:
                        GlobalVariables.dietLevel = 18
                    else:
                        GlobalVariables.dietLevel = 17
                elif self.clicked_preference.get() == "Vegetarian":
                    if int(self.height.get())>=170 and int(self.weight.get())>=70 and int(self.age.get())>=15:
                        GlobalVariables.dietLevel = 16
                    else:
                        GlobalVariables.dietLevel = 15
                elif self.clicked_preference.get() == "Vegan":
                    if int(self.height.get())>=170 and int(self.weight.get())>=70 and int(self.age.get())>=15:
                        GlobalVariables.dietLevel = 14
                    else:
                        GlobalVariables.dietLevel = 13 

            elif self.clicked_goal.get() == "Bulk":
                if self.clicked_preference.get() == "Non-vegetarian":
                    if int(self.height.get())>=170 and int(self.weight.get())>=65 and int(self.age.get())>=15:
                        GlobalVariables.dietLevel = 12
                    else:
                        GlobalVariables.dietLevel = 12
                elif self.clicked_preference.get() == "Vegetarian":
                    if int(self.height.get())>=170 and int(self.weight.get())>=70 and int(self.age.get())>=15:
                        GlobalVariables.dietLevel = 10
                    else:
                        GlobalVariables.dietLevel = 9
                elif self.clicked_preference.get() == "Vegan":
                    if int(self.height.get())>=170 and int(self.weight.get())>=70 and int(self.age.get())>=15:
                        GlobalVariables.dietLevel = 8
                    else:
                        GlobalVariables.dietLevel = 7

            elif self.clicked_goal.get() == "Body recomposition":
                if self.clicked_preference.get() == "Non-vegetarian":
                    if int(self.height.get())>=170 and int(self.weight.get())>=70 and int(self.age.get())>=15:
                        GlobalVariables.dietLevel = 6
                    else:
                        GlobalVariables.dietLevel = 5
                elif self.clicked_preference.get() == "Vegetarian":
                    if int(self.height.get())>=170 and int(self.weight.get())>=70 and int(self.age.get())>=15:
                        GlobalVariables.dietLevel = 4
                    else:
                        GlobalVariables.dietLevel = 3
                elif self.clicked_preference.get() == "Vegan":
                    if int(self.height.get())>=170 and int(self.weight.get())>=70 and int(self.age.get())>=15:
                        GlobalVariables.dietLevel = 2
                    else:
                        GlobalVariables.dietLevel = 1
            self.master.destroy()
            ShowDiets.App()
        except:
            messagebox.showerror(title="Invalid",message="Invalid inputs")