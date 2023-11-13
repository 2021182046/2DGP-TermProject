from pico2d import *
import math
import sdl2

WIDTH, HEIGHT = 1920, 1080
open_canvas(WIDTH, HEIGHT)

ui_main = load_image('UI_black(1920x1080).png')
ui_1st = load_image('UI_1st.png')
ui_2nd = load_image('UI_2nd.png')
ui_3rd = load_image('UI_3rd.png')
ui_4th = load_image('UI_4th.png')
ui_lap = load_image('UI_Lap.png')
ui_lap_0 = load_image('UI_Lap0.png')
ui_lap_1 = load_image('UI_Lap1.png')
ui_lap_2 = load_image('UI_Lap2.png')

font = load_font('ENCR10B.TTF', 30)
start_time = get_time()

game = True
left, right, front, back = False, False, False, False
move = False

class Map:
    def __init__(self):
        self.image = load_image('map1.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(2300, 0)


class Collision_road:
    def __init__(self, left_b, bottom_b, right_b, top_b):
        self.left_b = left_b
        self.bottom_b = bottom_b
        self.right_b = right_b
        self.top_b = top_b

    def draw(self):
        draw_rectangle(*self.collide_box())

    def collide_box(self):
        return self.left_b, self.bottom_b, self.right_b, self.top_b

    def handle_collision(self, group, other):
        if group == 'car:road':
            other.speed_limit = 7

        else:
            other.speed_limit = 4

class Car:
    def __init__(self, speed_limit, rotation): #속도, 각도
        self.image = load_image('player_car.png')

        self.rotation_center_x, self.rotation_center_y = 640, 400
        self.speed = 0
        self.speed_limit = speed_limit
        self.image_rotation_angle = math.radians(-90)
        self.rotation_angle = math.radians(-90)
        self.rotation = rotation
        self.x, self.y = 170, 240
        self.accel = 0.1


    def rotate(self):
        if self.speed != 0:
            if left:
                self.rotation_angle += self.rotation
                self.image_rotation_angle += self.rotation * 0.0175  # 자연스러운 각도 연동값
            elif right:
                self.rotation_angle -= self.rotation
                self.image_rotation_angle -= self.rotation * 0.0175 # 자연스러운 각도 연동값

    def draw(self):
        self.image.clip_composite_draw(0, 0, 1280, 800, self.image_rotation_angle, '',
                                       self.x, self.y, 70, 50)
        draw_rectangle(*self.collide_box())

    def move_front(self):
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

    def move_slowdown(self):
        self.speed = max(self.speed - self.accel / 2, 0)
        self.move()

    def update(self):
        self.rotate()
        if front:
            self.move_front()
        elif back:
            self.move_back()
        if not move:
            PLAYER_CAR.move_slowdown()

    def collide_box(self):
        return self.x - 20, self.y - 30, self.x + 20, self.y + 30

    def handle_collision(self, group, other):
        if group == 'car:road':
            self.speed_limit = 7

        else:
            self.speed_limit = 4


def collide(a, b): # 충돌 검사
    left_a, bottom_a, right_a, top_a = a.collide_box()
    left_b, bottom_b, right_b, top_b = b.collide_box()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True


collision_pairs = {}
def add_collision_pair(group, a, b): # 충돌 그룹 등록
    if group not in collision_pairs:
        print(f'Added new group {group}')
        collision_pairs[group] = [ [],[] ]
    if a:
        collision_pairs[group][0].append(a)
    if b:
        collision_pairs[group][1].append(b)

def handle_collisions(): # 충돌 그룹의 충돌 후 동작
    for group, pairs in collision_pairs.items():
        for a in pairs[0]:
            collided = False
            for b in pairs[1]:
                if collide(a, b):
                    a.handle_collision(group, b)
                    b.handle_collision(group, a)
                    collided = True
            if not collided:
                a.speed_limit = 4


def move_event():
    global game, PLAYER_CAR, left, right, front, back, move

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_a:
                left = True
                right = False
            elif event.key == SDLK_d:
                left = False
                right = True
            elif event.key == SDLK_w:
                front = True
                move = True
            elif event.key == SDLK_s:
                back = True
                move = True

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_a:
                left = False
            elif event.key == SDLK_d:
                right = False
            elif event.key == SDLK_w:
                front = False
                move = False
            elif event.key == SDLK_s:
                back = False
                move = False

PLAYER_CAR = Car(3, 1) # 플레이어 생성
MAP = Map()

roads = [Collision_road(100, 50, 200, 500),
         Collision_road(130, 500, 220, 700),
         Collision_road(160, 720, 400, 780),
         Collision_road(400, 750, 450, 800),
         Collision_road(250, 800, 600, 850),
         Collision_road(450, 860, 870, 890),
         Collision_road(670, 900, 1350, 940),
         Collision_road(1150, 950, 1800, 980),
         Collision_road(1600, 1000, 1800, 1020),
         Collision_road(1800, 800, 1900, 950),
         Collision_road(1770, 700, 1830, 800),
         Collision_road(1830, 750, 1860, 800),
         Collision_road(1700, 550, 1770, 700),
         Collision_road(1730, 700, 1770, 750),
         Collision_road(1730, 450, 1770, 550),
         Collision_road(1770, 410, 1810, 510),
         Collision_road(1810, 350, 1850, 450),
         Collision_road(1850, 300, 1890, 410)]
for road in roads:
    add_collision_pair('car:road', PLAYER_CAR, road)


while(game):
    clear_canvas()
    MAP.draw()
    PLAYER_CAR.draw()
    ui_main.draw_now(WIDTH // 2, HEIGHT // 2)
    ui_1st.draw_now(80, HEIGHT - 50)
    ui_lap.draw_now(250, HEIGHT - 50)
    ui_lap_0.draw_now(360, HEIGHT - 50)

    current_time = get_time()
    elapsed_time = current_time - start_time
    font.draw(500, HEIGHT - 65, 'Lap Time : %.3f' % elapsed_time, (255,255,255))

    PLAYER_CAR.update()
    move_event()
    for road in roads: # 도로 충돌박스 그리기
        road.draw()

    handle_collisions()

    update_canvas()
    delay(0.01)