from turtle import Screen

BACKGROUND_COLOR = "black"
HEIGHT = 600
WIDTH = 600


class Window:
    """Represents the game window for the snake game."""

    def __init__(self):
        """
        Initializes a new Window object and creates the game window.

        Calls the create_window method to set up the screen properties, including
        size, background color, title, and update settings.
        """
        self.screen = Screen()
        self.create_window()

    def create_window(self):
        """
        Configures the game window's properties.

        Sets the window size, background color, title, and disables automatic screen updates
        to allow for manual control of screen refreshes.
        
        :return: None
        """
        self.screen.setup(width=WIDTH, height=HEIGHT)
        self.screen.bgcolor(BACKGROUND_COLOR)
        self.screen.title("Snake Game")
        self.screen.tracer(0)
