import tkinter
from tkinter import PhotoImage
from tkinter import messagebox
from tkinter import *

#Adding functionalities to the buttons.
def logout():
    messagebox.showinfo(title="Logout", message="Successfully logged out")
    window.destroy()
    import OOP_Login_page

def yourdetails():
    messagebox.showinfo(title="Your details", message="Username=johnsmith\nPassword=12345678")

def dietplans():
    messagebox.showinfo(title="Diet plans", message="Eat whatever you want")

def workoutplans():
    messagebox.showinfo(title="Workout plans", message="Play football")

def progress():
    messagebox.showinfo(title="Your progress", message="No progress saved\nPlease comeback later")

#Creating the window.
window = tkinter.Tk()
window.title("Main Menu")
window.geometry("800x500")
window.configure(bg="#B9D3EE")

#Defning the logo.
logo=PhotoImage(file="C:/Users/iamar/OneDrive/Pictures/A LEVELS/NEA/LOGO FITMETRIX BLUE.png") 

#Creating the frames, interface_frame holds both options_frame & main_frame.
interface_frame = tkinter.Frame(window, highlightbackground="black", highlightthickness=1)
options_frame = tkinter.Frame(interface_frame, bg="#CDC9C9", highlightbackground="black", highlightthickness=1)
main_frame = tkinter.Frame(interface_frame, bg="#B9D3EE", highlightbackground="black", highlightthickness=1)

#Postioning the frames.
interface_frame.pack(anchor=CENTER)
options_frame.pack(side=tkinter.LEFT)
options_frame.pack_propagate(False)
options_frame.configure(width=170, height=500)
main_frame.pack(side=tkinter.LEFT)
main_frame.propagate(False)
main_frame.configure(width=800, height=500)

#Creating the options_frame 's buttons.
logout_button = tkinter.Button(options_frame, bg="#8B8989", text="Logout", font=("Arial Black", 14), command=logout)
logout_button.place(x=35, y=20)
yourdetails_button = tkinter.Button(options_frame, bg="#8B8989", text="Your details", font=("Arial Black", 14), command=yourdetails)
yourdetails_button.place(x=10, y=425)

#Creating the main_frame 's labels.
main_label = tkinter.Label(main_frame, text = "FitMetrix", bg="#FCE6C9", fg="#000000", font=("Arial", 30))
main_label.place(relx=.47, rely=.1, anchor=CENTER)
logo_label = tkinter.Label(main_frame, image=logo, bg="#B9D3EE")
logo_label.place(relx=.47, rely=.28,anchor=CENTER)

#Creating the main_frame 's buttons.
diet_button = tkinter.Button(main_frame, text="Diet plans", bg="#CDC9C9", font=("Arial black", 18), height=3, command=dietplans)
diet_button.place(relx=.15, rely=.55,anchor=CENTER)
workout_button = tkinter.Button(main_frame, text="Workout plans", bg="#CDC9C9", font=("Arial black", 18), height=3, command=workoutplans)
workout_button.place(relx=.465, rely=.55,anchor=CENTER)
progress_button = tkinter.Button(main_frame, text="Your progress", bg="#CDC9C9", font=("Arial black", 18), height=3, command=progress)
progress_button.place(relx=.82, rely=.55,anchor=CENTER)


window.mainloop()