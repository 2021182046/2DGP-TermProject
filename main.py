from pico2d import *
from car import Car
from map import Map
from ui import load_ui, draw_ui
from control_car import move_event
from collision import Collision_road, Collision_wall, add_collision_pair, handle_collisions
from collision_area import create_collision_area
import game_framework, title_mode
from global_values import WIDTH, HEIGHT, game, left, right, front, back, boost, move

open_canvas(WIDTH, HEIGHT)

game_framework.run(title_mode)

close_canvas()
