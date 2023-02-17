from turtle import Turtle, Screen
from random import choice

x, y = 800, 800
step = 50
side = 3
color = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'SeaGreen']

t = Turtle()
screen = Screen()

screen.setup(x, y)
screen.bgcolor('black')

x, y = -50, 300
t.pencolor('white')
t.penup()
t.speed(7)
t.goto(x, y)
t.pendown()


def figure(number):
    alfa = 360 / side
    for _ in range(number):
        t.forward(100)
        t.right(alfa)
    t.pencolor(choice(color))


for i in range(7):
    figure(side)
    side += 1

screen.exitonclick()
