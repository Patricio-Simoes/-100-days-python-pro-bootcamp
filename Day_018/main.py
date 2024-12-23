# The task of day 18 was creating a Hirst painting, making use of the turtle module
# and extracting the used colors from another image, using the colorgram module.

import colorgram
from turtle import Turtle, Screen
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
    Extracts a specified number of colors from a given image.

    This function uses the colorgram module to extract colors and appends them
    to the global rgb_colors list as RGB tuples.

    :param x: The number of colors to extract from the image.
    :param image: The path to the image file from which to extract colors.
    :return: None
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
    Draws a filled circle at the specified (x, y) coordinates.

    The circle is filled with a randomly chosen color from the rgb_colors list.

    :param x: The x-coordinate where the circle will be drawn.
    :param y: The y-coordinate where the circle will be drawn.
    :return: None
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
    Draws a grid of circles based on the defined number of rows and columns.

    Each circle is drawn with a radius of CIRCLE_SIZE / 2 and spaced by SPACE_SIZE.

    :return: None
    """
    print(rgb_colors)

    start_x = -((COLS - 1) * SPACE_SIZE) / 2
    start_y = -((ROWS - 1) * SPACE_SIZE) / 2

    for row in range(ROWS):
        for col in range(COLS):
            x = start_x + col * SPACE_SIZE
            y = start_y + row * SPACE_SIZE
            draw_circle(x, y)


extract_colors(20, "assets/painting.jpg")

draw_hirst()

screen.exitonclick()
