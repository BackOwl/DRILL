import random
import json
import os

from pico2d import *
import game_framework
import game_world
import sever
import collision

from boy import Boy
from grass import Grass
from ball import Ball
from brick import Brick

name = "MainState"




def enter():
    sever.boy = Boy()
    game_world.add_object(sever.boy, 1)

    sever.grass = Grass()
    game_world.add_object(sever.grass, 0)

    sever.balls = [Ball() for i in range(200)]
    game_world.add_objects(sever.balls, 1)


    sever.brick = Brick()
    game_world.add_object(sever.brick, 1)



def exit():
    game_world.clear()

def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        else:
            sever.boy.handle_event(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update()
# 객체들이 알아서 업데이트 해야함 밑에 명령어들을 객체들로 옳겨야함, 잔디가. 볼이 스스로
# 잔디가 충돌을 체크하도록 만들어본다 - grass 에 완료
# 소년과 볼이 체크 - boy에 완료
# ball과 brick 에 처리 - brick에서 다루자 
    for ball in sever.balls.copy():

        #if collision.collide(ball, sever.grass):
            #ball.stop()
        if collision.collide(ball, sever.boy):
            #sever.balls.remove(ball)
            #game_world.remove_object(ball)
            pass
        #elif collision.collide(ball,sever.brick):
            # 발판과 충돌이 발생했을 경우 발판에 볼을 담음
            #sever.brick.attach_ball(ball)
            #sever.balls.remove(ball) # 발판에 포함되었기 때문에 충돌체크 x
            #sever.brick.attach_ball(ball)
        else: #볼이 발판볼과 충돌
            for brick_ball in sever.brick.child_ball:
                if collision.collide(ball, brick_ball):
                    sever.brick.attach_ball(ball)
                    sever.balls.remove(ball)
                    break











def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()






