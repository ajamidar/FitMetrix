import tkinter as tk
from tkinter import PhotoImage
from tkinter import messagebox
from tkinter import *
from PIL import Image, ImageTk
import GlobalVariables
import UpdateProgress_Menu as UpdateProgress
import YourProgress_Menu as YourProgress
import mySQL as SQL

#Creating the window.
class App(tk.Tk):
    def __init__(self):

        #main setup
        super().__init__()
        self.title("Update progress")
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
        self.create_dropList()
        self.create_entries()
        self.create_button()

#Creating the labels
    def create_labels(self):
        self.main_label = tk.Label(self, text = "Upload your progress", bg="#98FB98", fg="#000000", font=("Arial", 25), highlightbackground="black", highlightthickness=1)
        self.main_label.place(relx=.59, rely=.1, anchor=CENTER)

        self.BMI_label=tk.Label(self, text="BMI", bg="#FFFACD")
        self.BMI_label.place(relx=.20, rely=0.26)

        self.bodyfat_label=tk.Label(self, text="Body fat%", bg="#FFFACD")
        self.bodyfat_label.place(relx=0.18,rely=0.38)

        self.weight_label=tk.Label(self, text="Weight", bg="#FFFACD")
        self.weight_label.place(relx=0.19,rely=0.51)

        self.follow_label=tk.Label(self, text="Did you follow your\nsaved plans?", bg="#FFFACD")
        self.follow_label.place(relx=0.13, rely=0.62)

#Creating the drop-down list.    
    def create_dropList(self):
        self.follow_options=["Yes","No"]
        self.follow=StringVar()
        self.follow.set("Select an option")
        self.follow_drop=OptionMenu(self, self.follow, *self.follow_options)
        self.follow_drop.config(width=50)
        self.follow_drop.place(relx=.6, rely=0.66, anchor=CENTER)

#Creating the entries.
    def create_entries(self):
        self.BMI=tk.Entry(self, font=("Calibri",18))
        self.BMI.config(width=28)
        self.BMI.place(relx=.328, rely=0.25)

        self.bodyfat=tk.Entry(self, font=("Calibri",18))
        self.bodyfat.config(width=28)
        self.bodyfat.place(relx=.328, rely=0.37)

        self.weight=tk.Entry(self, font=("Calibri",18))
        self.weight.config(width=28)
        self.weight.place(relx=.328, rely=0.50)

#Creating the buttons.
    def create_button(self):
        self.save=tk.Button(self, text="Submit", font=("Calibri", 12), command=self.Save)
        self.save.place(relx=0.4, rely=0.8)

        self.update=tk.Button(self, text="Update", font=("Calibri", 12), command=self.Update)
        self.update.place(relx=0.6, rely=0.8)

#Saving the user's progress in the system's database.
    def Save(self):
        try:
            if int(self.BMI.get())<=40 and int(self.bodyfat.get())<=55:
                SQL.addtoUserProfile(GlobalVariables.username,self.bodyfat.get(),self.BMI.get())
                SQL.updateWeight(GlobalVariables.username, self.weight.get())
                messagebox.showinfo(title="Saved", message="Your progress has been saved.")
                self.master.destroy()
                YourProgress.App()
            else:
                messagebox.showerror(title="Error",message="Invalid inputs")
        except:
            messagebox.showerror(title="Error",message="Invalid inputs")

#Updating the user's progress in the system's database. 
    def Update(self):
        try:
            if int(self.BMI.get())<=40 and int(self.bodyfat.get())<=55:
                SQL.UpdateUserProfile(GlobalVariables.username,self.bodyfat.get(),self.BMI.get())
                SQL.updateWeight(GlobalVariables.username,self.weight.get())
                messagebox.showinfo(title="Updated", message="Your progress has been updated.")
                self.master.destroy()
                YourProgress.App()
            else:
                messagebox.showerror(title="Error",message="Invalid inputs")
        except:
            messagebox.showerror(title="Error",message="Invalid inputs") 
