from turtle import Turtle
import time

ALIGNMENT = "center"
FONT = ("Courier Prime", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highest_score = 0
        self.FILE = "data/score.txt"
        self.read_highest_score()
        self.color("white")
        self.penup()
        self.game_start()
        self.hideturtle()

    def display(self):
        self.clear()
        self.goto(0, 200)
        self.write(f"Score = {self.score} | Highest Score = {self.highest_score}", align=ALIGNMENT, font=FONT)

    def increase(self):
        self.score += 1
        self.display()

    def game_start(self):
        self.write("Press any key to start...", align=ALIGNMENT, font=FONT)

    def game_over(self):
        """
        Brings the snake back to it's starting position and prints the GAME OVER text.
        Also, updates the highest score and saves it to the specified file.
        """
        if self.score > self.highest_score:
            self.highest_score = self.score
        self.save_highest_score()
        self.home()
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def reset(self):
        """
        Resets the scoreboard while updating the highest score.
        """
        self.score = 0
        self.display()

    def read_highest_score(self):
        """
        Tries to read the file specified in self.FILE and retrieves its data to the self.highest_score attribute.
        """
        with open(self.FILE, "r") as file:
            try:
                self.highest_score = int(file.read())
            except:
                pass

    def save_highest_score(self):
        """
        Saves the current self.highest_score to the file specified in self.FILE.
        @return:
        """
        with open(self.FILE, "w") as file:
            file.write(str(self.highest_score))
