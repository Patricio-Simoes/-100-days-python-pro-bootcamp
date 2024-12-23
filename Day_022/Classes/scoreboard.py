from turtle import Turtle

ALIGN = "Center"
FONT = ("Courier Prime", 32, "normal")


class Scoreboard(Turtle):
    def __init__(self, height):
        """
        Initializes the scoreboard object and sets up the initial score.

        :param height: The height of the game window, used for positioning the scoreboard.
        """
        super().__init__()
        self.height = height
        self.create_scoreboard()
        self.game_start()

    def create_scoreboard(self):
        """
        Sets up the scoreboard's appearance and initializes player scores.

        :return: None
        """
        self.color("white")
        self.penup()
        self.hideturtle()
        self.player_one_score = 0
        self.player_two_score = 0

    def update_scoreboard(self):
        """
        Updates the scoreboard display after a player scores.

        :return: None
        """
        self.clear()
        self.goto(self.xcor(), self.height / 2 - 75)
        self.write(
            f"{self.player_two_score} - {self.player_one_score}", align=ALIGN, font=FONT
        )

    def score(self, player):
        """
        Increments the score for the specified player.

        :param player: Identifies the player ("player_one" or "player_two").
        :return: None
        """
        if player == "player_one":
            self.player_one_score += 1
        else:
            self.player_two_score += 1
        self.update_scoreboard()

    def game_start(self):
        """
        Displays a message prompting the user to press a key to start the game.

        :return: None
        """
        self.write(
            "Press any key to start...",
            align=ALIGN,
            font=("Courier Prime", 24, "normal"),
        )
