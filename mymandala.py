from ast import For, pattern
import turtle
t = turtle.Turtle()


t.screen.bgcolor("black")
t.color ("#ffcc00")
t.pensize(2)
t.speed(0)


def pen(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def pattern():
    for i in range(23) :
        t.forward(360)
        t.circle(20)
        t.left(216 + 3)


        
    t.end_fill()

pen (-200, 100)
pattern()

pen (-30, -184)
t.circle(220)

pen(-30, -194)
t.circle(230)

pen(-30, -144)
t.circle(180)

pen(-60, -30)
star()

pen(-21, -10)
t.circle(46)

t.hideturtle()
turtle.done()
