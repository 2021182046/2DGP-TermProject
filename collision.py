from pico2d import *


class Collision_road:
    def __init__(self, left_b, bottom_b, right_b, top_b):
        self.left_b = left_b
        self.bottom_b = bottom_b
        self.right_b = right_b
        self.top_b = top_b

    def draw(self):
        draw_rectangle(*self.collide_box())

    def collide_box(self):
        return self.left_b, self.bottom_b, self.right_b, self.top_b

    def handle_collision(self, group, other):
        if group == 'car:road':
            other.speed_limit = 7
        else:
            other.speed_limit = 4


class Collision_wall:
    def __init__(self, left_b, bottom_b, right_b, top_b):
        self.left_b = left_b
        self.bottom_b = bottom_b
        self.right_b = right_b
        self.top_b = top_b

    def draw(self):
        draw_rectangle(*self.collide_box())

    def collide_box(self):
        return self.left_b, self.bottom_b, self.right_b, self.top_b

    def handle_collision(self, group, other):
        if group == 'car:wall':
            other.speed = -other.speed / 2
            other.move()


def collide(a, b): # 충돌 검사
    left_a, bottom_a, right_a, top_a = a.collide_box()
    left_b, bottom_b, right_b, top_b = b.collide_box()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True


collision_pairs = {}
def add_collision_pair(group, a, b): # 충돌 그룹 등록
    if group not in collision_pairs:
        print(f'Added new group {group}')
        collision_pairs[group] = [ [],[] ]
    if a:
        collision_pairs[group][0].append(a)
    if b:
        collision_pairs[group][1].append(b)

def handle_collisions(): # 충돌 그룹의 충돌 후 동작
    for group, pairs in collision_pairs.items():
        for a in pairs[0]:
            collided = False
            for b in pairs[1]:
                if collide(a, b):
                    a.handle_collision(group, b)
                    b.handle_collision(group, a)
                    collided = True
            if not collided and group ==  'car:road':
                a.speed_limit = 4