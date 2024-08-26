import tkinter as tk
from tkinter import PhotoImage
from tkinter import messagebox
from tkinter import *
from PIL import Image, ImageTk
import Main_Menu as MainMenu
import Login_Page as LoginPage
import mySQL as SQL
from HashingAlgorithm import *
import GlobalVariables

#Creating the window.
class App(tk.Tk):
    def __init__(self):

        #main setup
        super().__init__()
        self.title("User Info")
        self.geometry("800x500")
        self.configure(bg="#B9D3EE")

        #widgets
        self.options=Options(self)
        self.main=Main(self)

        #run
        self.mainloop()

#Creating the Options menu.    
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
        self.create_dropList()
        self.create_entries()
        self.create_button()

#Creating the labels.
    def create_labels(self):
        self.main_label = tk.Label(self, text = "Your information", bg="#98FB98", fg="#000000", font=("Arial", 25), highlightbackground="black", highlightthickness=1)
        self.main_label.place(relx=.53, rely=.1, anchor=CENTER)

        self.name_label=tk.Label(self, text="Name", bg="#FFE4E1")
        self.name_label.place(relx=0.19,rely=0.240)

        self.height_label=tk.Label(self, text="Height(cm)", bg="#FFE4E1")
        self.height_label.place(relx=0.19,rely=0.345)

        self.weight_label=tk.Label(self, text="Weight(kg)", bg="#FFE4E1")
        self.weight_label.place(relx=0.19,rely=0.453)

        self.age_label=tk.Label(self, text="Age", bg="#FFE4E1")
        self.age_label.place(relx=0.2,rely=0.56)

        self.gender_label=tk.Label(self, text="Gender", bg="#FFE4E1")
        self.gender_label.place(relx=0.19, rely=0.68)

#Creating the drop-down list.    
    def create_dropList(self):

        self.gender_options=["Male","Female"]
        self.clicked_gender=StringVar()
        self.clicked_gender.set("Select gender")
        self.preference_drop=OptionMenu(self, self.clicked_gender, *self.gender_options)
        self.preference_drop.config(width=50)
        self.preference_drop.place(relx=.6, rely=0.7, anchor=CENTER)


#Creating the entries.
    def create_entries(self):

        self.name=tk.Entry(self,font=("Calibri",18))
        self.name.config(width=28)
        self.name.place(relx=.328, rely=0.235)

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

#Implementing the info function which saves a user's detials when they register onto the program.   
    def info(self):

        self.username = GlobalVariables.username
        try:
            x = SQL.Username_get2(self.username)
            if (len([*self.name.get()])<30) and (int(self.height.get())>=100 and int(self.height.get())<=200) and (int(self.age.get())>=12 and int(self.age.get())<=100) and (int(self.weight.get())>=30 and int(self.weight.get())<=200):
                SQL.updateInfo(self.username, self.name.get(), self.age.get(), self.clicked_gender.get(), self.height.get(), self.weight.get())
                messagebox.showinfo(title="Registered", message="Thank you for your co-operation\nYou are now a part of the FitMetrix community")
                self.master.destroy()
                MainMenu.App()
            else:
                messagebox.showerror(title="Registration failure", message="Invalid inputs")
        except:
            messagebox.showerror(title="Error", message="Invalid inputs")