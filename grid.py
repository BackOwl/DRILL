import turtle

countx =500
county =300
turtle.penup()
turtle.goto(0,300)
while (county>-300):
    turtle.pendown()
    turtle.goto(500,county)
    turtle.penup()
    county = county-100
    turtle.goto(0,county)

turtle.penup()
county =county+100
turtle.goto(countx,county)
turtle.left(90)
while(countx>-100):
    turtle.pendown()
    turtle.forward(500)
    turtle.penup()
    countx = countx-100
    turtle.goto(countx,county)
turtle.exitonclick()
