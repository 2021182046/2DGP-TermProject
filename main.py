from pico2d import *
import math
import sdl2

WIDTH, HEIGHT = 1280, 720
open_canvas(WIDTH, HEIGHT)

map = load_image('map0.png')
player = load_image('player_car.png')

ui_main = load_image('UI_black(1280x720).png')
ui_1st = load_image('UI_1st.png')
ui_2nd = load_image('UI_2nd.png')
ui_3rd = load_image('UI_3rd.png')
ui_4th = load_image('UI_4th.png')
ui_lap = load_image('UI_Lap.png')
ui_lap_0 = load_image('UI_Lap0.png')
ui_lap_1 = load_image('UI_Lap1.png')
ui_lap_2 = load_image('UI_Lap2.png')

idle, accel_push, accel_idle = True, False, True
left, right = False, False
dir, dir_y = 0,0
player_x, player_y = WIDTH//2, HEIGHT//2

class Car:
    Image_player = player

    def __init__(self, speed_limit, rotation): #속도, 각도
        self.image = self.Image_player
        self.speed = 0
        self.speed_limit = speed_limit
        self.rotation_angle = math.radians(-90)
        self.rotation = math.radians(rotation)
        self.break_push = False
        self.backward = False

    def rotate(self):
        if left:
            self.rotation_angle += self.rotation
        elif right:
            self.rotation_angle -= self.rotation

    def draw(self):
        self.image.rotate_draw(self.rotation_angle, player_x, player_y, 80, 50)

    def update(self):
        if accel_push:
            self.backward = False
            if self.speed < self.speed_limit:
                self.speed += 0.1
        elif accel_idle:
            if not self.break_push:
                if not self.backward:
                    if self.speed > 0:
                        self.speed -= 0.1
        elif self.break_push:
            if self.speed > 0:
                self.speed -= 0.2
            else:
                self.backward = True
        elif self.backward:
            pass

PLAYER_CAR = Car(10, 1)

def move_event():
    global idle, accel_push, accel_idle, dir, dir_y, PLAYER_CAR, left, right

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            accel_push = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_a:
                idle = False
                accel_push = False
                accel_idle = False
                left, right = True, False
                dir -= 1
            elif event.key == SDLK_d:
                idle = False
                accel_push = False
                accel_idle = False
                left, right = False, True
                dir += 1
            elif event.key == SDLK_w:
                idle = False
                accel_push = True
                accel_idle = False
                dir_y += 1
            elif event.key == SDLK_s:
                idle = False
                accel_push = False
                #accel_idle = True
                PLAYER_CAR.break_push = True

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_a:
                idle = True
                accel_push = False
                accel_idle = True
                left, right = False, False
                dir = 0
            elif event.key == SDLK_d:
                idle = True
                accel_push = False
                accel_idle = True
                left, right = False, False
                dir = 0
            elif event.key == SDLK_w:
                idle = True
                accel_push = False
                accel_idle = True
            elif event.key == SDLK_s:
                idle = True
                accel_push = False
                #accel_idle = False
                PLAYER_CAR.break_push = False

while(True):
    clear_canvas()
    map.draw_now(WIDTH//2, HEIGHT//2)
    ui_main.draw_now(WIDTH // 2, HEIGHT // 2)
    ui_1st.draw_now(80, HEIGHT - 50)
    ui_lap.draw_now(250, HEIGHT - 50)
    ui_lap_0.draw_now(360, HEIGHT - 50)
    PLAYER_CAR.draw()
    PLAYER_CAR.rotate()
    PLAYER_CAR.update()
    player_x += dir * PLAYER_CAR.speed
    player_y += dir_y * PLAYER_CAR.speed
    update_canvas()
    move_event()
    delay(0.01)