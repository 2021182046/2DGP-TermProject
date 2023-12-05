import math
import global_values
from pico2d import *


class Car:
    def __init__(self, speed_limit, rotation, x, y): #속도, 각도
        self.image = load_image('resource/player_car.png')

        self.rotation_center_x, self.rotation_center_y = 640, 400
        self.speed = 0
        self.speed_limit = speed_limit
        self.image_rotation_angle = math.radians(-90)
        self.rotation_angle = math.radians(-90)
        self.rotation = rotation
        #self.x, self.y = 170, 240
        self.x, self.y = x, y
        self.accel = 0.1
        self.boost_speed_limit = 5 # 부스터 최고속도
        self.boost_value = 100
        self.hp = 100
        self.hp_wait_time = 0
        self.lab_count = 0
        self.lab_middle_count = 0


    def rotate(self):
        if self.speed != 0:
            if global_values.left:
                self.rotation_angle += self.rotation
                self.image_rotation_angle += self.rotation * 0.0175  # 자연스러운 각도 연동값
            elif global_values.right:
                self.rotation_angle -= self.rotation
                self.image_rotation_angle -= self.rotation * 0.0175 # 자연스러운 각도 연동값

    def draw(self):
        boost_font = load_font('resource/ENCR10B.TTF', 15)
        hp_font = load_font('resource/ENCR10B.TTF', 12)
        self.image.clip_composite_draw(0, 0, 1280, 800, self.image_rotation_angle, '',
                                       self.x, self.y, 70, 50)
        boost_font.draw(self.x+10, self.y+10, f'{self.boost_value}')
        hp_font.draw(self.x-20, self.y-40, f'HP:{self.hp}')
        #draw_rectangle(*self.collide_box()) # 차 충돌박스 그리기

    def move_front(self):
        if global_values.boost and self.boost_value > 0:
            self.speed = min(self.speed + self.accel*2, self.boost_speed_limit)
            self.boost_value -= 1
        else:
            self.speed = min(self.speed + self.accel, self.speed_limit)
        self.move()

    def move_back(self):
        self.speed = max(self.speed - self.accel, -self.speed_limit / 5)
        self.move()

    def move(self):  # 현재 속도/회전 각도에 따른 수직 수평거리 계산, 위치 갱신
        radians = math.radians(self.rotation_angle)

        horizontal = math.sin(radians) * self.speed
        vertical = math.cos(radians) * self.speed

        self.x -= horizontal
        self.y += vertical

        # self.x = clamp(0, self.x, 4900 - 1920)
        # self.y = clamp(0, self.y, 2400 - 1080)

    def move_slowdown(self):
        self.speed = max(self.speed - self.accel / 2, 0)
        self.move()

    def update(self):
        self.rotate()
        if global_values.front:
            self.move_front()
        elif global_values.back:
            self.move_back()
        if not global_values.move:
            self.move_slowdown()
        print(self.lab_middle_count)  # 랩 중간체크 테스트

    def collide_box(self):
        return self.x - 10, self.y - 20, self.x + 10, self.y + 20

    def handle_collision(self, group, other):
        if group == 'car:road':
            self.speed_limit = 3
        else:
            self.speed_limit = 2
        if group == 'car:wall':
            self.speed = -self.speed / 2
            if get_time() > self.hp_wait_time:
                self.hp -= 10
                self.hp_wait_time = get_time() + 3 #3초 무적시간
            self.move()
        if group == 'car:line':
            if self.lab_middle_count == 1:
                self.lab_middle_count = 0
                self.lab_count += 1
        if group == 'car:mid_line':
            if self.lab_middle_count == 0:
                self.lab_middle_count = 1

    def wall_bounce(self): # 벽에 부딪히면 부딪히기 전 진행속도의 절반속도로 튕겨져나감
        self.speed = -self.speed / 2
        self.move()