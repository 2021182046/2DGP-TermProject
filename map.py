from pico2d import *



class Map:
    def __init__(self):
        self.mid_lines = None
        self.lines = None
        self.roads = None
        self.walls = None
        self.image = load_image('resource/map2_2.png')
        self.x, self.y = 970, 350  #1000, 500

    def set_collision_areas(self, walls, roads, lines, mid_lines):
        self.walls = walls
        self.roads = roads
        self.lines = lines
        self.mid_lines = mid_lines

    def update(self, car_x, car_y, car_speed):
        old_x, old_y = self.x, self.y
        self.x = 1500 - car_x + car_speed #차량 생성위치 좌표를 더하기
        self.y = 750 - car_y + car_speed #위와 동일
        dx, dy = old_x - self.x, old_y - self.y
        for wall in self.walls:
            wall.update(dx, dy)
        for road in self.roads:
            road.update(dx, dy)
        for line in self.lines:
            line.update(dx, dy)
        for mid_line in self.mid_lines:
            mid_line.update(dx, dy)
        pass

    def draw(self):
        self.image.draw(self.x, self.y)

