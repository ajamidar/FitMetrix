import tkinter as tk
from tkinter import PhotoImage
from tkinter import messagebox
from tkinter import *
from PIL import Image, ImageTk
import YourProgress_Menu as YourProgress_Menu
import GlobalVariables
import mySQL as SQL
import matplotlib.pyplot as plt
from abc import ABC, abstractmethod

#Creating the window.
class App(tk.Tk):
    def __init__(self):

        #main setup
        super().__init__()
        self.title("Analytics")
        self.geometry("800x500")
        self.configure(bg="#B9D3EE")

        #widgets
        self.options=Options(self)
        self.main=Main(self)

        #run
        self.mainloop()

#Creating Options Frame.   
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
        
    #Back button's function.
    def back(self):
        try:
            self.master.destroy()
            YourProgress_Menu.App()
        except:
            pass


#Creating Abstract class - this gives a structure for the main frame.
class MainStructure(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def create_labels():
        pass
    
    @abstractmethod
    def create_entries():
        pass
    
    @abstractmethod
    def create_buttons():
        pass
    
    @abstractmethod
    def Graph1():
        pass
    
    @abstractmethod
    def Graph2():
        pass
    
    @abstractmethod
    def check():
        pass

#Creating Main frame.
class Main(tk.Frame, MainStructure):
    def __init__(self,master):
        super().__init__(master)
        self.configure(bg="#FFFACD", highlightbackground="black", highlightthickness=1)
        self.pack(side=tk.LEFT)
        self.propagate(False)
        self.configure(width=800, height=500)

        self.create_labels()
        self.create_entries()
        self.create_buttons()

#Creating the labels.
    def create_labels(self):
        self.main_label = tk.Label(self, text = "Analytics", bg="#98FB98", fg="#000000", font=("Arial", 25), highlightbackground="black", highlightthickness=1)
        self.main_label.place(relx=.53, rely=.1, anchor=CENTER)

        self.BMI_label=tk.Label(self, text="Your BMI", bg="#FFFACD")
        self.BMI_label.place(relx=.17, rely=0.225)

        self.AvgBMI_label=tk.Label(self, text="Average BMI", bg="#FFFACD")
        self.AvgBMI_label.place(relx=.155, rely=0.335)
    
        self.bodyfat_label=tk.Label(self, text="Your bodyfat%", bg="#FFFACD")
        self.bodyfat_label.place(relx=.145, rely=0.585)

        self.AvgBodyfat_label=tk.Label(self, text="Average bodyfat%", bg="#FFFACD")
        self.AvgBodyfat_label.place(relx=.130, rely=0.695)

#Creating the entries.    
    def create_entries(self):

        self.BMI=tk.Entry(self, font=("Calibri",18))
        self.BMI.config(width=28)
        self.BMI.place(relx=.328, rely=0.215)
        self.BMI.insert(0,str(SQL.getBMI(GlobalVariables.username)))
        self.check()

        self.AvgBMI=tk.Entry(self, font=("Calibri",18))
        self.AvgBMI.config(width=28)
        self.AvgBMI.place(relx=.328, rely=0.325)
        self.AvgBMI.insert(0,str("{:.1f}".format(SQL.getAvgBMI())))

        self.Bodyfat=tk.Entry(self, font=("Calibri",18))
        self.Bodyfat.config(width=28)
        self.Bodyfat.place(relx=.328, rely=0.575)
        self.Bodyfat.insert(0,str(SQL.getBodyfat(GlobalVariables.username)))

        self.AvgBodyfat=tk.Entry(self, font=("Calibri",18))
        self.AvgBodyfat.config(width=28)
        self.AvgBodyfat.place(relx=.328, rely=0.685)
        self.AvgBodyfat.insert(0,str("{:.1f}".format(SQL.getAvgBodyfat())))

#Creating the buttons.    
    def create_buttons(self):
        self.graph1=tk.Button(self, text="Graph it!", font=("Calibri", 12), command=self.Graph1)
        self.graph1.place(relx=0.45, rely=0.45) 

        self.graph2=tk.Button(self, text="Graph it!", font=("Calibri", 12), command=self.Graph2)
        self.graph2.place(relx=0.45, rely=0.81) 

#Setting up the 1st graph.
    def Graph1(self):
        YourBMI = int(SQL.getBMI(GlobalVariables.username))
        AvgBMI = int(SQL.getAvgBMI())
        UKAvgBMI = GlobalVariables.UKAvgBMI
        BMI_data = {"You":YourBMI,
                    "FitMetrix average":AvgBMI,
                    "UK's average":UKAvgBMI}
        
        plt.rcParams["axes.prop_cycle"] = plt.cycler(
            color = ["#4C2A85","#BE96FF","#957DAD","#5E366E","#A98CCC"])
        
        fig1, ax1 = plt.subplots()
        ax1.bar(BMI_data.keys(), BMI_data.values())
        ax1.set_title("BMI comparison")
        ax1.set_xlabel("Reference")
        ax1.set_ylabel("BMI")
        plt.show()

#Setting up the 2nd graph.
    def Graph2(self):
        if SQL.getGender(GlobalVariables.username) == "Male":
            YourBodyfat = int(SQL.getBodyfat(GlobalVariables.username))
            AvgBodyfat = int(SQL.getAvgBodyfat())
            UKAvgBodyfat = GlobalVariables.UKAvgBodyfat_Male
            
            Bodyfat_data = {"You":YourBodyfat,
                            "FitMetrix average":AvgBodyfat,
                            "UK's average":UKAvgBodyfat}
            
            plt.rcParams["axes.prop_cycle"] = plt.cycler(
            color = ["#4C2A85","#BE96FF","#957DAD","#5E366E","#A98CCC"])
        
            fig1, ax1 = plt.subplots()
            ax1.bar(Bodyfat_data.keys(), Bodyfat_data.values())
            ax1.set_title("Bodyfat comparison")
            ax1.set_xlabel("Reference(Men)")
            ax1.set_ylabel("Bodyfat")
            plt.show()

        elif SQL.getGender(GlobalVariables.username) == "Female":
            YourBodyfat = int(SQL.getBodyfat(GlobalVariables.username))
            AvgBodyfat = int(SQL.getAvgBMI())
            UKAvgBodyfat = GlobalVariables.UKAvgBodyfat_Female

            Bodyfat_data = {"You":YourBodyfat,
                            "FitMetrix average":AvgBodyfat,
                            "UK's average":UKAvgBodyfat}
            
            plt.rcParams["axes.prop_cycle"] = plt.cycler(
            color = ["#4C2A85","#BE96FF","#957DAD","#5E366E","#A98CCC"])
        
            fig1, ax1 = plt.subplots()
            ax1.bar(Bodyfat_data.keys(), Bodyfat_data.values())
            ax1.set_title("Bodyfat guide")
            ax1.set_xlabel("Reference(Women)")
            ax1.set_ylabel("Bodyfat")
            plt.show()

#Check for existence of data in the database.
    def check(self):
        if self.BMI.get() == "None":
            messagebox.showerror(title="Error", message="Please upload your progress first.")