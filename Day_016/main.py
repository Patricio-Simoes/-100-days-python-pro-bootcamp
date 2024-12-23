# The task of day 16 was creating the coffee machine made in day 15, but this time, following the OOP paradigm.

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from ascii_art import logo
import os
import sys
import time


def cls():
    os.system("cls" if os.name == "nt" else "clear")


def start():
    """
    Starts the program and returns the user's order.
    """
    cls()
    value = ""
    print(logo)
    print("Welcome to the OOP coffee machine!")
    print("What would you like?")
    print(menu.get_items())
    return input(": ").lower()


menu = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()

while True:
    order = start()
    # ? Checks if the program should shutdown.
    if order == "off":
        print("Shutting down...")
        break
    # ? Checks if a report was asked.
    if order == "report":
        coffee_machine.report()
        money_machine.report()
    # ? If not, checks if the input is valid.
    else:
        item = menu.find_drink(order)
        while item is None:
            item = menu.find_drink(order)
            time.sleep(1)
            order = start()
        # ? The order is valid. Checks if the order can be made.
        if coffee_machine.is_resource_sufficient(item):
            # ? If the order can me made, payment is asked.
            if money_machine.make_payment(item.cost):
                print(f"One {order} comming up!")
                coffee_machine.make_coffee(item)
    time.sleep(3.5)
