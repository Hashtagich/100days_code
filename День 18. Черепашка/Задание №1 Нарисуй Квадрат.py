from turtle import Turtle, Screen

x, y = 400, 400
step = 100

t = Turtle()
screen = Screen()

screen.setup(x, y)
screen.bgcolor('black')

t.pencolor('white')

for _ in range(4):
    t.forward(100)
    t.left(90)

screen.exitonclick()
