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
ui_lap_1 = load_image('UI_Lap1.png')
ui_lap_2 = load_image('UI_Lap2.png')

font = load_font('ENCR10B.TTF', 30)
boost_font = load_font('ENCR10B.TTF', 15)
start_time = get_time()

game = True
left, right, front, back, boost = False, False, False, False, False
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

class Collision_wall:
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
        if group == 'car:wall':
            other.speed = -other.speed / 2
            other.move()

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
        self.boost_speed_limit = 10 # 부스터 최고속도
        self.boost_value = 100


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
        boost_font.draw(self.x+10, self.y+10, f'{self.boost_value}')
        #draw_rectangle(*self.collide_box())

    def move_front(self):
        if boost and self.boost_value > 0:
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
        return self.x - 10, self.y - 20, self.x + 10, self.y + 20

    def handle_collision(self, group, other):
        if group == 'car:road':
            self.speed_limit = 7
        else:
            self.speed_limit = 4
        if group == 'car:wall':
            self.speed = -self.speed / 2
            self.move()

    def wall_bounce(self): # 벽에 부딪히면 부딪히기 전 진행속도의 절반속도로 튕겨져나감
        self.speed = -self.speed / 2
        self.move()

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
            if not collided and group ==  'car:road':
                a.speed_limit = 4



def move_event():
    global game, PLAYER_CAR, left, right, front, back, boost, move

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
            elif event.key == SDLK_LSHIFT:
                boost = True

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
            elif event.key == SDLK_LSHIFT:
                boost = False

PLAYER_CAR = Car(7, 1) # 플레이어 생성
MAP = Map()
walls = [Collision_wall(0, 0, 40, 600),
         Collision_wall(40, 350, 60, 600),
         Collision_wall(60, 600, 70, 700),
         Collision_wall(70, 700, 80, 800),
         Collision_wall(80, 800, 90, 900),
         Collision_wall(90, 900, 100, 930),
         Collision_wall(100, 930, 110, 950),
         Collision_wall(110, 950, 120, 970),
         Collision_wall(120, 960, 150, 980),
         Collision_wall(150, 980, 180, 1000),
         Collision_wall(180, 1000, 220, 1020),
         Collision_wall(220, 1010, 350, 1030),
         Collision_wall(350, 1020, 450, 1040),
         Collision_wall(450, 1010, 600, 1030),
         Collision_wall(600, 1000, 720, 1020),
         Collision_wall(720, 1010, 800, 1030),
         Collision_wall(800, 1020, 880, 1040),
         Collision_wall(880, 1030, 960, 1050),
         Collision_wall(960, 1040, 1100, 1060),
         Collision_wall(1100, 1050, 1200, 1070),
         Collision_wall(1200, 1060, 1280, 1070),
         Collision_wall(1280, 1065, 1360, 1080),
         Collision_wall(1360, 1080, 1440, 1100),

         Collision_wall(210, 0, 250, 200),
         Collision_wall(220, 200, 260, 400),
         Collision_wall(230, 400, 270, 500),
         Collision_wall(250, 500, 270, 550),
         Collision_wall(260, 550, 270, 600),

         Collision_wall(340, 500, 350, 550),
         Collision_wall(340, 550, 350, 600),
         Collision_wall(350, 600, 370, 630),
         Collision_wall(370, 630, 390, 660),
         Collision_wall(390, 650, 420, 680),
         Collision_wall(420, 670, 450, 690),
         Collision_wall(450, 690, 480, 710),
         Collision_wall(480, 700, 510, 720),
         Collision_wall(510, 720, 650, 750),
         Collision_wall(620, 750, 800, 780),
         Collision_wall(750, 780, 1000, 800),
         Collision_wall(900, 800, 1200, 820),
         Collision_wall(1100, 820, 1400, 840),
         Collision_wall(1300, 840, 1600, 860),
         Collision_wall(1500, 860, 1700, 880),
         Collision_wall(1570, 450, 1590, 700),
         Collision_wall(1590, 700, 1610, 750),
         Collision_wall(1610, 750, 1630, 800),
         Collision_wall(1630, 770, 1650, 850),
         Collision_wall(1590, 400, 1610, 450),
         Collision_wall(1610, 350, 1630, 400),
         Collision_wall(1630, 300, 1650, 350),
         Collision_wall(1650, 270, 1670, 320),
         Collision_wall(1670, 250, 1700, 270),
         Collision_wall(1700, 230, 1730, 250),
         Collision_wall(1730, 200, 1760, 230),
         Collision_wall(1760, 170, 1790, 200),
         Collision_wall(1790, 140, 1820, 170),
         Collision_wall(1820, 110, 1850, 140),
         Collision_wall(1850, 80, 1880, 110),

         ]
for wall in walls:
    add_collision_pair('car:wall', PLAYER_CAR, wall)


roads = [Collision_road(110, 50, 190, 500),
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
         Collision_road(1850, 300, 1890, 410)
         ]
for road in roads:
    add_collision_pair('car:road', PLAYER_CAR, road)



while(game):
    clear_canvas()
    MAP.draw()
    PLAYER_CAR.draw()
    ui_main.draw(WIDTH // 2, HEIGHT // 2)
    ui_1st.draw(80, HEIGHT - 50)
    ui_lap.draw(250, HEIGHT - 50)
    ui_lap_1.draw(360, HEIGHT - 50)

    current_time = get_time()
    elapsed_time = current_time - start_time
    minutes = int(elapsed_time/60)
    second = elapsed_time % 60
    font.draw(500, HEIGHT - 65, 'Lap Time : %d:%.3f' %(minutes, second), (255,255,255))

    PLAYER_CAR.update()
    move_event()
    #for road in roads: # 도로 충돌박스 그리기
        #road.draw()

    #for wall in walls:  # 도로 충돌박스 그리기
        #wall.draw()

    handle_collisions()

    update_canvas()
    delay(0.01)