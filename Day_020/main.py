# The task for day 20 was creating a snake game using the turtle module.
# This project was completed on day 21.

from Classes.snake import Snake
from Classes.window import Window

import time

window = Window()

snake = Snake()

window.screen.listen()
window.screen.onkey(snake.up, "Up")
window.screen.onkey(snake.down, "Down")
window.screen.onkey(snake.left, "Left")
window.screen.onkey(snake.right, "Right")

is_game_on = True

while is_game_on:
    window.screen.update()
    time.sleep(0.05)
    snake.move()

screen.exitonclick()
