from turtle import Turtle

STARTING_POSITION = (0, -260)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

COLOR = "white"
SPEED = 20


class Player(Turtle):
    def __init__(self):
        """
        Initializes the player object and sets up the turtle.

        :return: None
        """
        super().__init__()
        self.create_turtle()

    def create_turtle(self):
        """
        Creates the player's turtle with specified shape, color, and starting position.

        :return: None
        """
        self.shape("turtle")
        self.color(COLOR)
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)

    def go_up(self):
        """
        Moves the player up by the defined move distance.

        :return: None
        """
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def go_down(self):
        """
        Moves the player down by the defined move distance,
        but prevents moving below the starting position.

        :return: None
        """
        new_y = self.ycor() - MOVE_DISTANCE
        if new_y > STARTING_POSITION[1]:
            self.goto(self.xcor(), new_y)

    def go_to_starting_position(self):
        """
        Resets the player's turtle to the starting position.

        :return: None
        """
        self.goto(STARTING_POSITION)
