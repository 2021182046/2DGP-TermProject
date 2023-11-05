from pico2d import *
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

idle, move = True, False
left, right = False, False
dir, dir_y = 0,0
player_x, player_y = WIDTH//2, HEIGHT//2

class Car:
    Image_player = player

    def __init__(self, speed_limit, rotation): #속도, 각도
        self.image = self.Image_player
        self.speed = 0
        self.speed_limit = speed_limit
        self.rotation_angle = 0
        self.rotation = rotation

    def rotate(self, left, right):
        if left:
            self.rotation_angle += self.rotation
        elif right:
            self.rotation_angle -= self.rotation

    def draw(self):
        self.image.rotate_draw(self.rotation_angle, player_x, player_y, 80, 50)

PLAYER_CAR = Car(50, 1)

def move_event():
    global idle, move, dir, dir_y, PLAYER_CAR

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            move = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_a:
                idle = False
                move = True
                PLAYER_CAR.rotate(True, False)
                dir -= 1
            elif event.key == SDLK_d:
                idle = False
                move = True
                PLAYER_CAR.rotate(False, True)
                dir += 1
            elif event.key == SDLK_w:
                idle = False
                move = True
                dir_y += 1
            elif event.key == SDLK_s:
                idle = False
                move = True
                dir_y -= 1
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_a:
                idle = True
                move = False
                PLAYER_CAR.rotate(False, False)
                dir += 1
            elif event.key == SDLK_d:
                idle = True
                move = False
                PLAYER_CAR.rotate(False, False)
                dir -= 1
            elif event.key == SDLK_w:
                idle = True
                move = False
                dir_y -= 1
            elif event.key == SDLK_s:
                idle = True
                move = False
                dir_y += 1


while(True):
    clear_canvas()
    map.draw_now(WIDTH//2, HEIGHT//2)
    ui_main.draw_now(WIDTH // 2, HEIGHT // 2)
    ui_1st.draw_now(80, HEIGHT - 50)
    ui_lap.draw_now(250, HEIGHT - 50)
    ui_lap_0.draw_now(360, HEIGHT - 50)
    #player.draw_now(player_x, player_y, 80, 50)  # 원본 크기 변경하여 적용
    PLAYER_CAR.draw()
    player_x += dir * 3
    player_y += dir_y * 3
    update_canvas()
    move_event()