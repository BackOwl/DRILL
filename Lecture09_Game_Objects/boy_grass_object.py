from pico2d import *
import random

# 내가 게임을 플레이함에 필요한 객체를 꼽아서( 소년, 잔디) 추상화
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class BALL:
    def __init__(self):
        ran = random.randint(0, 1)
        self.x = random.randint(0, 800)
        self.y = 599
        self.speed = random.randint(1, 20)

        #self.image = load_image('ball21x21.png')
        if ran == 0:
            self.image = load_image('ball21x21.png')
            self.xx =21
        elif ran == 1:
            self.image = load_image('ball41x41.png')
            self.xx =41


    def update(self):
        self.y -= self.speed
        if (self.y - self.xx) < 0:
            self.y = 0 +(self.xx //2)

    def draw(self):
        self.image.draw(self.x, self.y)


class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100,400), 90
        self.frame = 0
        self.image = load_image('ball21x21.png')

    def update(self):
        self.x += 0
        self.frame = (self.frame + 1) % 18

    def draw(self):
        self.image.draw(self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


# initialization code
open_canvas()
grass = Grass()  # 잔디 객체 생성
boy = Boy()
team = [BALL() for i in range(1, 10+1)]
running = True
# game main loop code
while running:
    handle_events()

    # game logic
    for boy in team:
        boy.update()

    # game drawing
    clear_canvas()
    grass.draw()
    boy.draw()
    for ball in team:
        ball.draw()
    update_canvas()

    delay(0.1)
# finalization code

close_canvas()
