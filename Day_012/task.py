# The task of day 12 was creating a simple number guessing game.
# A random number is generated between 1 and 100.
# The easy difficulty gives the user 10 attempts at guessing the game while the hard gives only 5.
# With each attempt, the scripts outputs if the guess was too low or too high.

from ascii_art import logo
import random
import os
import sys


# * Clears the screen.
def cls():
    os.system("cls" if os.name == "nt" else "clear")


def start_game():
    """
    Starts the game and returns a random number between 1 and 100 aswell as the difficulty that the player selected.
    """
    diff = ""
    num = random.randint(1, 101)
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    while diff != "h" and diff != "e":
        diff = input("Choose a difficulty.\n[E]asy\n[H]ard\n: ").lower()
        if diff != "h" and diff != "e":
            print("Error! Invalid input.")
    return num, diff


def set_attempts(diff):
    """
    Returns 10 if difficulty was set to easy, 5 if set to hard.
    """
    if diff == "e":
        return 10
    else:
        return 5


def play(num, x):
    """
    Verifies the user's guess and outputs if the generated number was bellow or above the user's guess.
    Returns -1 if the guess was wrong, or, 0 if right.
    """
    if x > num:
        print("Too high.")
        return -1
    elif x < num:
        print("Too low.")
        return -1
    elif x == num:
        print("Nailed it!")
        return 0


is_play_again = True
is_game_over = False


while is_play_again:
    number, difficulty = start_game()
    attempts = set_attempts(difficulty)

    while not is_game_over:
        x = input("Make a guess: ")
        if play(int(number), int(x)) == -1:
            attempts -= 1
            print(f"You have {attempts} attempts remaining to guess the right number.")
        else:
            is_game_over = True
    aux = ""
    while aux != "y" and aux != "n":
        aux = input("Would you like to play again? [Y/N]:").lower()
        if aux != "y" and aux != "n":
            print("Error! Invalid input.")
    if aux == "y":
        is_game_over = False
        is_play_again = True
        cls()
    else:
        print("Goodbye...")
        sys.exit()
