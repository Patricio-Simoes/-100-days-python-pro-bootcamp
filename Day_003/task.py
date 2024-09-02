# The final task of day 3 was to build a little "crossroads" game using if/else statements where,
# the final goal was to select the correct options in order to find the treasure and reach the end of the game.

import sys

ascii_art = """
  ____________________________________________________________________
 / \-----     ---------  -----------     -------------- ------    ----\\
 \_/__________________________________________________________________/
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~\    \\"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____~____~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  -------\\
 \_/__________________________________________________________________/
"""

print(ascii_art)

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a crossroad, where would you like to go?")
crossroads = input("Type 'left' or 'right': ").lower()

if crossroads == "right":
    print("You've fell into a hole. Game Over.")
elif crossroads == "left":
    lake = input("You've come into a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat, or 'swim' to swim across: ").lower()
    if lake == "swim":
        print("You've got attacked by an angry trout. Game Over.")
    elif lake == "wait":
        door = input("You've arrived at the island unharmed, there is a house with 3 doors."
              "One red, one yellow and one blue. Which one do you choose? ").lower()
        if door == "red":
            print("It's a room full of fire. Game Over!")
        elif door == "blue":
            print("You've found the treasure. Congratulations!")
        elif door == "yellow":
            print("You've entered in a room full of beasts. Game Over.")
        else:
            print("Sorry, you've typed the wrong inputs...")
            sys.exit()
    else:
        print("Sorry, you've typed the wrong inputs...")
        sys.exit()
else:
    print("Sorry, you've typed the wrong inputs...")
    sys.exit()
