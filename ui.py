from pico2d import *
from global_values import WIDTH, HEIGHT
import leaderboard_mode

ui_main, ui_1st, ui_2nd, ui_3rd, ui_4th, ui_lap, ui_lap_1, ui_lap_2, flag, signal, font \
    = None,None,None,None,None,None,None,None,None,None,None


def load_ui():
    global ui_main, ui_1st, ui_2nd, ui_3rd, ui_4th, ui_lap, ui_lap_1, ui_lap_2, flag, signal, font, start_time

    ui_main = load_image('resource/UI_black(1600x900).png')
    ui_1st = load_image('resource/UI_1st.png')
    ui_2nd = load_image('resource/UI_2nd.png')
    ui_3rd = load_image('resource/UI_3rd.png')
    ui_4th = load_image('resource/UI_4th.png')
    ui_lap = load_image('resource/UI_Lap.png')
    ui_lap_1 = load_image('resource/UI_Lap1.png')
    ui_lap_2 = load_image('resource/UI_Lap2.png')
    flag = load_image('resource/flag.png')
    font = load_font('resource/ENCR10B.TTF', 30)
    signal = [load_image('resource/signal_stop.png'),
              load_image('resource/signal_wait.png'),
              load_image('resource/signal_start.png')]


def draw_ui(PLAYER_CAR, game_state):
    global ui_main, ui_1st, ui_2nd, ui_3rd, ui_4th, ui_lap, ui_lap_1, ui_lap_2, font, start_time

    ui_main.draw(WIDTH // 2, HEIGHT // 2)
    ui_1st.draw(80, HEIGHT - 50)
    ui_lap.draw(250, HEIGHT - 50)
    if PLAYER_CAR.lab_count == 0:
        ui_lap_1.draw(360, HEIGHT - 50)
    elif PLAYER_CAR.lab_count == 1:
        ui_lap_2.draw(360, HEIGHT - 50)
    else:
        ui_lap_2.draw(360, HEIGHT - 50)
        flag.draw(800, 450)

    if game_state == 'start':
        elapsed_time = get_time() - mainmode_start_time
        index = int(elapsed_time)
        if index < len(signal):
            signal[index].draw(800, 450)

    if game_state == 'play':
        current_time = get_time()
        elapsed_time = current_time - mainmode_start_time - 2
        minutes = int(elapsed_time/60)
        second = elapsed_time % 60
        font.draw(500, HEIGHT - 65, 'Lap Time : %d:%.3f' %(minutes, second), (255,255,255))
        leaderboard_mode.LAP_TIME = elapsed_time


def load_main_mode_start_time(start_time): #main_mode에서 시작시간 가져오기
    global mainmode_start_time
    mainmode_start_time = start_time