from pico2d import *



class Map:
    def __init__(self):
        self.roads = None
        self.walls = None
        self.image = load_image('resource/map1.png')
        self.x, self.y = 2300, 0

    def set_collision_areas(self, walls, roads):
        self.walls = walls
        self.roads = roads

    def update(self, car_x, car_y):
        old_x, old_y = self.x, self.y
        self.x = 2300 - car_x + 170 #차량 생성위치 좌표를 더하기
        self.y = 0 - car_y + 240 #위와 동일
        dx, dy = old_x - self.x, old_y - self.y
        for wall in self.walls:
            wall.update(dx, dy)
        for road in self.roads:
            road.update(dx, dy)
        pass

    def draw(self):
        self.image.draw(self.x, self.y)
