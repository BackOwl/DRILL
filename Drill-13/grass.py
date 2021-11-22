from pico2d import *
import sever
import collision

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def update(self):
        # 잔디가 볼들으 ㅣ충돌을 검사하도록 함
        for ball in sever.balls:
            if collision.collide(ball,self):
                ball.stop()

    def draw(self):
        self.image.draw(400, 30)
        self.image.draw(1200, 30)
        # fill here
        draw_rectangle(*self.get_bb())


    # fill here
    def get_bb(self):
        return 0, 0, 1600-1, 50
