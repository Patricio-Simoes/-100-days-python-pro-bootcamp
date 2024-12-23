from turtle import *
import time

WIDTH = 600
HEIGHT = 600
STEPS = 20

def spawn_snake():
    """
    Spawns the initial snake with 3 turtles attached to each other.
    """
    global snake
    for i in range(0,3):
        new_segment = Turtle()
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(starting_positions[i])
        segments.append(new_segment)

screen = Screen()

starting_positions = [(20, 0), (0, 0), (-20, 0)]

segments = []

is_game_on = True

screen.tracer(0)
screen.bgcolor("black")
screen.title("Snake Game")

spawn_snake()

while is_game_on:
    time.sleep(0.1)
    screen.update()
    #? Moves each segment to the next segment's coordinates.
    #? (This is the logic that makes the snake move without losing segments).
    for seg in range(len(segments) - 1, 0, -1):
        new_x = segments[seg - 1].xcor()
        new_y = segments[seg - 1].ycor()
        segments[seg].goto(new_x, new_y)
    segments[0].forward(STEPS)

screen.exitonclick()