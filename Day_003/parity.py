# This script evaluates if a given number is odd or even.
# To achieve this, the modulo operator is used to check if the remainder is equal to zero.
# If it is, the number is even, if not, it is odd.

print("Let's verify if a number is even or odd!")
num = int(input("Please insert an integer number: "))

if num % 2 == 0:
    print("The number is even!")
else:
    print("The number is odd!")
