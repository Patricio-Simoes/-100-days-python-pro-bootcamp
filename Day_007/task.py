# The task of day 7 was creating a hangman game.
# This script makes use of concepts learned in previous days to achieve that goal.

import random
from words import words
from stages import stages

#* This function draws the console menu.
def menu():
    print(f"Word to guess: {' '.join(output)}")
    guess = input("Guess a letter: ")
    play(guess.lower())
    status()

#* This function checks is the user's input is in the selected word.
#*  - If it is, scores a point.
#*  - If it is not, loses a life.

def play(guess):
    if guess in word:
        score(guess)
    else:
        lose_life(guess)

#* This function scores a point and updates the output.
def score(guess):
    i = 0
    for letter in word:
        if letter == guess:
            output[i] = guess
        i += 1

#* This function loses a life and updates the output.
def lose_life(guess):
    global lifes
    lifes -= 1
    print(f"{guess} is not in the word, you lose a life.")

#* This function prints the status of the player's lifes on screen.
def status():
    print(stages[lifes])
    print(f"***********************{lifes}/6 LIVES LEFT***********************")

#* This function checks if either conditions to end the game have been met and returns either True or False.
def is_game_over():
    if lifes == 0:
        global word
        word = word.upper()
        print(f"***********************IT WAS {word}! YOU LOSE***********************")
        return True
    elif not '_' in output:
        print("***********************YOU WIN!***********************")
        return True
    return False

print("""
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/
""")

#? Keeps track of the player's lifes.
lifes = 6

#? Random number used to pick a word.
index = random.randint(0, len(words) - 1)

#? Selected word.
word = words[index]

#? The output presented on the screen.
#? Starts with all entries as '_'.
output = []

for i in range(len(word)):
    output.append("_")

while not is_game_over():
    menu()