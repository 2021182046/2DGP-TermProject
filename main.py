from pico2d import *

WIDTH, HEIGHT = 800, 600
open_canvas(WIDTH, HEIGHT)

map = load_image('map0.png')
player = load_image('player_car.png')

ui_main = load_image('UI_black(800x600).png')
ui_1st = load_image('UI_1st.png')
ui_2nd = load_image('UI_2nd.png')
ui_3rd = load_image('UI_3rd.png')
ui_4th = load_image('UI_4th.png')
ui_lap = load_image('UI_Lap.png')
ui_lap_0 = load_image('UI_Lap0.png')
ui_lap_1 = load_image('UI_Lap1.png')
ui_lap_2 = load_image('UI_Lap2.png')

while(True):
    clear_canvas()
    map.draw_now(WIDTH//2, HEIGHT//2)
    ui_main.draw_now(WIDTH//2, HEIGHT//2)
    ui_1st.draw_now(60, HEIGHT-40)
    ui_lap.draw_now(250, HEIGHT-40)
    ui_lap_0.draw_now(360, HEIGHT-40)
    player.draw_now(WIDTH//2, HEIGHT//2, 80, 50) # 원본 크기 변경하여 적용
    update_canvas()
    delay(0.1)
