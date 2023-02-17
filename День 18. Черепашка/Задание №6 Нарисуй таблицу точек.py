import turtle as tim
from random import randint

x, y = 800, 800
step = 50
radius = 20
width, height = 10, 10

t = tim.Turtle()
tim.colormode(255)
screen = tim.Screen()

screen.setup(x, y)
screen.bgcolor('black')

x, y = -350, -370
t.speed('fastest')
t.penup()


def color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    result = (r, g, b)
    return result


def dro_dote():
    t.goto(x, y)

    for _ in range(width):
        t.pencolor(color())
        t.dot(radius)
        t.forward(step)


for _ in range(height):
    dro_dote()
    y += 50

screen.exitonclick()
