# The task of day 19 was mini-racing bet game using the turtle module.

from turtle import *
from random import randint

def get_bet():
    """
    Retrieves the user's bet input.
    """
    global bet
    while bet not in ["1", "2", "3", "4", "5", "6"]:
        bet = screen.textinput(
            title="Place your bet",
            prompt="Which turtle will win the race?\n[1].Red\n[2].Orange:\n[3].Yellow\n[4].Green\n[5].Blue\n[6].Purple",
        )

def spawn_turtles():
    """
    Spawns the turtles.
    """
    global turtles
    for i in range(len(COLORS)):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(COLORS[i])
        new_turtle.penup()
        new_turtle.goto(x=-230, y=POSITIONS[i])
        turtles.append(new_turtle)

def race():
    global winner
    #? Flags the race as ongoing.
    is_race_on = True
    #? Ongoing loop until a turtle as reached the end, (cor with x = 230)
    while is_race_on == True:
        for i in range(len(COLORS)):
            turtles[i].forward(randint(0,10))
            if turtles[i].xcor() >= 230:
                winner = i
                is_race_on = False

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
POSITIONS = [-75, -45, -15, 15, 45, 75]
HEIGHT = 500
WIDTH = 400

turtles = []
i = 0
bet = ""
is_race_on = False
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
