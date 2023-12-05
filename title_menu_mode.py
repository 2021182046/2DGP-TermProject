from pico2d import *
from sdl2 import SDL_QUIT, SDL_KEYDOWN, SDLK_ESCAPE, SDLK_SPACE

import game_framework
import main_mode


def init():
    global image, bgm

    image = load_image('resource/mainmenu.jpg')

    bgm = load_music('resource/titanium_bgm.mp3')
    bgm.set_volume(2)
    bgm.repeat_play()
    #배경 이미지 출처 : https://www.freepik.com/free-ai-image/shiny-sports-car-driving-illuminated-sports-track-generative-ai_48632269.htm#query=f1%20racing&position=13&from_view=keyword&track=ais&uuid=d73ef0f7-1234-4f00-b83c-3a5f206808cc
    #폰트 : 넥슨 LV1고딕


def finish():
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            bgm.stop()
            game_framework.change_mode(main_mode)

def update():
    pass

def draw():
    clear_canvas()
    image.draw(800,450)
    update_canvas()
