# This code is meant to be run on Reeborg's world: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
# The link leads to a maze problem, where the robot, "Reboorg", makes use of the following Python code to get out of it.

def turn_right():
    for i in range(3):
        turn_left()

while front_is_clear():
    move()
        
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
