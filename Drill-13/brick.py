import random

from pico2d import *

import game_framework
import game_world


class Brick:
    def __init__(self):
        self.image = load_image('brick180x40.png')
        self.x, self.y = 100, 200
        self.speed = 200 # 200 pixel per second

        self.child_ball =[] # 발판에 속한 볼의 리스트

    def update(self):
        self.x += game_framework.frame_time * self.speed
        if self.x > 1600:
            self.x = 1600
            self.speed = -self.speed
        if self.x < 0:
            self.x = 0
            self.speed = -self.speed

        #자식의 개수를 확인
        if len(self.child_ball)>10:
            # 부모 자식관계를 끊기
            # 가지고 있던 자식들을 balls로 보낸다
            # 발판 부시기
            pass




    def draw(self):
        self.image.draw(self.x, self.y)


    def draw_bb(self):
        draw_rectangle(*self.get_bb())
        pass


    def get_bb(self):
        return self.x-90, self.y-20, self.x+90, self.y+20

    def attach_ball(self,ball):
        # 발판은 볼에대한 리스트가 필요하다
        self.child_ball.append(ball)
        ball.set_parent(self)# 볼에 대해서 부모를 설정 링크

