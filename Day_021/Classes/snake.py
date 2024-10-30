from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

STARTING_SPEED = 5
STARTING_POSITIONS = [(-20,0), (0,0), (20,0)]

class Snake:

    def __init__(self):
        self.create_snake()
    
    def create_snake(self):
        self.segments = []
        self.speed = STARTING_SPEED
        for position in STARTING_POSITIONS:
            self.add_segment(position)
        self.head = self.segments[0]

    def add_segment(self, position):
        new_seg = Turtle("square")
        new_seg.color("white")
        new_seg.penup()
        new_seg.goto(position)
        self.segments.append(new_seg)

    def move(self):
        #? Method responsible for keeping segments attached when the snake turns.
        for index in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[index - 1].xcor()
            new_y = self.segments[index - 1].ycor()
            self.segments[index].goto(new_x, new_y)
        self.head.forward(self.speed)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    
    def extend(self, total):
        for i in range(total):
            self.add_segment(self.segments[-1].position())

    def reset(self):
        for seg in self.segments:
            print("Deleting segment")
            seg.hideturtle()
            del seg
        print("Reseting")
        print("Creating snake")
        self.create_snake()
