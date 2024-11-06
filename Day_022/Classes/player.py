from turtle import Turtle

COLOR = "white"
SPEED = 50

STRETCH_HEIGHT = 1
STRETCH_WIDTH = 5


class Player(Turtle):
    def __init__(self, HORIZONTAL_EDGE, VERTICAL_EDGE):
        super().__init__()
        self.HORIZONTAL_EDGE = HORIZONTAL_EDGE
        self.VERTICAL_EDGE = VERTICAL_EDGE
        self.create_paddle()

    def create_paddle(self):
        """Creates the player's paddle turtle.
        """
        self.shape("square")
        self.color(COLOR)
        self.shapesize(STRETCH_WIDTH, STRETCH_HEIGHT)
        self.penup()
        self.goto(self.HORIZONTAL_EDGE, 0)

    def go_up(self):
        """Moves the player's paddle up.
        """
        if self.ycor() < self.VERTICAL_EDGE - 95:
            self.goto(self.HORIZONTAL_EDGE, self.ycor() + SPEED)

    def go_down(self):
        """Moves the player's paddle down.
        """
        if self.ycor() > -self.VERTICAL_EDGE + 95:
            self.goto(self.HORIZONTAL_EDGE, self.ycor() - SPEED)
