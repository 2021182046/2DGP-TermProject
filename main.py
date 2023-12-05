from pico2d import *
import game_framework, title_mode, leaderboard_mode
from global_values import WIDTH, HEIGHT

open_canvas(WIDTH, HEIGHT, sync=True)

game_framework.run(title_mode)
#game_framework.run(leaderboard_mode)

close_canvas()
