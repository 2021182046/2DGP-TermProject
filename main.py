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

idle, move, on_break = True, False, False
dir, dir_y = 0,0
player_x, player_y = WIDTH//2, HEIGHT//2
speed, speed_limit = 0, 10
accel, accel_break, break_abs = 0.5, 0.5, 0


def speed_down():
    global speed, accel_break
    if speed > 0:
        speed -= accel_break
        delay(0.01)
        if speed < 0:
            speed = 0
            move = False

def speed_up():
    global speed, accel
    if speed < speed_limit:
        speed += accel

def move_event():
    global idle, move, dir, dir_y
    global speed, accel

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            move = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_a:
                idle = False
                move = True
                dir -= 1
            elif event.key == SDLK_d:
                idle = False
                move = True
                dir += 1
            elif event.key == SDLK_w:
                idle = False
                move = True
                dir_y += 1
                speed_up()
            elif event.key == SDLK_s:
                idle = False
                move = True
                dir_y -= 1
                speed_down()
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_a:
                idle = True
                move = False
                dir += 1
            elif event.key == SDLK_d:
                idle = True
                move = False
                dir -= 1
            elif event.key == SDLK_w:
                idle = True
                move = False
                on_break = True
                dir_y -= 1
            elif event.key == SDLK_s:
                idle = True
                move = False
                dir_y += 1
                speed_down()


while(True):
    while idle:
        clear_canvas()
        map.draw_now(WIDTH//2, HEIGHT//2)
        ui_main.draw_now(WIDTH//2, HEIGHT//2)
        ui_1st.draw_now(80, HEIGHT-50)
        ui_lap.draw_now(250, HEIGHT-50)
        ui_lap_0.draw_now(360, HEIGHT-50)
        player.draw_now(player_x, player_y, 80, 50) # 원본 크기 변경하여 적용
        player_x += dir*3
        player_y += dir_y*3 + speed
        update_canvas()
        move_event()
        if on_break:
            break_abs += 1
            if break_abs > 10:
                on_break = False
                break_abs = 0
            else:
                while 10:
                    speed_down()
                    delay(0.01)
        delay(0.05)

    while move:
        clear_canvas()
        map.draw_now(WIDTH//2, HEIGHT//2)
        ui_main.draw_now(WIDTH // 2, HEIGHT // 2)
        ui_1st.draw_now(80, HEIGHT - 50)
        ui_lap.draw_now(250, HEIGHT - 50)
        ui_lap_0.draw_now(360, HEIGHT - 50)
        player.draw_now(player_x, player_y, 80, 50)  # 원본 크기 변경하여 적용
        player_x += dir * 3
        player_y += dir_y * 3 + speed
        update_canvas()
        move_event()
        delay(0.05)