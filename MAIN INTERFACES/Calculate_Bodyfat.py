import tkinter as tk
from tkinter import PhotoImage
from tkinter import messagebox
from tkinter import *
from PIL import Image, ImageTk
import Calculations_menu as Calculations_menu
import Show_Bodyfat as Show_Bodyfat
import GlobalVariables

#Creating the window.
class App(tk.Tk):
    def __init__(self):

        #main setup
        super().__init__()
        self.title("Bodyfat")
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
            Calculations_menu.App()
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
        self.create_entries()
        self.create_button()
        self.create_dropList()

#Creating the labels.
    def create_labels(self):
        self.main_label = tk.Label(self, text = "Body fat% calculator", bg="#98FB98", fg="#000000", font=("Arial", 25), highlightbackground="black", highlightthickness=1)
        self.main_label.place(relx=.53, rely=.1, anchor=CENTER)

        self.height_label=tk.Label(self, text="Height(m)", bg="#FFFACD")
        self.height_label.place(relx=0.18,rely=0.345)

        self.weight_label=tk.Label(self, text="Weight(kg)", bg="#FFFACD")
        self.weight_label.place(relx=0.1775,rely=0.453)

        self.age_label=tk.Label(self, text="Age", bg="#FFFACD")
        self.age_label.place(relx=0.2,rely=0.56)

        self.gender_label=tk.Label(self, text="Gender", bg="#FFFACD")
        self.gender_label.place(relx=0.19,rely=0.67)
    
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

#Creating the drop-down list.
    def create_dropList(self):

        self.gender_options=["Male","Female"]
        self.clicked_gender=StringVar()
        self.clicked_gender.set("Select gender")
        self.preference_drop=OptionMenu(self, self.clicked_gender, *self.gender_options)
        self.preference_drop.config(width=50)
        self.preference_drop.place(relx=.6, rely=0.69, anchor=CENTER)

#Creating the calculate button.
    def create_button(self):
        calculate=tk.Button(self, text="Calculate", font=("Calibri", 12), command=self.calculation)
        calculate.place(relx=0.5, rely=0.775)


#Implementing the bodyfat calculations.    
    def calculation(self):
        try:
            self.Height=float(self.height.get())
            self.Age=int(self.age.get())
            self.Weight=float(self.weight.get())

            self.BMI = (self.Weight)/(self.Height**2)
            self.BMI = ("{:.1f}".format(self.BMI))

            if self.clicked_gender.get() == "Male":
                self.Bodyfat = ("{:.1f}".format((float(1.20)*float(self.BMI))+(0.23*self.Age)-(16.2)))
                self.Bodyfat = str(self.Bodyfat) + "%"

            elif self.clicked_gender.get() == "Female":
                self.Bodyfat = ("{:.1f}".format((float(1.20)*float(self.BMI))+(0.23*self.Age)-(5.4)))
                self.Bodyfat = str(self.Bodyfat) + "%" 

            
            GlobalVariables.bodyfat = self.Bodyfat    

            self.master.destroy()
            Show_Bodyfat.App()
        except:
            messagebox.showerror(title="Error",message="Invalid inputs")