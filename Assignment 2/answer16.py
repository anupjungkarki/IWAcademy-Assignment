# Imagine you are creating a Super Mario game. You need to define a class to represent Mario. What would it look like?
# If you aren't familiar with SuperMario, use your own favorite video or board game to model a player.
class Mario:
    def __init__(self):
        self._lives = 3
        self._speed = 10
        self._jumpHeight = 5
        self._width = 32
        self._height = 64
        self._sprite = "/path/for Image"

    def draw(self, screen):
        # To draw Sprite to the screen
        return

    def update(self, delta_time):
        # To use jump method if jump button is pressed
        # To run if left or right is pressed
        return

    def move(self, direction):
        # To use for speed and move in the specified direction
        return

    def jump(self):
        # To determine the jump height
        return

    def collides(self):
        # To determine the width and height if mario collide with object
        return
