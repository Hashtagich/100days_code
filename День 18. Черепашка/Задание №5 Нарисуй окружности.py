import turtle as tim
from random import randint

x, y = 800, 800
radius = 100
alfa = 5
num = int(360 / alfa)

t = tim.Turtle()
tim.colormode(255)
screen = tim.Screen()

screen.setup(x, y)
screen.bgcolor('black')

t.speed('fastest')


def color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    result = (r, g, b)
    return result


for _ in range(num):
    t.pencolor(color())
    t.circle(radius)
    t.left(alfa)

screen.exitonclick()
