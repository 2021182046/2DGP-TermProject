from pico2d import *
from global_values import WIDTH, HEIGHT

start_time = get_time()
ui_main, ui_1st, ui_2nd, ui_3rd, ui_4th, ui_lap, ui_lap_1, ui_lap_2, font \
    = None,None,None,None,None,None,None,None,None


def load_ui():
    global ui_main, ui_1st, ui_2nd, ui_3rd, ui_4th, ui_lap, ui_lap_1, ui_lap_2, font, start_time

    ui_main = load_image('resource/UI_black(1920x1080).png')
    ui_1st = load_image('resource/UI_1st.png')
    ui_2nd = load_image('resource/UI_2nd.png')
    ui_3rd = load_image('resource/UI_3rd.png')
    ui_4th = load_image('resource/UI_4th.png')
    ui_lap = load_image('resource/UI_Lap.png')
    ui_lap_1 = load_image('resource/UI_Lap1.png')
    ui_lap_2 = load_image('resource/UI_Lap2.png')
    font = load_font('resource/ENCR10B.TTF', 30)


def draw_ui():
    global ui_main, ui_1st, ui_2nd, ui_3rd, ui_4th, ui_lap, ui_lap_1, ui_lap_2, font, start_time

    ui_main.draw(WIDTH // 2, HEIGHT // 2)
    ui_1st.draw(80, HEIGHT - 50)
    ui_lap.draw(250, HEIGHT - 50)
    ui_lap_1.draw(360, HEIGHT - 50)

    current_time = get_time()
    elapsed_time = current_time - start_time
    minutes = int(elapsed_time/60)
    second = elapsed_time % 60
    font.draw(500, HEIGHT - 65, 'Lap Time : %d:%.3f' %(minutes, second), (255,255,255))