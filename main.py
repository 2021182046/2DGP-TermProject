from pico2d import *
import math
import sdl2

WIDTH, HEIGHT = 1920, 1080
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

font = load_font('ENCR10B.TTF', 30)
start_time = get_time()

game = True
left, right, front, back = False, False, False, False
move = False

class Car:
    Image_player = player

    def __init__(self, speed_limit, rotation): #속도, 각도
        self.image = self.Image_player

        self.rotation_center_x, self.rotation_center_y = 640, 400

        self.speed = 0
        self.speed_limit = speed_limit
        self.image_rotation_angle = math.radians(-90)
        self.rotation_angle = math.radians(-90)
        self.rotation = rotation
        self.x, self.y = 960, 400
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
                                       self.x, self.y, 80, 50)

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

PLAYER_CAR = Car(5, 1) # 플레이어 생성

while(game):
    clear_canvas()
    map.draw_now(WIDTH//2, HEIGHT//2)
    ui_main.draw_now(WIDTH // 2, HEIGHT // 2)
    ui_1st.draw_now(80, HEIGHT - 50)
    ui_lap.draw_now(250, HEIGHT - 50)
    ui_lap_0.draw_now(360, HEIGHT - 50)

    current_time = get_time()
    elapsed_time = current_time - start_time
    font.draw(500, HEIGHT - 65, 'Lap Time : %.3f' % elapsed_time, (255,255,255))

    PLAYER_CAR.draw()
    PLAYER_CAR.update()
    move_event()
    update_canvas()
    delay(0.01)