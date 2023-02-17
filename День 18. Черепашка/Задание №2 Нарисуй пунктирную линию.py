from turtle import Turtle, Screen

x, y = 400, 400
step = 100

t = Turtle()
screen = Screen()

screen.setup(x, y)
screen.bgcolor('black')
x = -200
y = 0
t.pencolor('white')
t.penup()
t.goto(x, y)
t.pendown()

for _ in range(15):
    t.forward(10)
    t.penup()
    t.forward(10)
    t.pendown()
    
screen.exitonclick()
