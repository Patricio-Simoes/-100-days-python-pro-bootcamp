# The task of day 18 was creating a hirst painting, making use of the turtle module and extracting the used colors from another image, using the colorgram module.

import colorgram
from turtle import *
from random import choice

CIRCLE_SIZE = 20
SPACE_SIZE = 50
ROWS = 10
COLS = 10

rgb_colors = []

turtle = Turtle()
screen = Screen()

turtle.hideturtle()
turtle.speed("fastest")
screen.colormode(255) 
turtle.penup()

def extract_colors(x, image):
    """
    Extracts x colorx from a given image and returns a tuple rgb array with them.
    """
    global rgb_colors
    colors = colorgram.extract(image, x)
    for color in colors:
        r = color.rgb[0]
        g = color.rgb[1]
        b = color.rgb[2]
        rgb = (r, g, b)
        rgb_colors.append(rgb)

def draw_circle(x, y):
    """
    Given x and y coordinates, turtle moves to them and draws a circle.
    """
    color = choice(rgb_colors)
    turtle.color(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(CIRCLE_SIZE / 2)
    turtle.end_fill()
    turtle.penup()

def draw_hirst():
    """
    Draws a grid of ROWS x COLS and inside it, draws ROWS x COLS circles,
    of radius CIRCLE_SIZE / 2, each spaced by SPACE_SIZE.
    """
    print(rgb_colors)

    start_x = -((COLS - 1) * SPACE_SIZE) / 2
    start_y = -((ROWS - 1) * SPACE_SIZE) / 2

    for row in range(ROWS):
        for col in range(COLS):
            x = start_x + col * SPACE_SIZE
            y = start_y + row * SPACE_SIZE
            draw_circle(x, y)

extract_colors(20,'assets/painting.jpg')

draw_hirst()

screen.exitonclick()