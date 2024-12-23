import time
from turtle import Screen
from Classes.player import Player
from Classes.car import Car
from Classes.scoreboard import Scoreboard


def tick(timer):
    """
    Refreshes the screen and updates game state.

    :param timer: Frequency of the tick in seconds.
    :return: True if the game continues, False if a collision occurs.
    """
    global ticks
    ticks += 1
    time.sleep(timer)
    screen.update()
    is_player_at_edge()
    move_cars()
    add_car()
    for car in cars:
        if check_collision(car):
            return False
    return True


def increase_level():
    """
    Increases the game level, updating the scoreboard and car speed.

    :return: None
    """
    global cars, car_add_tick_rate

    player.go_to_starting_position()
    scoreboard.update_scoreboard()

    if car_add_tick_rate > MIN_CAR_ADD_TICK_RATE:
        car_add_tick_rate -= CAR_ADD_DECREASE_TICK_RATE

    # Increases the current cars speed rate.
    for car in cars:
        car.move_distance = scoreboard.level * STARTING_CAR_MOVE_DISTANCE


def add_car():
    """
    Adds a new car to the game if the tick count is divisible by the car spawn rate.

    :return: None
    """
    global ticks, car_add_tick_rate
    if ticks % car_add_tick_rate == 0:
        ticks = 0
        cars.append(
            Car(
                SCREEN_X_EDGE,
                SCREEN_Y_EDGE,
                CAR_STRETCH_WIDTH,
                CAR_STRETCH_HEIGHT,
                STARTING_CAR_MOVE_DISTANCE * scoreboard.level,
            )
        )


def remove_car(car):
    """
    Removes a specified car from the game.

    :param car: The car object to be removed.
    :return: None
    """
    global cars
    car.remove_car()
    cars.remove(car)


def move_cars():
    """
    Moves all existing cars across the screen.

    :return: None
    """
    for car in cars:
        car.move()
        # The car has reached the horizontal edge and must be de-spawned.
        if car.xcor() <= -SCREEN_X_EDGE:
            remove_car(car)


def is_player_at_edge():
    """
    Checks if the player's turtle has reached the top edge of the screen.

    :return: None
    """
    if player.ycor() >= SCREEN_Y_EDGE:
        # The player has reached the end of the level.
        increase_level()


def check_collision(car):
    """
    Checks for a collision between the player and a specified car.

    :param car: The car object to check for collision.
    :return: True if a collision occurs, False otherwise.
    """
    player_x = player.xcor()
    player_y = player.ycor()

    car_x = car.xcor()
    car_y = car.ycor()

    car_width = 20 * CAR_STRETCH_WIDTH
    car_height = 20 * CAR_STRETCH_HEIGHT

    if (
        car_x - car_width / 2 < player_x < car_x + car_width / 2
        and car_y - car_height / 2 < player_y < car_y + car_height / 2
    ):
        return True
    return False


###########################
# Game tweaking variables #
###########################

SCREEN_BACKGROUND_COLOR = "black"
SCREEN_EDGE_DISTANCE_X_BUFFER = 25
SCREEN_EDGE_DISTANCE_Y_BUFFER = 50
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 600
SCREEN_X_EDGE = (SCREEN_WIDTH / 2) - SCREEN_EDGE_DISTANCE_X_BUFFER
SCREEN_Y_EDGE = (SCREEN_HEIGHT / 2) - SCREEN_EDGE_DISTANCE_Y_BUFFER

CAR_ADD_TICK_RATE = 60  # CAR_SPAWN_TIMER_MAX_RATE * TICK_TIMER = Time in seconds
CAR_ADD_DECREASE_TICK_RATE = 10  # Decrease amount for car add tick rate per level.
MIN_CAR_ADD_TICK_RATE = 10
CAR_STRETCH_HEIGHT = 1.5
CAR_STRETCH_WIDTH = 1

COLLISION_DISTANCE_BUFFER = 15

STARTING_CAR_MOVE_DISTANCE = 0.75
STARTING_CARS = 10

TICK_TIMER = 0.01

########
# Game #
########

cars = []

ticks = 0

car_add_tick_rate = CAR_ADD_TICK_RATE

# Screen setup.

screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor(SCREEN_BACKGROUND_COLOR)
screen.tracer(0)

scoreboard = Scoreboard(-SCREEN_X_EDGE, SCREEN_Y_EDGE)

player = Player()

# Generates the initials cars.

for i in range(STARTING_CARS):
    new_car = Car(
        SCREEN_X_EDGE,
        SCREEN_Y_EDGE,
        CAR_STRETCH_WIDTH,
        CAR_STRETCH_HEIGHT,
        STARTING_CAR_MOVE_DISTANCE,
        True,
    )
    cars.append(new_car)

screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")

is_game_on = True

while is_game_on:
    if not tick(TICK_TIMER):
        is_game_on = False

scoreboard.game_over()

screen.exitonclick()
