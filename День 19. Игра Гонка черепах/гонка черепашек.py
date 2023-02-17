from turtle import Turtle, Screen
from random import randint

screen = Screen()
x, y = 600, 400
screen.setup(x, y)
screen.bgcolor('Black')
key = False

list_turtle = []
list_color = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

x = x/(-2) + 15
y = y/(-2) + 50

user_bet = screen.textinput(title='Делайте Ваши ставки.',
                            prompt='Выберите цвет черепашки.''\nred, orange, yellow, green, blue или purple')

for i in range(len(list_color)):
    turtle = Turtle()
    turtle.shape('turtle')
    turtle.speed(7)
    turtle.color(list_color[i])
    turtle.penup()
    turtle.goto(x, y)
    list_turtle.append(turtle)
    y += 50

if user_bet:
    key = True

while key:
    for t in list_turtle:

        if t.xcor() > 275:
            key = False
            winning_color = t.pencolor()

            if winning_color == user_bet:
                print(f'Вы победили! Выиграла черепашка {winning_color} цвета!')
            else:
                print(f'Вы проиграли! Выиграла черепашка {winning_color} цвета!')

        num = randint(0, 10)
        t.forward(num)

screen.exitonclick()
