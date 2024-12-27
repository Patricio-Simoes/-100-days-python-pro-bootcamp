import os
import pandas
from turtle import Turtle, Screen

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
BACKGROUND_IMAGE = os.path.join(PROJECT_DIR, "assets", "blank_states_img.gif")
STATES_FILE = os.path.join(PROJECT_DIR, "data", "50_states.csv")


def read_states_file():
    """
    Read a CSV file containing state names and their coordinates.

    This function loads state names along with their x and y coordinates
    from a CSV file specified by the `STATES_FILE` variable.
    It returns a dataframe containing the relevant data.

    :return: DataFrame containing state names and coordinates.
    """
    states = pandas.read_csv(STATES_FILE)
    return states


def setup():
    """
    Initialize the game screen for the U.S. States Game.

    This function sets the title of the game window, loads the background image
    of a blank U.S. map, and configures the screen size for the game.
    It should be called before starting the game to ensure proper setup.

    :return: None
    """
    screen.title("U.S States Game")
    screen.bgpic(BACKGROUND_IMAGE)
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)


def check_user_input(user_input):
    """
    Check if the user input matches a valid state name.

    This function verifies if the provided input corresponds to a valid state name
    in the predefined list of state names (`states_list`). If a match is found,
    it returns True, else, returns False.

    If the user's input equals "exit", calls the exit_game() function.

    :param user_input: The name of the state entered by the user (str).
    :return: True if the input matches a state name, otherwise False.
    """
    if user_input == "exit":
        exit_game()
    elif user_input in states_list:
        return True
    else:
        return False


def draw_state_name(state_name, x_cor, y_cor):
    """
    Draw the name of the state on the screen at specified coordinates.

    This function uses the Turtle graphics library to write the state's name
    at the given x and y coordinates on the screen.

    :param state_name: The name of the state to be drawn (str).
    :param x_cor: The x-coordinate for the state's name (int).
    :param y_cor: The y-coordinate for the state's name (int).
    :return: None
    """
    lincoln.goto(x_cor, y_cor)
    lincoln.write(state_name.capitalize(), align="center", font=("Arial", 8, "normal"))


def exit_game():
    """
    Exits the game and saves the states that have not been guessed.

    This function creates a list of states that are missing from the
    guessed states and saves this list to a CSV file named
    'states_to_learn.csv' in the 'data' directory of the project.

    Returns:
        None
    """
    missing_states = [state for state in states_list if state not in guessed_states]
    indexed_states = [(index + 1, state) for index, state in enumerate(missing_states)]
    new_data = pandas.DataFrame(indexed_states, columns=["Number", "State"])
    new_data.to_csv(
        os.path.join(PROJECT_DIR, "data", "states_to_learn.csv"), index=False
    )
    return None


screen = Screen()

lincoln = Turtle()
lincoln.hideturtle()
lincoln.penup()

score = 0
setup()

STATES_DATAFRAME = read_states_file()
guessed_states = []
states_list = STATES_DATAFRAME["state"].str.lower().tolist()

TOTAL_STATES = len(states_list)

##################
# Main game loop #
##################

while score < TOTAL_STATES:
    user_input = screen.textinput(
        title=f"{len(guessed_states)}/{TOTAL_STATES} States correct",
        prompt="Insert a state's name",
    ).lower()

    # None is returned when the input is "Exit".
    if check_user_input(user_input) is None:
        break
    elif check_user_input(user_input):
        guessed_states.append(user_input)
        score += 1
        ROW = STATES_DATAFRAME[STATES_DATAFRAME["state"].str.lower() == user_input]
        x_cor = ROW["x"].values[0]
        y_cor = ROW["y"].values[0]
        draw_state_name(user_input, x_cor, y_cor)

screen.mainloop()
