from pico2d import *

class Map:
    def __init__(self):
        self.image = load_image('resource/map1.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(2300, 0)
