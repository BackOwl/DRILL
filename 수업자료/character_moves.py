from pico2d import *
import math 
open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

# fill here
x =0
y =90
case =1
check =0
manpai=0
direction = 0
while 1:
    if case ==1:
        if direction ==0:
            while x<400:
                clear_canvas_now()
                grass.draw_now(400,30)
                character.draw_now(x,y)
                x+=2
                delay(0.01)
            direction=4
            check+=1
            if check==2:
                case=0
                check=0
        elif direction ==4:
            while x<800:
                clear_canvas_now()
                grass.draw_now(400,30)
                character.draw_now(x,y)
                x+=2
                delay(0.01)
            direction =1
        elif direction ==1:
            while y<600:
                clear_canvas_now()
                grass.draw_now(400,30)
                character.draw_now(x,y)
                y+=2
                delay(0.01)
            direction =2
        if direction ==2:
            while x>=0:
                clear_canvas_now()
                grass.draw_now(400,30)
                character.draw_now(x,y)
                x-=2
                delay(0.01)
            direction =3
        elif direction ==3:
            while y>=90:
                clear_canvas_now()
                grass.draw_now(400,30)
                character.draw_now(x,y)
                y-=2
                delay(0.01)
            direction =0
    elif case ==0:
        while manpai<360:
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(x,y)
            x=400+250*math.cos(manpai/360*2*math.pi)
            y=400+250*math.sin(manpai/360*2*math.pi)
            manpai+=2
            delay(0.01)
        case =1
        x=0
        y=80
        manpai=0

    
delay(5)
close_canvas()
