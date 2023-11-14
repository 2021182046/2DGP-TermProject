from pico2d import *
import global_values

def move_event():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            global_values.game = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_a:
                global_values.left = True
                global_values.right = False
            elif event.key == SDLK_d:
                global_values.left = False
                global_values.right = True
            elif event.key == SDLK_w:
                global_values.front = True
                global_values.move = True
            elif event.key == SDLK_s:
                global_values.back = True
                global_values.move = True
            elif event.key == SDLK_LSHIFT:
                global_values.boost = True

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_a:
                global_values.left = False
            elif event.key == SDLK_d:
                global_values.right = False
            elif event.key == SDLK_w:
                global_values.front = False
                global_values.move = False
            elif event.key == SDLK_s:
                global_values.back = False
                global_values.move = False
            elif event.key == SDLK_LSHIFT:
                global_values.boost = False