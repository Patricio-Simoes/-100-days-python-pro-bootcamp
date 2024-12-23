from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

STARTING_POSITIONS = [(-20, 0), (0, 0), (20, 0)]

speed = 5


class Snake:
    """Represents the snake in the game."""

    def __init__(self):
        """
        Initializes a new Snake object and creates the initial segments.

        Sets up the segments of the snake based on predefined starting positions
        and assigns the head of the snake to the first segment.
        """
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """
        Creates the initial segments of the snake.

        Each segment is represented as a turtle object, positioned according to
        the predefined starting positions, and added to the segments list.
        
        :return: None
        """
        for position in STARTING_POSITIONS:
            new_seg = Turtle("square")
            new_seg.color("white")
            new_seg.penup()
            new_seg.goto(position)
            self.segments.append(new_seg)

    def move(self):
        """
        Moves the snake forward while maintaining the connection between segments.

        Each segment follows the segment in front of it, ensuring the snake's shape
        is preserved as it moves forward.
        
        :return: None
        """
        for index in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[index - 1].xcor()
            new_y = self.segments[index - 1].ycor()
            self.segments[index].goto(new_x, new_y)
        self.head.forward(speed)

    def up(self):
        """
        Changes the direction of the snake's head to up.

        The direction will only change if the snake is not currently heading down.
        
        :return: None
        """
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """
        Changes the direction of the snake's head to down.

        The direction will only change if the snake is not currently heading up.
        
        :return: None
        """
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """
        Changes the direction of the snake's head to left.

        The direction will only change if the snake is not currently heading right.
        
        :return: None
        """
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """
        Changes the direction of the snake's head to right.

        The direction will only change if the snake is not currently heading left.
        
        :return: None
        """
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
