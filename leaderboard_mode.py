from pico2d import *
import game_framework

PLAYER_NAME = 'PLAYER 1'
LAP_TIME = None
HP = None

def init():
    global leaderboard_image, board_font
    leaderboard_image = load_image('resource/leaderboard(1600x900).jpg')
    board_font = load_font('resource/ENCR10B.TTF', 30)
def finish():
    pass
def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
def update():
    pass
def draw():
    clear_canvas()
    minutes = int(LAP_TIME / 60)
    second = LAP_TIME % 60
    leaderboard_image.draw(800, 450)
    board_font.draw(500, 550, f'{PLAYER_NAME}', (255, 255, 255))
    board_font.draw(880, 550, '%d:%.3f' % (minutes, second), (255, 255, 255))
    board_font.draw(1240, 550, f'{HP}', (255, 255, 255))
    update_canvas()
