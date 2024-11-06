from turtle import Turtle
from random import randint, randrange

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

X_SCREEN_EDGE_BUFFER = 0
Y_SCREEN_EDGE_BUFFER = 40


class Car(Turtle):
    def __init__(self, x_edge, y_edge, x_stretch, y_stretch, speed, random=False):
        """
        Initializes the car object.
        @param x_edge: Indicates horizontal edges where cars can be generated.
        @param y_edge: Indicates vertical edges where cars can be generated.
        @param x_stretch: Indicates the width proportion that the car's square shape should be stretched by.
        @param y_stretch: Indicates the height proportion that the car's square shape should be stretched by.
        @param speed: Indicates the car's current move speed.
        @param random: Indicates if the car should be placed randomly, (True for the starting cars, False otherwise).
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
        Creates the car.
        """
        self.shape("square")
        self.shapesize(self.width_stretch, self.height_stretch)
        self.penup()
        self.setheading(180)
        self.color(COLORS[randrange(len(COLORS))])

    def place_starting_car(self):
        """
        Places a car at a random x and y positions.
        """
        new_x = randint(int(-self.x_edge), int(self.x_edge))
        new_y = randint(int(-self.y_edge), int(self.y_edge))
        self.goto(new_x, new_y)

    def place_car(self):
        """
        Places a car at the horizontal edge of the screen.
        """
        new_x = self.x_edge
        new_y = randint(int(-self.y_edge), int(self.y_edge))
        self.goto(new_x, new_y)

    def move(self):
        """
        Moves the car by its current speed, (level based).
        """
        self.goto(self.xcor() - self.move_distance, self.ycor())

    def remove_car(self):
        """
        Removes the car from the screen by killing the corresponding turtle.
        """
        self.hideturtle()
        del self
