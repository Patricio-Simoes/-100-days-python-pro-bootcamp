from turtle import Turtle

ALIGN = "left"
FONT = ("Courier Prime", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self, x_cor, y_cor):
        """
        Initializes the scoreboard object.

        :param x_cor: The x-coordinate for the scoreboard's position.
        :param y_cor: The y-coordinate for the scoreboard's position.
        """
        super().__init__()
        self.level = 0
        self.x = x_cor
        self.y = y_cor
        self.create_scoreboard()

    def create_scoreboard(self):
        """
        Sets up the scoreboard's appearance and initial display.

        :return: None
        """
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(self.x, self.y)
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Increments the level and updates the scoreboard display.

        :return: None
        """
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align=ALIGN, font=FONT)

    def game_over(self):
        """
        Displays the game over message at the center of the screen.

        :return: None
        """
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
