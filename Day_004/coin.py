# This script makes use of the random library to generate numbers that are either zero or one.
# Then, it is going to assign the number to a coin's face:
#   - Heads - 0
#   - Tails - 1

import random as rand

r = rand.randint(0, 1)

if r == 0:
    result = "Heads"
else:
    result = "Tails"

print(f"You've got {result}!")
