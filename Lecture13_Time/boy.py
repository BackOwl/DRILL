import game_framework
from pico2d import *
from ball import Ball

import game_world

# Boy Run Speed
# fill expressions correctly
PIXEL_PER_METER = 0
RUN_SPEED_KMPH = 0
RUN_SPEED_MPM = 0
RUN_SPEED_MPS = 0
RUN_SPEED_PPS = 0

# Boy Action Speed
PIXEL_PER_METER = (10.0/0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM =(RUN_SPEED_KMPH * 1000.0/60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM /60.0)
RUN_SPEED_PPS = ( RUN_SPEED_MPS * PIXEL_PER_METER)

# fill expressions correctly
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8



# Boy Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP,UP_DOWN, DOWN_DOWN,DOWN_UP,UP_UP, SLEEP_TIMER, SPACE = range(10)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,

    (SDL_KEYDOWN, SDLK_UP): UP_DOWN,
    (SDL_KEYDOWN, SDLK_DOWN): DOWN_DOWN,
    (SDL_KEYUP, SDLK_UP): UP_UP,
    (SDL_KEYUP, SDLK_DOWN): DOWN_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE
}


# Boy States

class IdleState:

    def enter(boy, event):

        if event == RIGHT_DOWN:
            boy.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            boy.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            boy.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            boy.velocity += RUN_SPEED_PPS
        elif event == UP_DOWN:
            boy.velocityy += RUN_SPEED_PPS
        elif event == DOWN_DOWN:
            boy.velocityy -= RUN_SPEED_PPS
        elif event == UP_UP:
            boy.velocityy -= RUN_SPEED_PPS
        elif event == DOWN_UP:
           boy.velocityy += RUN_SPEED_PPS
        boy.timer = 1000



    def exit(boy, event):
        if event == SPACE:
            boy.fire_ball()

        pass

    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        boy.timer -= 1
        if boy.timer == 0:
            boy.add_event(SLEEP_TIMER)

    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_draw(int(boy.frame) * 100, 300, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(int(boy.frame) * 100, 200, 100, 100, boy.x, boy.y)


class RunState:

    def enter(boy, event):
        # fill here
        if event == RIGHT_DOWN:
            boy.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            boy.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            boy.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            boy.velocity += RUN_SPEED_PPS
        elif event == UP_DOWN:
            boy.velocityy += RUN_SPEED_PPS
        elif event == DOWN_DOWN:
            boy.velocityy -= RUN_SPEED_PPS
        elif event == UP_UP:
            boy.velocityy -= RUN_SPEED_PPS
        elif event == DOWN_UP:
           boy.velocityy += RUN_SPEED_PPS
        boy.dir = clamp(-1,boy.velocity,1)


    def exit(boy, event):
        if event == SPACE:
            boy.fire_ball()



    def do(boy):
        # fill here
        boy.frame = (boy.frame + FRAMES_PER_ACTION*ACTION_PER_TIME*game_framework.frame_time) % 8
        boy.x += boy.velocity * game_framework.frame_time
        boy.y += boy.velocityy * game_framework.frame_time
        boy.x = clamp(25, boy.x, 1600 - 25)
        boy.y = clamp(25, boy.y, 1600 - 25)
        # for event in boy.event_que:
        #     if event == DOWN_UP or UP_UP or LEFT_UP or RIGHT_UP:
        #         check = True
        #         if check == True:
        #             for events in boy.event_que:
        #                 if events == DOWN_DOWN or UP_DOWN or LEFT_DOWN or RIGHT_DOWN:
        #                     boy.add_event(RunState)
        #                     boy.fire_ball()
        #                     break

    @staticmethod
    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_draw(int(boy.frame) * 100, 100, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(int(boy.frame) * 100, 0, 100, 100, boy.x, boy.y)


class SleepState:

    def enter(boy, event):
        boy.frame = 0

    def exit(boy, event):
        pass

    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8

    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_composite_draw(int(boy.frame) * 100, 300, 100, 100, 3.141592 / 2, '', boy.x - 25, boy.y - 25, 100, 100)
        else:
            boy.image.clip_composite_draw(int(boy.frame) * 100, 200, 100, 100, -3.141592 / 2, '', boy.x + 25, boy.y - 25, 100, 100)






next_state_table = {
    IdleState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState,
                UP_UP: IdleState, DOWN_UP: IdleState, UP_DOWN: RunState, DOWN_DOWN: RunState,
                SLEEP_TIMER: SleepState, SPACE: IdleState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: RunState, RIGHT_DOWN: RunState,
               UP_UP: IdleState, DOWN_UP: IdleState, UP_DOWN: RunState, DOWN_DOWN: RunState,
               SPACE: RunState},
    SleepState: {LEFT_DOWN: RunState, RIGHT_DOWN: RunState, LEFT_UP: RunState, RIGHT_UP: RunState, SPACE: IdleState}
}

class Boy:

    def __init__(self):
        self.x, self.y = 1600 // 2, 90
        # Boy is only once created, so instance image loading is fine
        self.image = load_image('animation_sheet.png')
        # fill here
        self.font = load_font('ENCR10B.TTF',16)
        self.dir = 1
        self.velocity = 0
        self.velocityy= 0
        self.frame = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)


    def fire_ball(self):
        ball = Ball(self.x, self.y, self.dir*3)
        game_world.add_object(ball, 1)


    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        self.font.draw(self.x-60,self.y+60,'(Time:%3.2f)'%get_time())
        # fill here
        debug_print('velocity_x :' + str(self.velocity) + '  Dir:' + str(
            self.dir) + 'State: ' + self.cur_state.__name__ )

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

