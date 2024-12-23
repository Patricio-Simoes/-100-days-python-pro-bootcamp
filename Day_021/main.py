# The task for day 21 was completing the snake game started on day 20 using the turtle module and OOP concepts.
# Some modifications were made to the starting code to slightly improve user experience and
# provide a game reset mechanism.

from Classes.food import Food
from Classes.scoreboard import Scoreboard
from Classes.snake import Snake
from Classes.window import Window

import time

FOOD_DISTANCE_BUFFER = 10
GAME_OVER_COR = 235
MAX_SPEED = 15
SCREEN_REFRESH_TIMER = 0.05
SEGMENT_MODIFIER = 2
SPEED_MODIFIER = 1.10
TAIL_DISTANCE_BUFFER = 1


def on_key_press():
    """Sets the key_pressed flag to True when a key is pressed."""
    global key_pressed
    key_pressed = True


def hold_screen():
    """
    Holds the screen on standby until the player presses any key.

    This function listens for key presses and updates the screen until a key is pressed.
    """
    global window

    for key in [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "space",
        "Return",
        "Up",
        "Down",
        "Left",
        "Right",
    ]:
        window.screen.onkey(on_key_press, key)

    window.screen.listen()

    while not key_pressed:
        window.screen.update()


def has_snake_eaten_food():
    """
    Checks if the snake's head has eaten food.

    If food is eaten, refreshes the food position, extends the snake,
    and increases the snake's speed if it is below the maximum speed.

    :return: None
    """
    if snake.head.distance(food) <= FOOD_DISTANCE_BUFFER:
        food.refresh()
        snake.extend(SEGMENT_MODIFIER)
        if snake.speed < MAX_SPEED:
            snake.speed *= SPEED_MODIFIER
        scoreboard.increase()


def has_snake_reached_boudaries():
    """
    Checks if the snake's head has reached the window boundaries.

    :return: True if the snake has reached the boundaries, otherwise False.
    """
    if (
        snake.head.xcor() > GAME_OVER_COR
        or snake.head.xcor() < -GAME_OVER_COR
        or snake.head.ycor() > GAME_OVER_COR
        or snake.head.ycor() < -GAME_OVER_COR
    ):
        return True


def has_snake_hit_tail():
    """
    Checks if the snake's head has collided with its tail.

    :return: True if the snake has hit its tail, otherwise False.
    """
    global is_game_on
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) <= TAIL_DISTANCE_BUFFER:
            return True


def game_over():
    """
    Ends the game and displays the game over message.

    :return: None
    """
    global is_game_on
    scoreboard.game_over()


#####################
# Game starts here. #
#####################

scoreboard = Scoreboard()
window = Window()

key_pressed = False

hold_screen()

food = Food()
snake = Snake()

scoreboard.display()

is_game_on = True

while is_game_on:
    window.screen.onkey(snake.up, "Up")
    window.screen.onkey(snake.down, "Down")
    window.screen.onkey(snake.left, "Left")
    window.screen.onkey(snake.right, "Right")
    window.screen.update()
    time.sleep(SCREEN_REFRESH_TIMER)
    snake.move()

    has_snake_eaten_food()

    if has_snake_reached_boudaries() or has_snake_hit_tail():
        game_over()
        window.screen.delay(500)
        key_pressed = False
        hold_screen()
        scoreboard.reset()
        snake.reset()
