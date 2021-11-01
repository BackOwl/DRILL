import turtle
import random
import math

def stop():
    turtle.bye()


def prepare_turtle_canvas():
    turtle.setup(1024, 768)
    turtle.bgcolor(0.2, 0.2, 0.2)
    turtle.penup()
    turtle.hideturtle()
    turtle.shape('arrow')
    turtle.shapesize(2)
    turtle.pensize(5)
    turtle.color(1, 0, 0)
    turtle.speed(100)
    turtle.goto(-500, 0)
    turtle.pendown()
    turtle.goto(480, 0)
    turtle.stamp()
    turtle.penup()
    turtle.goto(0, -360)
    turtle.pendown()
    turtle.goto(0, 360)
    turtle.setheading(90)
    turtle.stamp()
    turtle.penup()
    turtle.home()

    turtle.shape('circle')
    turtle.pensize(1)
    turtle.color(0, 0, 0)
    turtle.speed(50)

    turtle.onkey(stop, 'Escape')
    turtle.listen()


def draw_big_point(p):
    turtle.goto(p)
    turtle.color(0.8, 0.9, 0)
    turtle.dot(15)
    turtle.write('     '+str(p))


def draw_point(p):
    turtle.goto(p)
    turtle.dot(5, random.random(), random.random(), random.random())


def draw_line_basic(p1, p2):
    #draw_big_point(p1)
    #draw_big_point(p2)
    
    x1,y1= p1[0],p1[1]
    x2,y2 = p2[0], p2[1]

    for i in range(0,1800,5):
        t = i/360*2*math.pi
        x = -140*math.cos(t) + 200*math.cos(t*0.7)
        y = -140*math.sin(t) - 200*math.sin(t*0.7)
        draw_point((x,y))
    draw_point(p2)
    # fill here
    pass


def draw_line(p1, p2):
    #draw_big_point(p1)
    #draw_big_point(p2)
    
    x1,y1= p1[0],p1[1]
    x2,y2 = p2[0], p2[1]

    for i in range(0,1800,5):
        t = i/360*2*math.pi
        x = 120*math.cos(t) + 200*math.cos(t*0.6)
        y = 120*math.sin(t) - 200*math.sin(t*0.6)
        #x=100+250*math.cos(t)
        #y=100+250*math.sin(t)
        draw_point((x,y))
    draw_point(p2)
        
    # fill here
    pass


prepare_turtle_canvas()
draw_line((-100,50),(100,50))
#draw_line((-100,50),(100,50))
turtle.done()
# fill here

turtle.done()
