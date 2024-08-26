import tkinter as tk
from tkinter import PhotoImage
from tkinter import messagebox
from tkinter import *
from PIL import Image, ImageTk
import Calculate_Bodyfat as Calculate_Bodyfat
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
            Calculate_Bodyfat.App()
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

#Creating the labels.
    def create_labels(self):
        self.main_label = tk.Label(self, text = "Body fat% calculator", bg="#98FB98", fg="#000000", font=("Arial", 25), highlightbackground="black", highlightthickness=1)
        self.main_label.place(relx=.53, rely=.1, anchor=CENTER)

        self.bodyfat_label=tk.Label(self, text="Result", bg="#FFFACD")
        self.bodyfat_label.place(relx=0.18,rely=0.32)

        self.chart_photo=Image.open("C:/Users/iamar/OneDrive/Pictures/A LEVELS/NEA/BODYFAT NEA.png")
        self.chart_photo=self.chart_photo.resize((250,225))
        self.chart_photo=ImageTk.PhotoImage(self.chart_photo)
        self.chart_photo_label=tk.Label(self,image=self.chart_photo)
        self.chart_photo_label.place(relx=.55, rely=.65,anchor=CENTER)
                
#Creating the entries.
    def create_entries(self):

        self.bodyfat=tk.Entry(self, font=("Calibri",18))
        self.bodyfat.config(width=28)
        self.bodyfat.place(relx=.275, rely=0.315)
        self.bodyfat.insert(0,GlobalVariables.bodyfat)