from turtle import Turtle
import time

ALIGNMENT = "center"
FONT = ("Courier Prime", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.game_start()
        self.hideturtle()

    def display(self):
        self.clear()
        self.goto(0, 200)
        self.write(f"Score = {self.score}", align=ALIGNMENT, font=FONT)

    def increase(self):
        self.score += 1
        self.display()

    def game_start(self):
        self.write("Press any key to start...", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def reset(self):
        self.score = 0
        self.display()
