# The task of day 9 was creating a script that simulated a silent auction house.
# Thsi script uses a dictionary to allow multiple users to "bid" a certain ammount and the, pass the device to another user to do the same.
# Once there are no more users, the scripts prints who bid the highest and declares the winner.


from ascii_art import logo
import os

bidders = {}
is_exit = False


# * Clears the screen.
def cls():
    os.system("cls" if os.name == "nt" else "clear")


# * Gets a user's name and bid ammount and adds these data to a dictionary.
def get_bid():
    name = input("Insert your name: ")
    while True:
        bid = input("Insert your bid: $")
        try:
            bid= float(bid)
            break
        except ValueError:
            print("Error: The input is invalid!")
    bidders[name] = bid


# * Checks if there are any users left who want to bid.
def keep_bidding():
    x = ""
    while x != "y" and x != "n":
        x = input("Are there any other bidders? [Y/N]: ").lower()
        if x != "y" and x != "n":
            print("Error! Invalid input.")
    if x == "y":
        return True
    elif x == "n":
        return False


# * Main function that keeps being called while keep_biding does not return False.
def menu():
    global is_exit
    while not is_exit:
        cls()
        print(logo)
        get_bid()
        is_exit = not keep_bidding()


# * Determines who bid the highest ammount and prints the user's name alongside the ammount bidded.
def get_winner():
    winner = ""
    ammount = 0
    for name in bidders:
        # ? Declares this user as the new winner.
        if bidders[name] > ammount:
            winner = name
            ammount = bidders[name]
    print(f"The winner is {winner} with a bid of ${ammount}!")


menu()
get_winner()
