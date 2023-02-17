from turtle import Turtle
from random import choice, randint

COLORS = ['LightCoral', 'orange', 'khaki', 'green', 'blue', 'purple']  # палитра цветов
MOVE_INCREMENT = 3  # шаг увеличение скорости
STEP = 5  # начальная скорость авто
X_START_R_CAR = 300  # стартовая точка авто, начинающей движение с правой стороны
X_END_R_CAR = -300  # финишная точка авто, начинающей движение с правой стороны
POSITION_R_CARS = [237, 213, 135, 112, 37, 13, -63, - 86, -186, -163]


class Car:

    def __init__(self):
        self.right_cars = []
        self.left_cars = []
        self.car_speed = STEP
        self.all_cars = []

    def create_r_car(self):  # Создаём одну машину и помещаем в список машин
        num = randint(1, 8)
        if num == 1:
            new_car = Turtle()
            new_car.penup()
            new_car.color(choice(COLORS))
            new_y = choice(POSITION_R_CARS)
            new_car.goto(X_START_R_CAR, new_y)
            new_car.shape('square')
            new_car.shapesize(stretch_len=1.8, stretch_wid=0.8)
            self.right_cars.append(new_car)
            self.all_cars.append(new_car)

    def create_l_car(self):  # Создаём одну машину и помещаем в список машин
        num = randint(1, 8)
        if num == 1:
            new_car = Turtle()
            new_car.penup()
            new_car.color(choice(COLORS))
            new_y = choice(POSITION_R_CARS)
            new_car.goto(-X_START_R_CAR, -new_y)
            new_car.shape('square')
            new_car.shapesize(stretch_len=1.8, stretch_wid=0.8)
            self.left_cars.append(new_car)
            self.all_cars.append(new_car)

    def move_left(self):  # Движение слева направо
        for car in self.right_cars:
            car.forward(-self.car_speed)

    def move_right(self):  # Движение слева направо
        for car in self.left_cars:
            car.forward(self.car_speed)

    def speed_up(self):  # Увеличение скорости авто
        self.car_speed += MOVE_INCREMENT
