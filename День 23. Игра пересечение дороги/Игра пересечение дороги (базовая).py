import time
from turtle import Screen
from cars import Car
from player import Player
from scoreboard import Score

# Задаём начальный экран
screen = Screen()
screen.title('Пересеки дорогу!')
screen.setup(600, 600)
screen.bgcolor('SlateGrey')
screen.tracer(0)

tablo = Score()
player = Player()
car = Car()

# Управление черепахой через англ раскладку и стрелки
screen.listen()
screen.onkey(player.go_up, 'w')
screen.onkey(player.go_up, 'Up')
screen.onkey(player.go_down, 's')
screen.onkey(player.go_down, 'Down')

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    car.create_r_car()  # каждую 0.1 секунду создается новая машина с вероятностью 1 к 8
    car.move_left()  # запуск движения авто, двигаются постоянно пока не дойдут до финиша
    # или игра не закончится движение слева
    car.create_l_car()  # каждую 0.1 секунду создается новая машина с вероятностью 1 к 8
    car.move_right()  # запуск движения авто, двигаются постоянно пока не дойдут до финиша
    # или игра не закончится движение слева

    for cars in car.all_cars:  # Проверка на столкновение машины с черепахой
        if cars.distance(player) < 20:
            game_on = False
            tablo.w_game_over()  # игра окончена

    if player.finish():  # Проверка на пересечение финиша
        tablo.w_level()  # Увеличивает уровень на один по тексту
        player.go_home()  # Возвращает черепашку на начальную позицию
        car.speed_up()  # Увеличивает скорость(self.car_speed = STEP) всех авто на MOVE_INCREMENT

screen.exitonclick()
