from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z']

    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

    symbols = ['~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', '|',
               '\\', ';', ':', "'", '"', ',', '<', '.', '>', '/', '?']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list.extend([str(choice(numbers)) for _ in range(randint(2, 4))])
    password_list.extend([choice(symbols) for _ in range(randint(2, 4))])

    shuffle(password_list)
    generated_password = "".join(password_list)
    password_field.delete(0, END)
    password_field.insert(0, generated_password)
    pyperclip.copy(generated_password) # Copy generated password to clipboard

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_name = website_field.get()
    email_or_username = email_username_field.get()
    password = password_field.get()
    new_data = {
        website_name:{
            "email": email_or_username,
            "password": password
        }
    }

    if website_name.strip() == "" or email_or_username.strip() == "" or password.strip() == "":
        messagebox.showwarning("Warning", "Please fill in empty fields!")
        print("Data not saved!")

    else:
        data = None
        # Load JSON data
        try:
            # Initially, update JSON file if not empty
            with open("data.json", "r") as file:
                # Read JSON Data
                data = json.load(file)
                # Update JSON Data
                data.update(new_data)
        # If data.json file not created
        except FileNotFoundError:
            # Create JSON File
            file = open("data.json", "w")
            file.close()
        # If JSON File is empty
        except json.decoder.JSONDecodeError:
            print("No data in JSON. Changing from update.() data to save/dump.() data to JSON file")
            data = new_data
        # Whatever happens, write data to JSON file
        finally:
            with open("data.json", "w") as file:
                json.dump(data, file, indent=1)

        messagebox.showinfo("Information", "Data Saved!")
        website_field.delete(0, END)
        password_field.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=50, pady=50)
window.title("Password Manager")
window.resizable(False, False)

canvas = Canvas(width=200, height=200, highlightthickness=0)
mypass_image = PhotoImage(file="logo.png")

window.wm_iconphoto(True, mypass_image) # Custom GUI Icon

mypass_logo = canvas.create_image(100,94, image=mypass_image)
website_label = Label(window, text="Website: ")
website_field = Entry(window, width=35)
website_field.focus()
search_btn = Button(window, text="Search", width=17)
email_username_label = Label(window, text="Username/Email: ")
email_username_field = Entry(window, width=35)
email_username_field.insert(0,"sample@email.com")
password_label = Label(window, text="Password: ")
password_field = Entry(window, width=21)
generate_password_btn = Button(window, text="Generate Password", cursor="hand2", command=generate_password)
add_btn = Button(window, text="Add", width=36, cursor="hand2", command=save)

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