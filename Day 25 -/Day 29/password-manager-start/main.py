# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from tkinter import *
from tkinter import messagebox
import json
# ---------------------------- SAVE PASSWORD ------------------------------- #
def Add():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()
    new_data = {website: {
        "email" : username,
        "password" : password
    }}
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message = "Please make sure you do not leave any fields empty")
    else:
        try:
            with open(f"PasswordManager.json","r") as data:
                data_file = json.load(data)
        except FileNotFoundError:
            with open(f"PasswordManager.json","w") as data:
                json.dump(new_data, data, indent = 4)
        else:
            data_file.update(new_data)
            with open(f"PasswordManager.json", "w") as data:
                json.dump(data_file, data, indent=4)

        finally:
            website_input.delete(0,END)
            password_input.delete(0,END)


def search():
    website = website_input.get()
    try:
        with open("PasswordManager.json","r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]['password']
            messagebox.showinfo(title=website,message=f"email: {email}\npassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists")
    



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")

window.config(padx=20, pady=20)
canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=image)
canvas.grid(column=1,row=0)
website_label=Label(text="Website:")
website_label.grid(column=0,row=1)
website_input = Entry(width=32)
website_input.grid(column=1,row=1,columnspan=1)
username_label=Label(text="Email/Username:")
username_label.grid(column=0,row=2)
username_input = Entry(width=50)
username_input.grid(column=1,row=2,columnspan=2)
username_input.insert(0,"kohcheexuan@gmail.com")
password_label=Label(text="Password:")
password_label.grid(column=0,row=3)
password_input = Entry(width=32)
password_input.grid(column=1,row=3)
password_button = Button(text="Generate Password",width = 15)
password_button.grid(column=2,row=3)
add_button = Button(text="Add",width=42,command=Add)
add_button.grid(column=1,row=4,columnspan=2)
search_button = Button(text="Search",width=15,command=search)
search_button.grid(column=2,row=1)


window.mainloop()