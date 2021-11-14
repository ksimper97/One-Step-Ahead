import arcade

from constants import CHARACTER_SCALING

class Obstacle(arcade.Sprite):

    def __init__(self):
        super().__init__()

        self.scale = CHARACTER_SCALING

class Fire(Obstacle):

    def __init__(self):
        super().__init__()