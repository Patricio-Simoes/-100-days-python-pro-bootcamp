from turtle import Screen

BACKGROUND_COLOR = "black"
HEIGHT = 500
WIDTH = 500


class Window:

    def __init__(self):
        self.screen = Screen()
        self.create_window()

    def create_window(self):
        self.screen.setup(width=WIDTH, height=HEIGHT)
        self.screen.bgcolor(BACKGROUND_COLOR)
        self.screen.title("Snake Game")
        self.screen.tracer(0)
