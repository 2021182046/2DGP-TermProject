from pico2d import *
from collision import Collision_line, Collision_middle_line, Collision_road, Collision_wall, add_collision_pair
from map import Map

roads = []
walls = []
lines = []

def create_collision_area(PLAYER_CAR, MAP):
    global roads, walls, lines, mid_lines
    walls = [Collision_wall(240, -320, 260, 1130),
             Collision_wall(1610, -350, 1630, 1130),

             Collision_wall(260, 1070, 1610, 1100),
             Collision_wall(260, -390, 1610, -380),

             # 타이어
             Collision_wall(1250, 490, 1270, 510),
             Collision_wall(1270, 480, 1290, 500),
             Collision_wall(1280, 470, 1310, 490),
             Collision_wall(1320, 460, 1340, 480),
             Collision_wall(1340, 450, 1360, 470),
             Collision_wall(1360, 440, 1380, 460),
             Collision_wall(1380, 430, 1400, 450),
             Collision_wall(1410, 420, 1430, 440),
             Collision_wall(1430, 400, 1450, 430),
             Collision_wall(1450, 390, 1470, 320),

             Collision_wall(1050, 340, 1070, 360),
             Collision_wall(1070, 320, 1090, 340),
             Collision_wall(1090, 310, 1110, 330),
             Collision_wall(1110, 290, 1130, 310),
             Collision_wall(1130, 280, 1150, 300),
             Collision_wall(1150, 270, 1170, 290),
             Collision_wall(1170, 260, 1190, 280),
             Collision_wall(1190, 250, 1210, 270),
             Collision_wall(1210, 240, 1230, 260),
             Collision_wall(1230, 240, 1250, 260),
             Collision_wall(1250, 230, 1270, 250),

             Collision_wall(890, -110, 980, -90),
             Collision_wall(1110, -110, 1180, -90),

             Collision_wall(1010, -130, 1040, -90),
             Collision_wall(1050, -110, 1070, -90),
             Collision_wall(1050, -140, 1070, -130),
             Collision_wall(1030, -150, 1050, -130),
             Collision_wall(1090, -100, 1110, -80),
             ]
    for wall in walls:
        add_collision_pair('car:wall', PLAYER_CAR, wall)

    roads = [Collision_road(450, 20, 560, 780),

             Collision_road(450, 800, 570, 840),
             Collision_road(480, 840, 600, 880),
             Collision_road(510, 880, 630, 920),
             Collision_road(560, 920, 700, 960),

             Collision_road(640, 890, 920, 1010),

             Collision_road(890, 920, 1050, 960),
             Collision_road(960, 880, 1110, 920),
             Collision_road(860, 990, 1110, 880),
             Collision_road(880, 950, 1140, 840),

             Collision_road(1040, 530, 1150, 800),

             Collision_road(1060, 490, 1170, 530),
             Collision_road(1080, 450, 1210, 490),
             Collision_road(1120, 410, 1320, 450),
             Collision_road(1180, 370, 1380, 410),
             Collision_road(1260, 330, 1440, 370),
             Collision_road(1340, 290, 1480, 330),
             Collision_road(1380, 250, 1500, 290),

             Collision_road(1390, -50, 1500, 250),

             Collision_road(1370, -90, 1470, -50),
             Collision_road(1350, -130, 1450, -90),
             Collision_road(1330, -170, 1430, -130),
             Collision_road(1290, -210, 1390, -170),

             Collision_road(770, -220, 1290, -110),

             Collision_road(650, -190, 770, -150),
             Collision_road(590, -150, 770, -110),
             Collision_road(550, -110, 650, -70),
             Collision_road(510, -70, 610, -30),
             Collision_road(490, -30, 590, 10)
             ]
    for road in roads:
        add_collision_pair('car:road', PLAYER_CAR, road)

    lines = [Collision_line(390, 450, 610, 500)]
    for line in lines:
        add_collision_pair('car:line', PLAYER_CAR, line)

    mid_lines = [Collision_middle_line(1320, 150, 1570, 200)]
    for mid_line in mid_lines:
        add_collision_pair('car:mid_line', PLAYER_CAR, mid_line)


    MAP.set_collision_areas(walls, roads, lines, mid_lines)

    # for road in roads: # 도로 충돌박스 그리기
    #     road.draw()
    # for wall in walls:  # 벽 충돌박스 그리기
    #     wall.draw()
