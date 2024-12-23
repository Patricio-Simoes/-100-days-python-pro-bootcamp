from turtle import Turtle

STARTING_SPEED = 2


class Ball(Turtle):
    def __init__(self):
        """
        Initializes the ball object and sets its initial properties.
        """
        super().__init__()
        self.create_ball()

    def create_ball(self):
        """
        Creates the ball with specified color and shape.

        :return: None
        """
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = STARTING_SPEED
        self.y_move = STARTING_SPEED

    def move(self):
        """
        Moves the ball in the current direction based on its speed.

        :return: None
        """
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def vertical_bounce(self):
        """
        Inverts the ball's vertical movement direction and increases its speed by 10%.

        :return: None
        """
        self.y_move *= -1.1

    def horizontal_bounce(self):
        """
        Inverts the ball's horizontal movement direction and increases its speed by 10%.

        :return: None
        """
        self.x_move *= -1.1

    def reset(self):
        """
        Resets the ball to its original position and reverts its movement direction.

        :return: None
        """
        self.x_move = STARTING_SPEED
        self.y_move = STARTING_SPEED
        self.goto(0, 0)
        self.horizontal_bounce()
