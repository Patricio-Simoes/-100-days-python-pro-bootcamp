from data import data
from ascii_art import logo, vs
import random
import os
import sys

game = True


def cls():
    os.system("cls" if os.name == "nt" else "clear")


def pick(x=-1):
    """
    Picks someone from the data list.
    If a parameter is passed, it will not pick that index.
    """
    length = len(data) - 1
    if x == -1:
        return random.randint(1, length)
    else:
        out = random.randint(1, length)
        while out == x:
            out = random.randint(1, length)
        return out


def compare(a, b):
    """
    Prints the elements that have the index that are passed as parameters and asks the user to compare them.
    Returns the user's input.
    """
    print(
        f"Compare A: {data[a]['name']}, a {data[a]['description']} from {data[a]['country']}"
    )
    print(vs)
    print(
        f"Against B: {data[b]['name']}, a {data[b]['description']} from {data[b]['country']}"
    )
    output = ""
    while output != "a" and output != "b":
        output = input("Who has more followers? [A/B]: ").lower()
        if output != "a" and output != "b":
            print("Error! Invalid input.")
    return output


def play(a, b, guess):
    """
    Checks if the user's guess was correct and returns 1 if it is, 0 otherwise.
    """
    print(data[a]["follower_count"])
    print(data[b]["follower_count"])
    if data[a]["follower_count"] >= data[b]["follower_count"] and guess == "a":
        return 1
    elif data[a]["follower_count"] <= data[b]["follower_count"] and guess == "b":
        return 1
    else:
        return 0


game = True

print(logo)

# ? Represents the total number of corrected guesses.
score = 0

while game:
    # ? Picks two random elements from data.
    a = pick()
    b = pick(a)
    guess = compare(a, b)
    cls()
    print(play(a, b, guess))
    if play(a, b, guess) == 1:
        print(logo)
        score += 1
        print(f"That's right! Current score: {score}")
    else:
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        game = False

# ? Asks the user if a new game is to be started.
aux = ""
while aux != "y" and aux != "n":
    aux = input("Would you like to play again? [Y/N]:").lower()
    if aux != "y" and aux != "n":
        print("Error! Invalid input.")
if aux == "y":
    is_game_over = False
    cls()
else:
    print("Goodbye...")
    sys.exit()
