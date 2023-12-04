from pico2d import *
from car import Car
from collision_area import create_collision_area, roads, walls
import global_values
from map import Map
from control_car import move_event
from ui import load_ui, draw_ui
from collision import Collision_road, Collision_wall, add_collision_pair, handle_collisions


def init():
    global PLAYER_CAR, MAP, game_state, start_time
    load_ui()
    PLAYER_CAR = Car(4, 1, 530, 400)
    MAP = Map()
    create_collision_area(PLAYER_CAR, MAP)
    game_state = 'start'
    start_time = get_time()

def finish():
    close_canvas()

def handle_events():
    global game_state
    if game_state == 'play':
        move_event()

def update():
    global game_state, start_time
    current_time = get_time()
    if game_state == 'start' and current_time - start_time > 3:
        game_state = 'play'
    if game_state == 'play':
        PLAYER_CAR.update()
        MAP.update(PLAYER_CAR.x, PLAYER_CAR.y, PLAYER_CAR.speed)
        handle_collisions()
    delay(0.01)

def draw():
    global game_state
    clear_canvas()
    MAP.draw()
    PLAYER_CAR.draw()
    draw_ui(PLAYER_CAR, game_state)
    for road in roads:  # 도로 충돌박스 그리기
        Collision_road.draw(road)
    for wall in walls:  # 벽 충돌박스 그리기
        Collision_road.draw(wall)
    update_canvas()
