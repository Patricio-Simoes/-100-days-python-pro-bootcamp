from turtle import Turtle
from random import randint, randrange

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

X_SCREEN_EDGE_BUFFER = 0
Y_SCREEN_EDGE_BUFFER = 40


class Car(Turtle):
    def __init__(self, x_edge, y_edge, x_stretch, y_stretch, speed, random=False):
        """
        Initializes a car object.

        :param x_edge: Horizontal edge limit for car generation.
        :param y_edge: Vertical edge limit for car generation.
        :param x_stretch: Width proportion for the car's shape.
        :param y_stretch: Height proportion for the car's shape.
        :param speed: Current move speed of the car.
        :param random: If True, places the car randomly; otherwise, places it at the edge.
        """
        super().__init__()
        self.move_distance = speed
        self.x_edge = x_edge - X_SCREEN_EDGE_BUFFER
        self.y_edge = y_edge - Y_SCREEN_EDGE_BUFFER
        self.height_stretch = y_stretch
        self.width_stretch = x_stretch
        self.speed = speed
        self.create_car()
        if random:
            self.place_starting_car()
        else:
            self.place_car()

    def create_car(self):
        """
        Creates the car shape and sets its properties.

        :return: None
        """
        self.shape("square")
        self.shapesize(self.width_stretch, self.height_stretch)
        self.penup()
        self.setheading(180)
        self.color(COLORS[randrange(len(COLORS))])

    def place_starting_car(self):
        """
        Places the car at random x and y positions within the screen limits.

        :return: None
        """
        new_x = randint(int(-self.x_edge), int(self.x_edge))
        new_y = randint(int(-self.y_edge), int(self.y_edge))
        self.goto(new_x, new_y)

    def place_car(self):
        """
        Places the car at the horizontal edge of the screen with a random y position.

        :return: None
        """
        new_x = self.x_edge
        new_y = randint(int(-self.y_edge), int(self.y_edge))
        self.goto(new_x, new_y)

    def move(self):
        """
        Moves the car left by its current speed.

        :return: None
        """
        self.goto(self.xcor() - self.move_distance, self.ycor())

    def remove_car(self):
        """
        Removes the car from the screen by hiding it and deleting the instance.

        :return: None
        """
        self.hideturtle()
        del self
