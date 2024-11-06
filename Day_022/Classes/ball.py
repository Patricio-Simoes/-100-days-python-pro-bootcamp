from turtle import Turtle

STARTING_SPEED = 2


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()

    def create_ball(self):
        """Creates the ball.
        """
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = STARTING_SPEED
        self.y_move = STARTING_SPEED

    def move(self):
        """Moves the ball.
        """
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def vertical_bounce(self):
        """Bounces the ball by inverting the movement on y coordinates.
        Additionally, increases the current ball speed by 10%.
        """
        self.y_move *= -1.1

    def horizontal_bounce(self):
        """Bounces the ball by inverting the movement on x coordinates.
        Additionally, increases the current ball speed by 10%.
        """
        self.x_move *= -1.1

    def reset(self):
        """Resets the ball back to its original position and reverts the bouncing direction.
        """
        self.x_move = STARTING_SPEED
        self.y_move = STARTING_SPEED
        self.goto(0, 0)
        self.horizontal_bounce()
