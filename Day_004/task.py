# The final task of day 4 was to build a rock, papper scissors game.
# This script receives an input from the user, which is then matched to a list of choices.
# The logic is done using if/else statements to determine the winner.

import random as rand
import sys

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

choices = [rock, paper, scissors]

computer = rand.randint(0,2)

choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")

if choice.isdigit():
    choice = int(choice)
else:
    print("Sorry, this is not a valid choice...")
    sys.exit()

if choice == 0:
    if computer == 0:
        result = "It's a draw!"
    if computer == 1:
        result = "The computer won!"
    if computer == 2:
        result = "Congratulations, you won!"
elif choice == 1:
    if computer == 0:
        result = "Congratulations, you won!"
    if computer == 1:
        result = "It's a draw!"
    if computer == 2:
        result = "The computer won!"
elif choice == 2:
    if computer == 0:
        result = "The computer won!"
    if computer == 1:
        result = "Congratulations, you won!"
    if computer == 2:
        result = "It's a draw!"
else:
    print("Sorry, this is not a valid choice...")
    sys.exit()

print("You played:")
print(choices[choice])
print("The computer played:")
print(choices[computer])
print(result)
