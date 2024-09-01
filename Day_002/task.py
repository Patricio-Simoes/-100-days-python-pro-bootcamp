# The final task of day 2 was to build a script that would receive the following:
#   - Total bill.
#   - A percentage symbolizing the ammount of tip to give, based on the total bill.
#   - The number of people to split the bill with.
# It should then take thee inputs and display the total ammount each people should pay in order to get the ammount of the bill plus the tip.

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

# The result is calculated based of the formula: bill * percentage.

# Adding +1 here in order to be able to multiply directy bellow, (ex. 100 * 1.12 = 112).
percentage = tip / 100 + 1
# This is the combined value.
total = bill * percentage
# This is the value each person should pay, rounded to 2 decimals.
result = round(total / people, 2)

print(f"Each person should pay: ${result}")
