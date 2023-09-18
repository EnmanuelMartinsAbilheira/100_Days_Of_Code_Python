
from tkinter import *
import os

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    with open("Password.txt", "a") as data_file:
        data_file.write(f"{website} ! {email} ! {password} \n")
        website_entry.delete(0, END)
        password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

#Labels
website_label = Label(text="Website: ")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username: ")
email_label.grid(column=0, row=2)

password_label = Label(text="Passsword: ")
password_label.grid(column=0, row=3)


#Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_label.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1,  columnspan=2)
email_entry.insert(0, "angela@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)


#Buttons
generate_password_buton = Button(text="Generate Password")
generate_password_buton.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4,  columnspan=2)

window.mainloop()
