import turtle as tim
from random import choice, randint

x, y = 800, 800
step = 30
alfa = [0, 90, 180, 270]

t = tim.Turtle()
tim.colormode(255)
screen = tim.Screen()

screen.setup(x, y)
screen.bgcolor('black')

t.pencolor('white')
t.speed(9)
t.pensize(10)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    result = (r, g, b)
    return result


def line():
    t.pencolor(random_color())
    t.forward(step)
    t.setheading(choice(alfa))


for i in range(200):
    line()

screen.exitonclick()
