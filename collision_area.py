from pico2d import *
from collision import Collision_road, Collision_wall, add_collision_pair
from map import Map

def create_collision_area(PLAYER_CAR, MAP):
    walls = [Collision_wall(0, 0, 40, 600),
             Collision_wall(40, 350, 60, 600),
             Collision_wall(60, 600, 70, 700),
             Collision_wall(70, 700, 80, 800),
             Collision_wall(80, 800, 90, 900),
             Collision_wall(90, 900, 100, 930),
             Collision_wall(100, 930, 110, 950),
             Collision_wall(110, 950, 120, 970),
             Collision_wall(120, 960, 150, 980),
             Collision_wall(150, 980, 180, 1000),
             Collision_wall(180, 1000, 220, 1020),
             Collision_wall(220, 1010, 350, 1030),
             Collision_wall(350, 1020, 450, 1040),
             Collision_wall(450, 1010, 600, 1030),
             Collision_wall(600, 1000, 720, 1020),
             Collision_wall(720, 1010, 800, 1030),
             Collision_wall(800, 1020, 880, 1040),
             Collision_wall(880, 1030, 960, 1050),
             Collision_wall(960, 1040, 1100, 1060),
             Collision_wall(1100, 1050, 1200, 1070),
             Collision_wall(1200, 1060, 1280, 1070),
             Collision_wall(1280, 1065, 1360, 1080),
             Collision_wall(1360, 1080, 1440, 1100),

             Collision_wall(210, 0, 250, 200),
             Collision_wall(220, 200, 260, 400),
             Collision_wall(230, 400, 270, 500),
             Collision_wall(250, 500, 270, 550),
             Collision_wall(260, 550, 270, 600),

             Collision_wall(340, 500, 350, 550),
             Collision_wall(340, 550, 350, 600),
             Collision_wall(350, 600, 370, 630),
             Collision_wall(370, 630, 390, 660),
             Collision_wall(390, 650, 420, 680),
             Collision_wall(420, 670, 450, 690),
             Collision_wall(450, 690, 480, 710),
             Collision_wall(480, 700, 510, 720),
             Collision_wall(510, 720, 650, 750),
             Collision_wall(620, 750, 800, 780),
             Collision_wall(750, 780, 1000, 800),
             Collision_wall(900, 800, 1200, 820),
             Collision_wall(1100, 820, 1400, 840),
             Collision_wall(1300, 840, 1600, 860),
             Collision_wall(1500, 860, 1700, 880),
             Collision_wall(1570, 450, 1590, 700),
             Collision_wall(1590, 700, 1610, 750),
             Collision_wall(1610, 750, 1630, 800),
             Collision_wall(1630, 770, 1650, 850),
             Collision_wall(1590, 400, 1610, 450),
             Collision_wall(1610, 350, 1630, 400),
             Collision_wall(1630, 300, 1650, 350),
             Collision_wall(1650, 270, 1670, 320),
             Collision_wall(1670, 250, 1700, 270),
             Collision_wall(1700, 230, 1730, 250),
             Collision_wall(1730, 200, 1760, 230),
             Collision_wall(1760, 170, 1790, 200),
             Collision_wall(1790, 140, 1820, 170),
             Collision_wall(1820, 110, 1850, 140),
             Collision_wall(1850, 80, 1880, 110)

             ]
    for wall in walls:
        add_collision_pair('car:wall', PLAYER_CAR, wall)

    roads = [Collision_road(110, 50, 190, 500),
             Collision_road(130, 500, 220, 700),
             Collision_road(160, 720, 400, 780),
             Collision_road(400, 750, 450, 800),
             Collision_road(250, 800, 600, 850),
             Collision_road(450, 860, 870, 890),
             Collision_road(670, 900, 1350, 940),
             Collision_road(1150, 950, 1800, 980),
             Collision_road(1600, 1000, 1800, 1020),
             Collision_road(1800, 800, 1900, 950),
             Collision_road(1770, 700, 1830, 800),
             Collision_road(1830, 750, 1860, 800),
             Collision_road(1700, 550, 1770, 700),
             Collision_road(1730, 700, 1770, 750),
             Collision_road(1730, 450, 1770, 550),
             Collision_road(1770, 410, 1810, 510),
             Collision_road(1810, 350, 1850, 450),
             Collision_road(1850, 300, 1890, 410)
             ]
    for road in roads:
        add_collision_pair('car:road', PLAYER_CAR, road)

    MAP.set_collision_areas(walls, roads)

    #for road in roads: # 도로 충돌박스 그리기
        #road.draw()
    #for wall in walls:  # 벽 충돌박스 그리기
        #wall.draw()
