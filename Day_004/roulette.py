# This script generates a random integer between 0 and 4 and matches the number with the index of a list.
# The list represents a group of friends and the one that gets selected has to pay the restaurant bill.

import random as rand

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

num = rand.randint(0,4)

print(f"{friends[num]} is paying the bill!")
