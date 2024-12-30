# Day 27 was focused on the Tkinter module and explorings it's widgets.
# This file contains a simple mile to km converter.

import tkinter as tk
from tkinter import messagebox


def convert_units():
    """
    Convert miles to kilometers and update the display label.

    This function retrieves the value entered in the miles entry field,
    converts it to kilometers using the conversion factor (1 mile = 1.60934 km),
    and updates the label to show the converted value. If the input is not a
    valid number, an error message is displayed to the user.

    Raises:
        ValueError: If the input from the miles entry field cannot be converted
        to a float, an error message box is shown to inform the user to enter
        a valid number.
    """
    try:
        converted_value = float(miles_entry.get()) * 1.60934
        km_value_label["text"] = converted_value
    except ValueError:
        messagebox.showerror(title="Invalid input", message="Please enter a valid number for miles.")


window = tk.Tk()

window.title("Mile to Km Converter")
window.config(padx = 20, pady = 20)

miles_unit_label = tk.Label(text="Miles")
miles_unit_label.grid(row=0, column=2)

km_unit_label = tk.Label(text="Km")
km_unit_label.grid(row=1, column=2)

miles_entry = tk.Entry(width=10)
miles_entry.grid(row=0, column=1)

km_value_label = tk.Label(text="0")
km_value_label.grid(row=1, column=1)

equal_to_label = tk.Label(text="is equal to")
equal_to_label.grid(row=1, column=0)

tk_button = tk.Button(text="Calculate", command=convert_units)
tk_button.grid(row=2, column=1)

window.mainloop()
