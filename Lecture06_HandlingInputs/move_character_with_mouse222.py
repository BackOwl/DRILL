from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 800, 600
open_canvas()

kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
mouseimg = load_image('hand_arrow.png')


def handle_events():
   global running
   global mx, my
   events = get_events()
   for event in events:
       if event.type == SDL_QUIT:
           running = False
       elif event.type == SDL_MOUSEMOTION:
           mx, my = event.x, KPU_HEIGHT -1 -event.y
           
       elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
           running = False
   pass


# fill here
def update_character():
   global x, y
   running = x<mx
   x = ( 1-0.005 )*x+0.005*mx
   y = ( 1-0.005 )*y+0.005*my
   

running = True
running_right =True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
mx, my = KPU_WIDTH *2 // 3, KPU_HEIGHT*2//3
frame = 0
hide_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    update_character()
    
    if running_right :
       character.clip_draw(frame * 100, 100*1 ,100, 100, x, y)
    else:
       character.clip_draw(frame * 100, 100*2 ,100, 100, x, y)
    
    mouseimg.draw(mx,my)
    update_canvas()
    frame = (frame + 1) % 8

    handle_events()

close_canvas()




