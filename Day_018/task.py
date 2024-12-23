from turtle import Turtle, Screen
from random import randint, choice

def draw_shape(sides):
    steps = 100
    angle = 360/sides
    for i in range(sides):
        turtle.forward(steps)
        turtle.left(angle)

def draw_shapes():
    colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "brown", "cyan"]
    i = 0
    while i < 9:
        turtle.color(colors[i])
        draw_shape(i+3)
        i += 1

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)

def random_walk(steps):
    directions = [0, 90, 180, 270]
    i = 0
    turtle.pensize(8)
    screen.colormode(255)
    while i < steps:
        turtle.color(random_color())
        turtle.left(choice(directions))
        turtle.forward(15)
        i += 1

def draw_spirograph():
    i = 1
    while i <= 36:
        turtle.circle(100)
        turtle.left(10)
        i += 1

turtle = Turtle()
turtle.speed(10)
screen = Screen()

screen.bgcolor("black")
turtle.color("white")

draw_spirograph()

screen.exitonclick()