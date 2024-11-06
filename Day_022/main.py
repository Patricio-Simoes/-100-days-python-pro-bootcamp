# The task for day 22 was creating the classic Pong game using Python's turtle module.

from Classes.ball import Ball
from Classes.player import Player
from Classes.scoreboard import Scoreboard
from Classes.window import Window

import time

BALL_PLAYER_COLLISION_DISTANCE = 50
BALL_PLAYER_COLLISION_X_BUFFER = 355
SCREEN_REFRESH_TIMER = 0.015


def on_key_press():
    global key_pressed
    key_pressed = True


def hold_screen():
    """
    * Holds the screen on stand by until the player presses any key.
    """
    global window

    for key in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3',
                '4', '5', '6', '7', '8', '9', 'space', 'Return',
                'Up', 'Down', 'Left', 'Right']:
        window.screen.onkey(on_key_press, key)

    window.screen.listen()

    while not key_pressed:
        window.screen.update()


window = Window()

scoreboard = Scoreboard(window.HEIGHT)

ball = Ball()

HORIZONTAL_EDGE = window.WIDTH / 2
VERTICAL_EDGE = window.HEIGHT / 2

PLAYER_ONE_X_COR = HORIZONTAL_EDGE - 25
PLAYER_TWO_X_COR = -HORIZONTAL_EDGE + 25

# Adding/Removing 25, (20 + 5) because that's the correspondent to the paddle's width.
player_one = Player(PLAYER_ONE_X_COR, VERTICAL_EDGE)
player_two = Player(PLAYER_TWO_X_COR, VERTICAL_EDGE)

key_pressed = False

hold_screen()

scoreboard.update_scoreboard()

while True:
    window.screen.update()
    time.sleep(SCREEN_REFRESH_TIMER)

    window.screen.listen()
    window.screen.onkey(player_one.go_up, "Up")
    window.screen.onkey(player_one.go_down, "Down")
    window.screen.onkey(player_two.go_up, "w")
    window.screen.onkey(player_two.go_down, "s")

    # Detects collision with vertical edges.
    if ball.ycor() >= (window.HEIGHT / 2 - 10) or ball.ycor() <= (-(window.HEIGHT / 2) + 10):
        ball.vertical_bounce()

    # Detects collision with paddles.
    if (ball.distance(player_one) < BALL_PLAYER_COLLISION_DISTANCE and ball.xcor() > BALL_PLAYER_COLLISION_X_BUFFER or
            ball.distance(player_two) < BALL_PLAYER_COLLISION_DISTANCE and
            ball.xcor() < -BALL_PLAYER_COLLISION_X_BUFFER):
        ball.horizontal_bounce()

    # Detects when the right paddle misses.
    if ball.xcor() > PLAYER_ONE_X_COR + 20:
        scoreboard.score("player_two")
        ball.reset()

    # Detects when the left paddle misses.
    if ball.xcor() < PLAYER_TWO_X_COR - 20:
        scoreboard.score("player_one")
        ball.reset()

    ball.move()
