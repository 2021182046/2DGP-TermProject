from pico2d import *
from car import Car
from collision_area import create_collision_area
from map import Map
from control_car import move_event
from ui import load_ui, draw_ui
from collision import Collision_road, Collision_wall, add_collision_pair, handle_collisions

def init():
    global PLAYER_CAR, MAP
    load_ui()
    PLAYER_CAR = Car(7, 1)
    MAP = Map()
    create_collision_area(PLAYER_CAR)

def finish():
    close_canvas()

def handle_events():
    move_event()

def update():
    PLAYER_CAR.update()
    MAP.update(PLAYER_CAR.x, PLAYER_CAR.y)
    handle_collisions()
    delay(0.01)

def draw():
    clear_canvas()
    MAP.draw()
    PLAYER_CAR.draw()
    draw_ui()
    update_canvas()
