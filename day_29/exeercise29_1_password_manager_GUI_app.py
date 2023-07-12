# Exercise29.1 Building a Password Manager GUI App with TKinter


from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    field_pass.delete(0, END)
    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    password_letter = [choice(letters) for letter in range(randint(8, 10))]
    password_num = [choice(numbers) for num in range(randint(2, 4))]
    password_symbol = [choice(symbols) for sym in range(randint(2, 4))]

    password_list = password_letter + password_num + password_symbol
    shuffle(password_list)

    final_gen_pass = "".join(password_list)
    field_pass.insert(0, final_gen_pass)
    pyperclip.copy(final_gen_pass)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    # Add all ithe inserted data to a document
    website = str(field_website.get())
    email = str(field_email.get())
    password = str(field_pass.get())
    if website == "":
        messagebox.showinfo(
            title="Oops",
            message=f"The website field is empty, please fill all the fields before saving.",
        )
    elif email == "":
        messagebox.showinfo(
            title="Oops",
            message=f"The email field is empty, please fill all the fields before saving.",
        )
    elif password == "":
        messagebox.showinfo(
            title="Oops",
            message=f"The password field is empty, please fill all the fields before saving.",
        )
    else:
        is_ok = messagebox.askokcancel(
            title=website,
            message=f"These are the detailes entered: \nEmail: {email} \nPassword:{password} \nIs it ok to save?",
        )

        if is_ok:
            with open("data.txt", "a") as new_access:
                new_access.write(website + " | " + email + " | " + password + "\n")
            # Reset the fields
            field_website.delete(0, END)
            field_pass.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
# Create the window
window = Tk()
window.title("BMM • Password Manager")
window.config(padx=50, pady=50)


# Create the canvas and upload the image
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)


# Labels
website = Label(text="Website:", font=("Arial", 12))
website.grid(column=0, row=1)
website.focus()

email = Label(text="Email/Username:", font=("Arial", 12))
email.grid(column=0, row=2)

password = Label(text="Password:", font=("Arial", 12))
password.grid(column=0, row=3)

password = Label(text="Password:", font=("Arial", 12))
password.grid(column=0, row=3)


# Entries
field_website = Entry(width=35)
field_website.grid(row=1, column=1, columnspan=2)

field_email = Entry(width=35)
field_email.grid(row=2, column=1, columnspan=2)
field_email.insert(0, "mariabalos16@gmail.com")

field_pass = Entry(width=21)
field_pass.grid(row=3, column=1, columnspan=1)


# Bottons
generate_button = Button(
    width=12, text="Generate Password", font=("Arial", 7), command=generate_pass
)
generate_button.grid(row=3, column=2, columnspan=1)

add_button = Button(width=36, text="Add", font=("Arial", 8), command=save_data)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
