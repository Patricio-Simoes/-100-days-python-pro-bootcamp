# The task of day 19 was mini-racing bet game using the turtle module.

from turtle import Turtle, Screen
from random import randint


def get_bet():
    """
    Retrieves the user's bet input.

    Prompts the user to select a turtle (1-6) that they believe will win the race.
    The input is validated to ensure it is one of the allowed options.

    :return: None
    """
    global bet
    while bet not in ["1", "2", "3", "4", "5", "6"]:
        bet = screen.textinput(
            title="Place your bet",
            prompt="Which turtle will win the race?\n[1].Red\n[2].Orange\n[3].Yellow\n[4].Green\n[5].Blue\n[6].Purple",
        )


def spawn_turtles():
    """
    Spawns the turtles for the race.

    Creates turtle objects for each color defined in the COLORS list,
    positions them at the starting line, and adds them to the turtles list.

    :return: None
    """
    global turtles
    for i in range(len(COLORS)):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(COLORS[i])
        new_turtle.penup()
        new_turtle.goto(x=-230, y=POSITIONS[i])
        turtles.append(new_turtle)


def race():
    """
    Conducts the turtle race.

    Moves each turtle forward by a random distance until one of them reaches
    the finish line (x-coordinate >= 230). The index of the winning turtle is stored.

    :return: None
    """
    global winner
    is_race_on = True  # Flags the race as ongoing.

    while is_race_on:
        for i in range(len(COLORS)):
            turtles[i].forward(randint(0, 10))
            if turtles[i].xcor() >= 230:
                winner = i
                is_race_on = False


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
POSITIONS = [-75, -45, -15, 15, 45, 75]
HEIGHT = 500
WIDTH = 400

turtles = []
bet = ""
winner = ""

screen = Screen()
screen.setup(HEIGHT, WIDTH)
screen.bgcolor("black")

get_bet()
spawn_turtles()
race()

if winner == bet:
    print("Congratulations, you've won the bet!")
else:
    print(f"The winner was {COLORS[winner]}, better luck next time!")

screen.exitonclick()
