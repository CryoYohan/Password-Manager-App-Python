import tkinter
from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=20, pady=20)
window.title("Password Manager")

canvas = Canvas(width=200, height=200, highlightthickness=0)
mypass_image = PhotoImage(file="logo.png")
canvas.create_image(100,94, image=mypass_image)
website_field = tkinter.Entry()

canvas.pack()

window.mainloop()