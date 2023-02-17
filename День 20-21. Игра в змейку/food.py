from turtle import Turtle
from random import randint


class Food(Turtle):  # Функция создания кусочка еды

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # размер
        self.color('blue')
        self.speed('fastest')  # отключение анимации
        self.new_food()

    def new_food(self):  # Функция случайного расположения кусочка еды
        random_x = randint(-280, 280)
        random_y = randint(-280, 280)
        self.goto(random_x, random_y)
