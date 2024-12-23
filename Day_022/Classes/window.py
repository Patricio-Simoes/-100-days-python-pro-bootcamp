from turtle import Screen

BACKGROUND_COLOR = "black"


class Window:
    def __init__(self):
        """
        Initializes the game window with specified dimensions and properties.
        """
        self.screen = Screen()
        self.HEIGHT = 600
        self.WIDTH = 800
        self.create_window()

    def create_window(self):
        """
        Sets up the game screen with dimensions, background color, and title.

        :return: None
        """
        self.screen.setup(self.WIDTH, self.HEIGHT)
        self.screen.bgcolor(BACKGROUND_COLOR)
        self.screen.title("Pong Game")
        self.screen.tracer(0)
