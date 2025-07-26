import tkinter
from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=50, pady=50)
window.title("Password Manager")

canvas = Canvas(width=200, height=200, highlightthickness=0)
mypass_image = PhotoImage(file="logo.png")
mypass_logo = canvas.create_image(100,94, image=mypass_image)
website_label = Label(window, text="Website: ")
website_field = Entry(window, width=35)
email_username_label = Label(window, text="Username/Email: ")
email_username_field = Entry(window, width=35)
password_label = Label(window, text="Password: ")
password_field = Entry(window, width=21)
generate_password_btn = Button(window, text="Generate Password")
add_btn = Button(window, text="Add", width=36)

# Grid Layout
canvas.grid(row=0, column=1,sticky=NSEW)
website_label.grid(row=1, column=0,sticky=NSEW)
website_field.grid(row=1, column=1, columnspan=2,sticky=NSEW,pady=5)
email_username_label.grid(row=2, column=0,sticky=NSEW)
email_username_field.grid(row=2, column=1, columnspan=2,sticky=NSEW,pady=5)
password_label.grid(row=3, column=0,sticky=NSEW)
password_field.grid(row=3, column=1, sticky=NSEW,pady=5)
generate_password_btn.grid(row=3, column=2,sticky=NSEW,pady=5, padx=2)
add_btn.grid(row=4, column=1, columnspan=2,sticky=NSEW,pady=5)

window.mainloop()