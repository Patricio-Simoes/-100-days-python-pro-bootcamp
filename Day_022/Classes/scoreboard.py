from turtle import Turtle

ALIGN = "Center"
FONT = ("Courier Prime", 32, "normal")


class Scoreboard(Turtle):
    def __init__(self, height):
        super().__init__()
        self.height = height
        self.create_scoreboard()
        self.game_start()

    def create_scoreboard(self):
        """Creates the scoreboard.
        """
        self.color("white")
        self.penup()
        self.hideturtle()
        self.player_one_score = 0
        self.player_two_score = 0

    def update_scoreboard(self):
        """Updates the scoreboard after a player scores.
        """
        self.clear()
        self.goto(self.xcor(), self.height / 2 - 75)
        self.write(f"{self.player_two_score} - {self.player_one_score}", align=ALIGN, font=FONT)

    def score(self, player):
        """Scores a point for the player

        Args:
            player (String): Identifies the player. Either player_one or player_two.
        """
        if player == "player_one":
            self.player_one_score += 1
        else:
            self.player_two_score += 1
        self.update_scoreboard()

    def game_start(self):
        """Holds the game and awaits for the the user to press a key.
        """
        self.write("Press any key to start...", align=ALIGN, font=("Courier Prime", 24, "normal"))
