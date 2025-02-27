# This script replicates the fizz buzz game login in Python.
#   - Each number from 1 to 100 is printed on the screen.
#   - When the number is divisible by 3 then instead of printing the number it should print "Fizz".
#   - When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
#   - If the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
