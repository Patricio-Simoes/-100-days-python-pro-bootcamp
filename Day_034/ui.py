from quiz_brain import QuizBrain

import os
import tkinter

THEME_COLOR = "#375362"

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

TRUE_IMG_FILE_PATH = os.path.join(PROJECT_DIR, "assets", "true.png")
FALSE_IMG_FILE_PATH = os.path.join(PROJECT_DIR, "assets", "false.png")


class QuizInterface:
    """Creates a GUI for the quiz application.

    This class initializes the main window and handles user interactions
    with the quiz, including displaying questions, updating the score,
    and handling button clicks.
    
    Attributes:
        quiz (QuizBrain): An instance of the QuizBrain class that manages
            the quiz logic.
        window (tkinter.Tk): The main application window.
        score_label (tkinter.Label): A label to display the current score.
        quote_canvas (tkinter.Canvas): A canvas to display the quiz questions.
        true_btn (tkinter.Button): A button for the user to select "True".
        false_btn (tkinter.Button): A button for the user to select "False".
    """
    def __init__(self, quiz_brain: QuizBrain):
        """Initializes the QuizInterface with a QuizBrain instance.

        Args:
            quiz_brain (QuizBrain): An instance of the QuizBrain class.
        """
        self.quiz = quiz_brain

        self.window = tkinter.Tk()
        self.window.resizable(False, False)

        self.window.title("Quizzler")
        self.window.config(background=THEME_COLOR, padx=20, pady=20)

        self.score_label = tkinter.Label(
            text=f"Score: {self.quiz.score}", foreground="#FFFFFF", background=THEME_COLOR
        )
        self.score_label.grid(row=0, column=1, pady=20)

        self.quote_canvas = tkinter.Canvas(width=300, height=250)
        self.quote = self.quote_canvas.create_text(
            150,
            125,
            width=280,
            font=("Arial", 16, "italic"),
            fill=THEME_COLOR,
        )
        self.quote_canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_img = tkinter.PhotoImage(file=TRUE_IMG_FILE_PATH)
        self.true_btn = tkinter.Button(image=true_img, highlightthickness=0, command=lambda: self.btn_click("true"))
        self.true_btn.grid(row=2, column=0)

        false_img = tkinter.PhotoImage(file=FALSE_IMG_FILE_PATH)
        self.false_btn = tkinter.Button(image=false_img, highlightthickness=0, command=lambda: self.btn_click("false"))
        self.false_btn.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        """Retrieves the next question from the quiz and updates the display.

        If there are still questions remaining, it updates the canvas with
        the next question. If there are no more questions, it displays a
        message indicating the end of the quiz and disables the answer buttons.
        """
        self.quote_canvas.config(background="#FFFFFF")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.quote_canvas.itemconfig(self.quote, text=q_text)
        else:
            self.quote_canvas.itemconfig(self.quote, text="You've reached the end of the quiz!")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def btn_click(self, value):
        """Handles the button click event for answering a question.

        Args:
            value (str): The value indicating the user's answer ("true" or "false").
        """
        if value == "true":
            result = self.quiz.check_answer("true")
        else:
            result = self.quiz.check_answer("false")
        if result:
            self.quote_canvas.config(background="green")
        else:
            self.quote_canvas.config(background="red")
        self.window.after(500, self.after_click)
    
    def after_click(self):
        """Updates the score and retrieves the next question after a delay."""
        self.update_score()
        self.get_next_question()
        
    def update_score(self):
        """Updates the score label to reflect the current score."""
        self.score_label.config(text=f"Score: {self.quiz.score}")