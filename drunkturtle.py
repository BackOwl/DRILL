
import turtle
import random
'''
#파이썬의 장점은 다형성

def add(a,b):
    sum-a+b
    return sum


'''
'''
def drunken_move():
    turtle.setheading(random.randint(0,360))
    turtle.forward(random.randint(50,300))
    turtle.stamp()


turtle.shape('turtle')
turtle.onkey(drunken_move,' ')
turtle.listen()

'''

'''
import turtle
# 중앙좌표 기준으로 원그리기 ( 다르게 )
def draw_circle(x,y,r):
    turtle.penup()
    turtle.goto(x,y)
    turtle.write((x,y,r))
    turtle.goto(x,y-r)
    turtle.pendown()
    turtle.circle(r)
   

turtle.shape("turtle")
draw_circle(0,0,50)
draw_circle(200,200,100)
draw_circle(100,-100,50)


'''
























