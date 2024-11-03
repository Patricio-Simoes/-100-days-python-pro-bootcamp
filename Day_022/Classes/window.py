from turtle import Screen

BACKGROUND_COLOR = "black"

class Window:
    def __init__(self):
        self.screen = Screen()
        self.HEIGHT = 600
        self.WIDTH = 800
        self.create_window()
        
    def create_window(self):
        """Creates the game screen.
        """
        self.screen.setup(self.WIDTH, self.HEIGHT)
        self.screen.bgcolor(BACKGROUND_COLOR)
        self.screen.title("Pong Game")
        self.screen.tracer(0)
