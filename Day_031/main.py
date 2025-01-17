# Day 31 was focused on creating a flash card app.
# This app makes use of tkinter and pandas to create a GUI
# that presents the front of a card with a word in french.
# After a 3s delay, the card flips with the corresponding word in English,
# the user then selects if he knew the English match or not.
# The known words are written to a csv file that is used to save the user's progress. 

import os
import pandas as pd
import random as rand
import tkinter as tk
from tkinter import messagebox

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

CARD_FRONT_IMAGE_PATH = os.path.join(PROJECT_DIR, "assets", "card_front.png")
CARD_BACK_IMAGE_PATH = os.path.join(PROJECT_DIR, "assets", "card_back.png")

RIGHT_BUTTON_IMAGE_PATH = os.path.join(PROJECT_DIR, "assets", "right.png")
WRONG_BUTTON_IMAGE_PATH = os.path.join(PROJECT_DIR, "assets", "wrong.png")

LEARNED_WORDS_FILE_PATH = os.path.join(PROJECT_DIR, "data", "words_to_learn.csv")
WORDS_FILE_PATH = os.path.join(PROJECT_DIR, "data", "french_words.csv")

BACKGROUND_COLOR = "#B1DDC6"


def next_card():
    """Display the next card with a random French word.

    This function selects a random word from the list of records,
    updates the canvas to show the French word, and sets a timer
    to flip the card after a specified duration.

    Raises:
        IndexError: If there are no words left in the records.
    """
    global current_card, timer
    try:
        current_card = records[rand.randint(0, len(df) - 1)]
    except IndexError:
        return
    else:
        screen.after_cancel(timer)
        timer = screen.after(3000, flip_card)
        canvas.itemconfig(canvas_bg, image=CARD_FRONT_IMAGE)
        canvas.itemconfig(card_title, text="French", fill="black")
        canvas.itemconfig(card_word, text=current_card["French"], fill="black")

def flip_card():
    """Flip the current card to show the English translation.

    This function updates the canvas to display the English word
    corresponding to the current French word.
    """
    canvas.itemconfig(canvas_bg, image=CARD_BACK_IMAGE)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


def learn_word():
    """Remove the current word from the list of records and update the CSV.

    This function removes the current card from the records,
    updates the CSV file to reflect the learned words, and
    displays the next card.
    """
    records.remove(current_card)
    update_csv()
    next_card()

def update_csv():
    """Update the CSV file with the current list of learned words.

    This function converts the current records into a DataFrame
    and saves it to the specified CSV file.
    """
    pd.DataFrame(records).to_csv(LEARNED_WORDS_FILE_PATH, index=False)


##############
# UI Configs #
##############

screen = tk.Tk()
screen.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
screen.title("Flashy")

CARD_FRONT_IMAGE = tk.PhotoImage(file=CARD_FRONT_IMAGE_PATH)
CARD_BACK_IMAGE = tk.PhotoImage(file=CARD_BACK_IMAGE_PATH)

RIGHT_BUTTON_IMAGE = tk.PhotoImage(file=RIGHT_BUTTON_IMAGE_PATH)
WRONG_BUTTON_IMAGE = tk.PhotoImage(file=WRONG_BUTTON_IMAGE_PATH)

canvas = tk.Canvas(height=526, width=800, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas_bg = canvas.create_image(400, 263, image=CARD_FRONT_IMAGE)
canvas.grid(row=0, column=0, columnspan=2)

wrong_btn = tk.Button(
    image=WRONG_BUTTON_IMAGE, borderwidth=0, relief="flat", command=next_card
)
wrong_btn.grid(row=1, column=0)

right_btn = tk.Button(
    image=RIGHT_BUTTON_IMAGE, borderwidth=0, relief="flat", command=learn_word
)
right_btn.grid(row=1, column=1)

card_title = canvas.create_text(400, 150, font=("Roboto", 40, "italic"))
card_word = canvas.create_text(400, 300, font=("Roboto", 60, "bold"))

###########
# Program #
###########

end_program = False

words_to_learn = []

try:
    df = pd.read_csv(LEARNED_WORDS_FILE_PATH)
except FileNotFoundError:
    df = pd.read_csv(WORDS_FILE_PATH)

records = df.to_dict(orient="records")

timer = screen.after(3000, flip_card)

next_card()

screen.mainloop()
