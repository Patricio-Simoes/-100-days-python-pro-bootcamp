# This script calculates the ammount of dollars that a customer that orders pizza has to pay based on the following:
#   - The pizza size.
#   - If pepperoni is to be added.
#   - If extra cheese is to be added.

import sys

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ").lower()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").lower()
extra_cheese = input("Do you want extra cheese? Y or N: ").lower()

total = 0

# This section calculates the ammount to pay based on the pizza size.
#   - Small : 15$
#   - Medium : 20$
#   - Large : 25$

if size == "s":
    total += 15
elif size == "m":
    total += 20
elif size == "l":
    total += 25
else:
    print("Sorry, you've typed the wrong inputs...")
    sys.exit()

# This section adds 2$ for small pizzas and 3$ for medium and large pizzas, if pepperoni is to be added.

if pepperoni == "y":
    if size == "s":
        total += 2
    else:
        total += 3

# This section adds 1$ if extra cheese is to be added.

if extra_cheese == "y":
    total += 1

print(f"Your final bill is: ${total}.")
