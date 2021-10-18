from pico2d import *
import os

os.chdir('C:/Users/백 아울/2DGP/2DGPclone\Labs\Lecture05_Animation')

# fill here

open_canvas()
grass = load_image('grass.png')
character = load_image('character.png')


character.draw(100,100)

update_canvas()
clear_canvas()
delay(5)


close_canvas()
