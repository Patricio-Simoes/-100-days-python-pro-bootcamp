from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

STARTING_SPEED = 5
STARTING_POSITIONS = [(-20, 0), (0, 0), (20, 0)]


class Snake:
    """Represents the snake in the game."""

    def __init__(self):
        """
        Initializes a new Snake object and creates the initial segments.

        Calls the create_snake method to set up the initial position and segments of the snake.
        """
        self.create_snake()

    def create_snake(self):
        """
        Creates the initial segments of the snake.

        Sets the starting speed and initializes the segments based on the predefined starting positions.
        The head of the snake is set to the first segment.
        """
        self.segments = []
        self.speed = STARTING_SPEED
        for position in STARTING_POSITIONS:
            self.add_segment(position)
        self.head = self.segments[0]

    def add_segment(self, position):
        """
        Adds a new segment to the snake at the specified position.

        :param position: A tuple representing the (x, y) coordinates for the new segment.
        :return: None
        """
        new_seg = Turtle("square")
        new_seg.color("white")
        new_seg.penup()
        new_seg.goto(position)
        self.segments.append(new_seg)

    def move(self):
        """
        Moves the snake forward while keeping the segments attached.

        Each segment follows the segment in front of it, maintaining the snake's shape.
        :return: None
        """
        for index in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[index - 1].xcor()
            new_y = self.segments[index - 1].ycor()
            self.segments[index].goto(new_x, new_y)
        self.head.forward(self.speed)

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

    def extend(self, total):
        """
        Extends the snake by adding a specified number of segments.

        Each new segment is added at the position of the last segment.

        :param total: The number of segments to add.
        :return: None
        """
        for i in range(total):
            self.add_segment(self.segments[-1].position())

    def reset(self):
        """
        Resets the snake by hiding and deleting all segments, then recreating the snake.

        :return: None
        """
        for seg in self.segments:
            seg.hideturtle()
            del seg
        self.create_snake()
