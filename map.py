from pico2d import *

class Map:
    def __init__(self):
        self.image = load_image('resource/map1.png')
        self.x, self.y = 2300, 0

    def update(self, car_x, car_y):
        self.x = 2300 - car_x + 170 #차량 생성위치 좌표를 더하기
        self.y = 0 - car_y + 240 #위와 동일
        pass

    def draw(self):
        self.image.draw(self.x, self.y)
