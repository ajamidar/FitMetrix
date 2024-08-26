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
        self.title("Your details")
        self.geometry("800x500")
        self.configure(bg="#FFFAFA")

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
        self.configure(bg="#DCDCDC", highlightbackground="black", highlightthickness=1)
        self.pack(side=tk.LEFT)
        self.propagate(False)
        self.configure(width=800, height=500)

        self.create_labels()
        self.create_entries()
        self.create_button()

#Creating the labels.
    def create_labels(self):
        self.main_label = tk.Label(self, text = "Your information", bg="#98FB98", fg="#000000", font=("Arial", 25), highlightbackground="black", highlightthickness=1)
        self.main_label.place(relx=.53, rely=.1, anchor=CENTER)

        self.name_label=tk.Label(self, text="Name", bg="#DCDCDC")
        self.name_label.place(relx=0.19,rely=0.240)

        self.height_label=tk.Label(self, text="Height", bg="#DCDCDC")
        self.height_label.place(relx=0.19,rely=0.345)

        self.weight_label=tk.Label(self, text="Weight", bg="#DCDCDC")
        self.weight_label.place(relx=0.19,rely=0.453)

        self.age_label=tk.Label(self, text="Age", bg="#DCDCDC")
        self.age_label.place(relx=0.2,rely=0.56)

        self.gender_label=tk.Label(self, text="Gender", bg="#DCDCDC")
        self.gender_label.place(relx=0.19, rely=0.68)

#Creating the entries.
    def create_entries(self):

        self.username = GlobalVariables.username

        self.Name = str(SQL.getName(self.username))
        self.name=tk.Entry(self,font=("Calibri",18))
        self.name.insert(0,self.Name)
        self.name.config(width=28)
        self.name.place(relx=.328, rely=0.235)
        
        self.Height = SQL.getHeight(self.username)
        self.height=tk.Entry(self, font=("Calibri",18))
        self.height.insert(0,self.Height)
        self.height.config(width=28)
        self.height.place(relx=.328, rely=0.335)
        
        self.Weight = SQL.getWeight(self.username)
        self.weight=tk.Entry(self, font=("Calibri",18))
        self.weight.insert(0,self.Weight)
        self.weight.config(width=28)
        self.weight.place(relx=.328, rely=0.445)

        self.Age = SQL.getAge(self.username)
        self.age=tk.Entry(self, font=("Calibri",18))
        self.age.insert(0,self.Age)
        self.age.config(width=28)
        self.age.place(relx=.328, rely=0.555)

        self.Gender = SQL.getGender(self.username)
        self.gender=tk.Entry(self, font=("Calibri",18))
        self.gender.insert(0,self.Gender)
        self.gender.config(width=28)
        self.gender.place(relx=.328, rely=0.675)

#Creating the save button.
    def create_button(self):
        self.save=tk.Button(self, text="Save", font=("Calibri", 12), command=self.save)
        self.save.place(relx=0.505, rely=0.8)

#Implementing the save function which updates the user's details in the program's database.
    def save(self):
        username = self.username
        if (len([*self.name.get()])<30) and (int(self.height.get())>=100 and int(self.height.get())<=200) and (int(self.age.get())>=12 and int(self.age.get())<=100) and (int(self.weight.get())>=30 and int(self.weight.get())<=200):
            SQL.updateInfo(username, self.name.get(), self.age.get(), self.gender.get(), self.height.get(), self.weight.get())
            messagebox.showinfo(title="Update success", message="Your information has been updated")
            self.master.destroy()
            MainMenu.App()
        else:
            messagebox.showerror(title="Update failure", message="Invalid inputs")
