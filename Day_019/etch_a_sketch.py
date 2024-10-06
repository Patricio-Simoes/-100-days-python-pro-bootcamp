from turtle import *

STEPS = 30
TURN = 15

tim = Turtle()
screen = Screen()

tim.speed(1)

def up():
    """
    Sets the turtle's heading to north and moves it forward.
    """
    tim.setheading(90)
    tim.forward(STEPS)

def down():
    """
    Sets the turtle's heading to south and moves it forward.
    """
    tim.setheading(270)
    tim.forward(STEPS)

def left():
    """
    Turns the turtle to the left.
    """
    tim.setheading(tim.heading() + TURN)
    tim.forward(STEPS)

def right():
    """
    Turns the turtle to the right.
    """
    tim.setheading(tim.heading() - TURN)
    tim.forward(STEPS)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()

screen.onkey(up, "w")
screen.onkey(down, "s")
screen.onkey(left, "a")
screen.onkey(right, "d")
screen.onkey(clear, "c")

screen.exitonclick()
