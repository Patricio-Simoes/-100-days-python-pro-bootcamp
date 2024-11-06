from turtle import Turtle

ALIGN = "left"
FONT = ("Courier Prime", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self, x_cor, y_cor):
        """
        Initializes the scoreboard object.
        @param x_cor: Represents the screen's xcor().
        @param y_cor: Represents the screen's ycor().
        """
        super().__init__()
        self.level = 0
        self.x = x_cor
        self.y = y_cor
        self.create_scoreboard()

    def create_scoreboard(self):
        """
        Creates the scoreboard.
        """
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(self.x, self.y)
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Updates the scoreboard with the current level.
        """
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)