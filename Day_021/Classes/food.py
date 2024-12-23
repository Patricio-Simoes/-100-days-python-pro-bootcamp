from turtle import Turtle
import random


class Food(Turtle):
    """Represents the food in the snake game, inheriting from Turtle."""

    def __init__(self):
        """
        Initializes a new Food object and generates its appearance.

        Calls the generate method to set up the food's shape and appearance,
        and then calls refresh to place it at a random location.
        """
        super().__init__()
        self.generate()
        self.refresh()

    def generate(self):
        """
        Sets the appearance of the food.

        Configures the food's shape, color, and size.
        """
        self.shape("circle")
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.shapesize(0.5, 0.5)

    def refresh(self):
        """
        Moves the food to a new random location on the screen.

        The new position is generated within the bounds of the game area.
        """
        random_x = random.randint(-230, 230)
        random_y = random.randint(-230, 200)
        self.goto(random_x, random_y)
