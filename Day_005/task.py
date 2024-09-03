# The final task of day 5 was a password generator.
# I've taken the liberty to modify the request a bit.
# This script receive the password length from the user and then proceeds to generate a random password made of letters, digits and symbols.
# The original request asked for the number of letters, digits and symbols aswell. I have made is so that, these variables are randomly generated.

import string
import time
import random as rand
import sys

letters = list(string.ascii_letters)
numbers = list(string.digits)
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]
password = []

print("Welcome to the password generator!")
length = input("How many characters should your password have? ")

# Checks if the user's input is valid.
if not length.isdigit():
    print("Sorry, that is not a valid number...")
    sys.exit()
length = int(length)

print(f"Generating a password of legth {length}...")
time.sleep(1.5)

# Defines how many numbers, characters and symbols the password should be composed of.
available_numbers = rand.randint(1, length - 2)
available_letters = rand.randint(1, length - available_numbers - 1)
available_symbols = length - available_numbers - available_letters

# Generates the password itself in sequential order.
for i in range(available_numbers):
    password.append(rand.choice(numbers))

for i in range(available_letters):
    password.append(rand.choice(letters))

for i in range(available_symbols):
    password.append(rand.choice(symbols))

# Shuffles the password in order to randomize the order of the characters
rand.shuffle(password)

final_password = ''.join(password)
print(f"Your password is: {final_password}")
