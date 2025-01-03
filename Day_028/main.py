# On day 28, a pomodoro app was created, using the Tkinter module.
# It's a simple app, that allows you to manage your time with the pomodoro technique,
# by taking 25 min long work sessions, each followed by a 5 min log short break and
# at the end of the 3rd work session, a 20 min long break.

import tkinter as tk
import math
import os

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

BACKGROUND_IMAGE = os.path.join(PROJECT_DIR, "assets", "tomato.png")

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

marks = ""
reps = 0
timer = None

def reset_timer():
    """
    Reset the timer and marks.

    This function cancels the current timer, resets the displayed time to "00:00",
    and clears the marks and repetitions count.

    :return: None
    """
    global marks, reps
    window.after_cancel(timer)
    title_label.config(text="Timer", color=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    marks = ""
    reps = 0

def start_timer():
    """
    Start the timer based on the current repetition count.

    This function increments the repetition count and determines whether to start
    a work session or a break based on the current repetition. It updates the
    title label and starts the countdown.

    :return: None
    """
    global reps
    reps += 1
    if reps % 8 == 0:
        title_label.config(text = "Break", fg = RED)
        count_down(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        title_label.config(text = "Break", fg = PINK)
        count_down(SHORT_BREAK_MIN * 60)
    else:
        title_label.config(text = "Work", fg = GREEN)
        count_down(WORK_MIN * 60)

def count_down(val):
    """
    Countdown timer function.

    This function updates the timer display every second. When the countdown
    reaches zero, it starts the next timer session and updates the marks.

    :param val: The time in seconds to count down from (int).
    :return: None
    """
    mins = math.floor(val / 60)
    secs = val % 60
    if secs < 10:
        secs = "0" + str(secs)
    canvas.itemconfig(timer_text, text="" + str(mins) + ":" + str(secs) + "")
    if val > 0:
        global timer
        timer = window.after(1000, count_down, val - 1)
    else:
        global marks
        start_timer()
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✓"
            check_marks.config(text=marks)

window = tk.Tk()

window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

bg_img = tk.PhotoImage(file=BACKGROUND_IMAGE)

canvas.create_image(100, 112, image=bg_img)

canvas.grid(row=1, column=1)

timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 36, "bold"))

title_label = tk.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(row=0, column=1)

start_button = tk.Button(text="Start", bg=GREEN, fg=RED, activebackground=RED, activeforeground=GREEN, font=(FONT_NAME, 12), cursor="hand2", justify="center", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = tk.Button(text="Reset", bg=GREEN, fg=RED, activebackground=RED, activeforeground=GREEN, font=(FONT_NAME, 12), cursor="hand2", justify="center", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

check_marks = tk.Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 24))
check_marks.grid(column=1, row=3)

timer = 5

window.mainloop()
