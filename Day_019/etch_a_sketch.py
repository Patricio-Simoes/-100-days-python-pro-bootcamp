from turtle import Turtle, Screen

STEPS = 30
TURN = 15

tim = Turtle()
screen = Screen()

tim.speed(1)


def up():
    """
    Moves the turtle forward in the north direction.

    Sets the turtle's heading to 90 degrees (up) and moves it forward by a predefined number of steps.

    :return: None
    """
    tim.setheading(90)
    tim.forward(STEPS)


def down():
    """
    Moves the turtle forward in the south direction.

    Sets the turtle's heading to 270 degrees (down) and moves it forward by a predefined number of steps.

    :return: None
    """
    tim.setheading(270)
    tim.forward(STEPS)


def left():
    """
    Turns the turtle to the left and moves it forward.

    Adjusts the turtle's heading by adding a predefined turn angle and then moves it forward by a predefined number of steps.

    :return: None
    """
    tim.setheading(tim.heading() + TURN)
    tim.forward(STEPS)


def right():
    """
    Turns the turtle to the right and moves it forward.

    Adjusts the turtle's heading by subtracting a predefined turn angle and then moves it forward by a predefined number of steps.

    :return: None
    """
    tim.setheading(tim.heading() - TURN)
    tim.forward(STEPS)


def clear():
    """
    Clears the turtle's drawings and resets its position.

    Lifts the pen, returns the turtle to the home position, and puts the pen down again.

    :return: None
    """
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
