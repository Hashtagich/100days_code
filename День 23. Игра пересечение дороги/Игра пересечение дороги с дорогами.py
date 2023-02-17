import time
from turtle import Screen
from cars import Car
from player import Player
from scoreboard import Score
from roads import Road

# Задаём начальный экран
screen = Screen()
screen.title('Пересеки дорогу!')
screen.setup(600, 600)
screen.bgcolor('White')
screen.tracer(0)

# Задаём дорогу и разметку
road = Road()
road.create_line()
road.create_l_line()

tablo = Score()
player = Player()
car = Car()

# Управление черепахой через англ раскладку и стрелки
screen.listen()
screen.onkey(player.go_up, 'w')
screen.onkey(player.go_up, 'Up')
screen.onkey(player.go_down, 's')
screen.onkey(player.go_down, 'Down')
# Дополнительное управление для разнообразия игры
screen.onkey(player.go_left, 'a')
screen.onkey(player.go_left, 'Left')
screen.onkey(player.go_right, 'Right')
screen.onkey(player.go_right, 'd')

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    car.create_r_car()  # каждую 0.1 секунду создается новая машина с вероятностью 1 к 8
    car.move_left()  # запуск движения авто, двигаются постоянно пока не дойдут
    # до финиша или игра не закончится движение слева
    car.create_l_car()  # каждую 0.1 секунду создается новая машина с вероятностью 1 к 8
    car.move_right()  # запуск движения авто, двигаются постоянно пока не дойдут
    # до финиша или игра не закончится движение с право

    for cars in car.all_cars:  # Проверка на столкновение машины с черепахой
        if cars.distance(player) < 20:
            game_on = False
            tablo.w_game_over()  # игра окончена

    if player.finish():  # Проверка на пересечение финиша
        tablo.w_level()  # Увеличивает уровень на один по тексту
        player.go_home()  # Возвращает черепашку на начальную позицию
        car.speed_up()  # Увеличивает скорость(self.car_speed = STEP) всех авто на MOVE_INCREMENT

screen.exitonclick()
