# The final task of day 1 was to build a script that would receive the following:
#   - The name of the city you grew up in.
#   - The name of your pet.
# Once these are gathered, a band name would be generated as following:
#   Name: city + pet

print("Welcome to the band name generator!")
city = input("What's the name of the city you grew up in?\n")
pet = input("What's your pet's name?\n")
print("Your band name could be " + city + " " + pet)