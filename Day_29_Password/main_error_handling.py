from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

FONT_NAME = "Ariel"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)
    password = "".join(password_list)
    pyperclip.copy(password)
    # password = ""
    # for char in password_list:
    #   password += char
    password_entry.insert(0, password)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    search_data ={}
    web_search = web_entry.get()
    email_search = email_entry.get()
    #password_search = password_entry.get()
    try:
        with open("Day_29_Password/data.json", "r") as data_file:
            search_data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(message="No information for that website exists")
        return
    #print(search_data)
    if web_search in search_data:
        password_search = search_data[web_search]["password"]
        messagebox.showinfo(message=f" Your username is: {email_search}\nYour password is: {password_search}")
    else:
        messagebox.showinfo(message="No information for that website exists")




# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = web_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data ={
        website: {
            "email": email,
            "password": password
        }
    }

    if website == "" or password == "":
        messagebox.showinfo(message="You forgot to complete the details you numpty!")
    else:
        # is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}\nPassword: {password} \nIs it ok to save?")
        # if is_ok:   Commented out for JSON
        try:
            with open("Day_29_Password/data.json", "r") as data_file:
                #json.dump(new_data, data_file, indent=4)
                #file.write(f"{website} | {email} | {password}\n")
                # Reading saved data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("Day_29_Password/data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            with open("Day_29_Password/data.json", "w") as data_file:
            #Updating data
                data.update(new_data)
                json.dump(data, data_file, indent=4)
        finally:
            web_entry.delete(0, END)
            password_entry.delete(0, END)
        # with open("Day_29_Password/data.json", "w") as data_file:
        #     #Saving data
        #     json.dump(data, data_file, indent=4)
        # web_entry.delete(0, END)
        # password_entry.delete(0, END)
    

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="Day_29_Password/logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Labels
web_label =Label(text="Website:", font=(FONT_NAME, 8))
web_label.grid(column=0, row=1)

email_label =Label(text="Email/Username::", font=(FONT_NAME, 8))
email_label.grid(column=0, row=2)

password_label =Label(text="Password:", font=(FONT_NAME, 8))
password_label.grid(column=0, row=3)

#Text entry
web_entry = Entry(width=21)
web_entry.focus()
web_entry.grid(column=1, row=1)

email_entry = Entry(width=35)
email_entry.insert(0, "scott@email.com")
email_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# Buttons
search_password = Button(text="Search", command=find_password, font=(FONT_NAME, 8), padx=2, pady=2)
search_password.grid(column=2, row=1,sticky="ew")

gen_password = Button(text="Generate Password", command=password_generator, font=(FONT_NAME, 8), padx=2, pady=2)
gen_password.grid(column=2, row=3)

add_password = Button(text="Add", command=save_password, width=42, font=(FONT_NAME, 8), padx=2, pady=2)
add_password.grid(column=1, row=4, columnspan=2)

window.mainloop()