from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier Prime", 16, "normal")


class Scoreboard(Turtle):
    """Represents the scoreboard for the snake game, inheriting from Turtle."""

    def __init__(self):
        """
        Initializes a new Scoreboard object.

        Sets the initial score and highest score, reads the highest score from a file,
        and prepares the scoreboard for display.
        """
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
        """
        Clears the scoreboard and displays the current score and highest score.

        :return: None
        """
        self.clear()
        self.goto(0, 200)
        self.write(
            f"Score = {self.score} | Highest Score = {self.highest_score}",
            align=ALIGNMENT,
            font=FONT,
        )

    def increase(self):
        """
        Increases the score by one and updates the display.

        :return: None
        """
        self.score += 1
        self.display()

    def game_start(self):
        """
        Displays a message prompting the player to start the game.

        :return: None
        """
        self.write("Press any key to start...", align=ALIGNMENT, font=FONT)

    def game_over(self):
        """
        Ends the game, displays the GAME OVER message, and updates the highest score.

        If the current score exceeds the highest score, it updates the highest score
        and saves it to the specified file.

        :return: None
        """
        if self.score > self.highest_score:
            self.highest_score = self.score
        self.save_highest_score()
        self.home()
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def reset(self):
        """
        Resets the current score to zero and updates the display.

        :return: None
        """
        self.score = 0
        self.display()

    def read_highest_score(self):
        """
        Reads the highest score from the specified file and updates the highest_score attribute.

        If the file cannot be read or contains invalid data, the highest score remains unchanged.

        :return: None
        """
        with open(self.FILE, "r") as file:
            try:
                self.highest_score = int(file.read())
            except ValueError:
                pass

    def save_highest_score(self):
        """
        Saves the current highest score to the specified file.

        :return: None
        """
        with open(self.FILE, "w") as file:
            file.write(str(self.highest_score))
