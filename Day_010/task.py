# The task of day 10 was creating a console calculator.
# This script uses a functions and if/else/switch statements to achieve this goal.
# In addition, the user can choose to keep performing operations over the previous one or start a new one.

from ascii_art import logo
import sys

def get_input(previous = ""):
    """
    Asks the user for 2 numbers and an operation.
    Returns these values under a dictionary.
    """
    global valid_operators
    x = ""
    y = ""
    o = ""
    #? Executes if this is not a blank operation, with a previous result to take into consideration.
    try:
        x = float(previous)
        while True:
            y = input("Insert the next number: ")
            try:
                y = float(y)
                break
            except ValueError:
                print("Error: The input is invalid!")
        while o not in valid_operators:
            o = input(
                "Pick one of the following:\n(+)Addition\n(-)Subtraction\n(*)Multiplication\n(/)Division\n: "
            )
            if o not in valid_operators:
                print("Error: The operator is not valid! Try again.")
        else:
            return {"x": x, "y": y, "o": o}
    #? Executes if this is a blank operation, with no previous result.
    except ValueError:
        while True:
            x = input("Insert the first number: ")
            try:
                x = float(x)
                break
            except ValueError:
                print("Error: The input is invalid!")
        while True:
            y = input("Insert the second number: ")
            try:
                y = float(y)
                break
            except ValueError:
                print("Error: The input is invalid!")
        while o not in valid_operators:
            o = input(
                "Pick one of the following:\n(+)Addition\n(-)Subtraction\n(*)Multiplication\n(/)Division\n: "
            )
            if o not in valid_operators:
                print("Error: The operator is not valid! Try again.")
        else:
            return {"x": x, "y": y, "o": o}


def add(x, y):
    """
    Adds 2 numbers and returns the value.
    """
    return x + y


def sub(x, y):
    """
    Subtracts 2 numbers and returns the value.
    """
    return x - y


def mult(x, y):
    """
    Multiplies 2 numbers and returns the value.
    """
    return x * y


def div(x, y):
    """
    Divides 2 numbers and returns the value.
    """
    if y != 0:
        return x / y
    else:
        return "Error: Cannot divide by 0!"


def calculate(x, y, o, previous = ""):
    """
    Displays and returns the value of the operation the user defined.
    """

    if previous != "":
        x = previous

    match o:
        case "+":
            r = add(x, y)
        case "-":
            r = sub(x, y)
        case "*":
            r = mult(x, y)
        case "/":
            r = div(x, y)
    print(f"{x} {o} {y} = {r}")
    return r


valid_operators = ["+", "-", "*", "/"]

is_continue = True

previous = ""

print(logo)

while is_continue:

    if previous == "":
        data = get_input()
    else:
        data = get_input(previous)

    result = calculate(data["x"], data["y"], data["o"])

    is_new = ""
    
    while not is_new in ["c", "s", "e"]:
        is_new = input("Continue, [C]\nStart a new operation, [S]\nExit, [E]\n: ").lower()
    match is_new:
        case "c":
            is_continue = True
            previous = result
        case "s":
            is_continue = True
            previous = ""
        case "e":
            is_continue = False

sys.exit()
