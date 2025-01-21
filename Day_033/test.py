# This is a small script, used to make API calls to a Kanye's quote API.
# With each button press, the displayed quote changes.

import tkinter as tk
import requests

def get_quote():
    response = requests.get("https://api.kanye.rest/").json()
    return response["quote"]

def update_quote():
    canvas.itemconfig(quote_text, text=get_quote())

window = tk.Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = tk.Canvas(width=300, height=414)
background_img = tk.PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text=get_quote(), width=250, font=("Arial", 16, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = tk.PhotoImage(file="kanye.png")
kanye_button = tk.Button(image=kanye_img, highlightthickness=0, command=update_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()