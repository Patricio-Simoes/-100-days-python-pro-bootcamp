# On day 29, a password manager app was created, using the Tkinter module.
# It's a simple password manager, that allows you to store yur entries in
# a txt file under the format: Website | Email/Username | Password
# The passwords can be randomly generated and copied to the clipboard, using
# the pyperclip module.

# On day 30, this app was updated to store in a JSON file instead.

import tkinter as tk
from tkinter import messagebox
import json
import os
import pyperclip
import random

FONT_BOLD = ("Roboto", 12, "bold")
FONT = ("Roboto", 12)

LETTERS = [
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
NUMBERS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
SYMBOLS = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

ICON_IMG = os.path.join(PROJECT_DIR, "assets", "logo.ico")
LOGO_IMG = os.path.join(PROJECT_DIR, "assets", "logo.png")

DATA_FILE = os.path.join(PROJECT_DIR, "data", "data.json")


def define_password_character_count(target_sum):
    """Define the count of letters, numbers, and symbols for the password.

    This function randomly generates the number of letters, numbers, and symbols
    to include in a password based on the specified total character count
    (target_sum). It ensures that at least one letter, one number, and
    one symbol are included in the password.

    Args:
        target_sum (int): The total number of characters the password should contain.

    Returns:
        list: A list containing three integers: the count of letters, the count of numbers,
        and the count of symbols.
    """
    letters = 1
    numbers = 1
    symbols = 1

    remaining = target_sum - 3

    letters += random.randint(0, remaining)
    remaining -= letters - 1

    numbers += random.randint(0, remaining)
    remaining -= numbers - 1

    symbols += remaining

    return [letters, numbers, symbols]


def generate_password():
    """Generate a random password and copy it to the clipboard.

    This function generates a password based on the character counts
    defined by the `define_password_character_count` function. It
    randomly selects letters, numbers, and symbols, shuffles them,
    and then copies the resulting password to the clipboard. The
    generated password is also displayed in the password entry field.

    Returns:
        None
    """
    count = define_password_character_count(int(password_spinbox.get()))

    password_letters = [random.choice(LETTERS) for _ in range(count[0])]
    password_numbers = [random.choice(NUMBERS) for _ in range(count[1])]
    password_symbols = [random.choice(SYMBOLS) for _ in range(count[2])]

    password = password_letters + password_numbers + password_symbols

    random.shuffle(password)

    password = "".join(password)

    pyperclip.copy(password)

    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

    tk.messagebox.showinfo(
        "Copied to Clipboard",
        "Your password has been generated & copied to the clipboard!",
    )


def save():
    """
    Save the entered website, email, and password to a specified data file.

    This function retrieves the values from the input fields for the website,
    email/username, and password. It checks if any of the fields are empty and
    displays an error message if so. If all fields are filled, it prompts the
    user to confirm the details before saving them to a specified data file.

    The data is stored in a JSON format, where each website is a key, and its
    associated value is a dictionary containing the email/username and password.
    If the file does not exist, it will be created. If the file is empty or
    contains invalid JSON, it will be initialized.

    After saving, the input fields are cleared.

    Raises:
        ValueError: If any of the fields are empty.
        FileNotFoundError: If the specified data file does not exist when trying to read.
        json.JSONDecodeError: If the data file is empty or contains invalid JSON.

    Returns:
        None
    """
    widgets = (website_entry, email_entry, password_entry)
    website = widgets[0].get()
    email = widgets[1].get()
    password = widgets[2].get()
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(
            title="Oops", message="Please don't leave any empty fields!"
        )
        return
    confirm = messagebox.askokcancel(
        title="Confirm details",
        message=f"Website: {website}\nEmail/Username: {email}\nPassword: {password}",
    )
    if confirm:
        new_data = {website: {"email": email, "password": password}}
        try:
            with open(DATA_FILE, "r") as file:
                file_data = json.load(file)
        except FileNotFoundError:
            with open(DATA_FILE, "w") as file:
                json.dump(new_data, file, indent=4)
        except json.JSONDecodeError:
            file_data = {}
        finally:
            file_data.update(new_data)
            with open(DATA_FILE, "w") as file:
                json.dump(file_data, file, indent=4)
            for widget in widgets:
                widget.delete(0, tk.END)


def search_data():
    """
    Search for the email/username and password associated with a given website entry.

    This function retrieves the website name from the input field and attempts to
    load the stored data from a specified JSON file. If the file is found and
    contains valid JSON data, it checks for the presence of the specified website
    entry. If found, it displays the associated email/username and password in a
    message box. If the website entry is not found, an error message is shown.

    If the data file does not exist or is empty, the function handles these cases
    gracefully without raising an error.

    Raises:
        FileNotFoundError: If the specified data file does not exist.
        json.JSONDecodeError: If the data file is empty or contains invalid JSON.
        KeyError: If the specified website entry is not found in the loaded data.

    Returns:
        None
    """
    entry = website_entry.get()
    if entry == "":
        tk.messagebox.showwarning("Empty Website", "Please insert a valid website name.")
        return
    try:
        with open(DATA_FILE, "r") as file:
            file_data = json.load(file)
    except FileNotFoundError:
        pass
    except json.JSONDecodeError:
        file_data = {}
    finally:
        try:
            tk.messagebox.showinfo(
                entry,
                f"Email/Username: {file_data[entry]['email']}\nPassword: {file_data[entry]['password']}",
            )
        except KeyError:
            tk.messagebox.showerror(entry, f"{entry} was not found in the database.")


window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
window.resizable(False, False)


logo_img = tk.PhotoImage(file=LOGO_IMG)

canvas = tk.Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = tk.Label(text="Website:", font=FONT_BOLD)
website_label.grid(row=1, column=0, sticky="E")

website_entry = tk.Entry(font=FONT)
website_entry.grid(row=1, column=1, columnspan=2, sticky="EW")
website_entry.focus()

email_label = tk.Label(text="Email/Username:", font=FONT_BOLD)
email_label.grid(row=2, column=0, sticky="E")

email_entry = tk.Entry(font=FONT)
email_entry.grid(row=2, column=1, columnspan=3, sticky="EW")

password_label = tk.Label(text="Password:", font=FONT_BOLD)
password_label.grid(row=3, column=0, sticky="E")

password_entry = tk.Entry(font=FONT)
password_entry.grid(row=3, column=1, sticky="EW")

password_spinbox = tk.Spinbox(from_=8, to=128, width=3)
password_spinbox.grid(row=3, column=2)
password_spinbox.bind("<Key>", "break")

search_btn = tk.Button(text="Search", font=FONT, padx=5, pady=0, command=search_data)
search_btn.grid(row=1, column=3, sticky="EW")

generate_btn = tk.Button(
    text="Generate Password", font=FONT, padx=5, pady=0, command=generate_password
)
generate_btn.grid(row=3, column=3, sticky="EW")

add_btn = tk.Button(text="Add", font=FONT, padx=5, pady=0, command=save)
add_btn.grid(row=4, column=1, sticky="EW")

window.mainloop()
