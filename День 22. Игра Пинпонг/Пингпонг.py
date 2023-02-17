from turtle import Screen
from board import Tablo
from gamers import Gamer
from ball import Ball
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(800, 600)
screen.title('Настольный теннис')
screen.tracer(0)

board = Tablo()
board.write_score()
gamer = Gamer((-350, 0))
gamer_2 = Gamer((350, 0))
# com = Gamer((350, 0))
ball = Ball()

key = True
while key:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_part_1()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.panch_y()

    if ball.distance(gamer_2) < 50 and ball.xcor() > 320 or ball.distance(gamer) < 50 and ball.xcor() < -320:
        ball.panch_x()

    if ball.xcor() > 380:
        ball.ball_home()
        board.gamer_win()

    if ball.xcor() < -380:
        ball.ball_home()
        board.gamer_2_win()

    # движение игрока №1 через кнопки
    screen.listen()
    screen.onkey(gamer.move_up, 'w')
    screen.onkey(gamer.move_down, 's')

    # движение игрока №2 через стрелки если играем вдвоём
    screen.onkey(gamer_2.move_up, 'Up')
    screen.onkey(gamer_2.move_down, 'Down')

    # цикличное движение компьютера
    # while com.ycor() < 250:
    # com.move_up()
    # while com.ycor() > -250:
    # com.move_down()

screen.exitonclick()
