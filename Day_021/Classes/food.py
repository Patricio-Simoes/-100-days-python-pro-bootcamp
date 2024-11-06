from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.generate()
        self.refresh()

    def generate(self):
        self.shape("circle")
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.shapesize(0.5, 0.5)

    def refresh(self):
        random_x = random.randint(-230, 230)
        random_y = random.randint(-230, 200)
        self.goto(random_x, random_y)
