import tkinter as tk
from tkinter import PhotoImage
from tkinter import messagebox
from tkinter import *
from PIL import Image, ImageTk
import Main_Menu as MainMenu
import UpdateProgress_Menu as UpdateProgress
import Analytics as Analytics

#Creating the window.
class App(tk.Tk):
    def __init__(self):

        #main setup
        super().__init__()
        self.title("Your progress menu")
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
            MainMenu.App()
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
        self.create_buttons()

#Creating the labels.
    def create_labels(self):
        self.main_label = tk.Label(self, text = "Your progress", bg="#98FB98", fg="#000000", font=("Arial", 40), highlightbackground="black", highlightthickness=1)
        self.main_label.place(relx=.50, rely=.15, anchor=CENTER)

        self.progress_photo=Image.open("C:/Users/iamar/OneDrive/Pictures/A LEVELS/NEA/PROGRESS PHOTO NEA.png")
        self.progress_photo=self.progress_photo.resize((140,120))
        self.progress_photo=ImageTk.PhotoImage(self.progress_photo)
        self.progress_photo_label=tk.Label(self,image=self.progress_photo)
        self.progress_photo_label.place(relx=.50, rely=.50,anchor=CENTER)
        
#Creating the buttons.   
    def create_buttons(self):
        self.update_progress_button = tk.Button(self, text="Update your\nprogress", bg="#CDC9C9", font=("Arial black", 18), height=3, width=12, command=self.updateProgress)
        self.update_progress_button.place(relx=.20, rely=.50,anchor=CENTER)
        self.view_analytics_button = tk.Button(self, text="View analytics", bg="#CDC9C9", font=("Arial black", 18), height=3, width=12, command=self.viewAnalytics)
        self.view_analytics_button.place(relx=.80, rely=.50,anchor=CENTER)

#Opening the update progress page.
    def updateProgress(self):
        try:
            self.master.destroy()
            UpdateProgress.App()
        except:
            pass

#Opening the analytics page.    
    def viewAnalytics(self):
        try:
            self.master.destroy()
            Analytics.App()
        except:
            pass