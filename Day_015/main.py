# The task of day 15 was creating a coffee machine.
# This coffee machine processes user's requests and receives payments, retunring the corresponding changes and requested items.
# Available options are:
#  - 1. Cappuccino
#  - 2. Latte
#  - 3. Expresso
#  - report
#  - refill
#  - off


from ascii_art import logo
from data import MENU, resources, input_options
import os
import sys
import time

def cls():
    os.system("cls" if os.name == "nt" else "clear")


def start():
    """
    Starts the coffee machine and retrieves the user's input.
    """
    cls()
    value = ""
    print(logo)
    print("Welcome to the coffee machine!")
    print("What would you like?")
    print("1. Cappuccino (1.5$)\n2. Latte (2.5$)\n3. Expresso (3.0$)")
    while value not in input_options:
        value = input(": ").lower()
    return value


def report():
    global money
    print("The coffee machine currently has:")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Milk: {resources['milk']}ml")
    print(f"Water: {resources['water']}ml")
    print(f"Money: {money}$")


def collect_payment():
    """
    Collects coins from the user and returns the summed value.
    """
    quarters = ""
    dimes = ""
    nickels = ""
    pennies = ""
    print("Please insert your coins.")
    while not quarters.isdigit():
        quarters = input("Number of quarters (0.25$): ")
        if not quarters.isdigit():
            print("Error! That is not a valid number of coins!")
    while not dimes.isdigit():
        dimes = input("Number of dimes (0.10$): ")
        if not quarters.isdigit():
            print("Error! That is not a valid number of coins!")
    while not nickels.isdigit():
        nickels = input("Number of dimes (0.05$): ")
        if not nickels.isdigit():
            print("Error! That is not a valid number of coins!")
    while not pennies.isdigit():
        pennies = input("Number of pennies (0.01$): ")
        if not pennies.isdigit():
            print("Error! That is not a valid number of coins!")
    total = round(
        float(quarters) * 0.25
        + float(dimes) * 0.10
        + float(nickels) * 0.05
        + float(pennies) * 0.01,
        2,
    )
    return total


def check_ingredients(item):
    """
    Checks if the machine has enough resources to make the desired coffee.
    If it has, returns 1. Returns 0 otherwise.
    """
    if resources["water"] >= MENU[item]["ingredients"]["water"]:
        if resources["coffee"] >= MENU[item]["ingredients"]["coffee"]:
            if item != "cappuccino":
                if resources["milk"] >= MENU[item]["ingredients"]["milk"]:
                    return 1
                else:
                    print("Error! The machine has run out of milk!")
            return 1
        else:
            print("Error! The machine has run out of coffee!")
    else:
        print("Error! The machine has run out of water!")
    return 0

def update_ingredients(item):
    """
    Updates the machine's ingredients after serving a coffee.
    """
    resources["coffee"] -= MENU[item]["ingredients"]["coffee"]
    resources["water"] -= MENU[item]["ingredients"]["water"]
    if item != "cappuccino":
        resources["milk"] -= MENU[item]["ingredients"]["milk"]

def refill():
    """
    Refills the machine with 300ml of water, 200 ml of milk and 100g of coffee.
    """
    resources["coffee"] += 100
    resources["milk"] += 200
    resources["water"] += 300
    print("The machine has been refilled!")

#? To make things easier, the program starts the machine with 100$.
money = 100

while True:
    choice = start()
    # ? Error handling is done on the start() function.
    if choice == "off":
        print("Shutting down...")
        break
    elif choice == "refill":
        refill()
    elif choice == "report":
        report()
    else:
        match choice:
            case "1":
                item = "cappuccino"
            case "2":
                item = "latte"
            case "3":
                item = "expresso"
        payment = collect_payment()
        if payment >= MENU[item]["cost"]:
            if check_ingredients(item) == 1:
                #? Checks if a change is due and updates the machine's money value.
                change = 0
                if payment > MENU[item]["cost"]:
                    change = round(payment - MENU[item]["cost"], 2)
                    print(f"Here is your {item} and your change of {change}$ enjoy!")
                else:
                    print(f"Here is your {item}, enjoy!")
                money = money - change + payment
                #? Updates the machine's ingredients.
                update_ingredients(item)
            else:
                pass
        else:
            print("Error! Not enought money. A refund has been issued.")
            print(f"Your item costs {MENU[item]['cost']}$ and you have entered only {payment}$.")
    time.sleep(3.5)