from turtle import Turtle, Screen

screen = Screen()
t = Turtle()

x, y = 600, 600
step, alfa = 50, 10

screen.setup(x, y)
screen.bgcolor('Black')
t.color('white')


def go():
    t.forward(step)

def go_bask():
    t.forward(-step)


def turn_left():
    t.left(alfa)


def turn_right():
    t.right(alfa)


def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()


screen.listen()
screen.onkey(go, 'w')
screen.onkey(go_bask, 's')
screen.onkey(turn_left, 'a')
screen.onkey(turn_right, 'd')
screen.onkey(clear, 'c')

screen.exitonclick()
