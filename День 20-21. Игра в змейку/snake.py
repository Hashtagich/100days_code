from turtle import Turtle
MOVE_DISTANCE = 20  # на сколько передвигается змея(одна клетка - куб)
ALFA = {'up': 90, 'left': 180, 'down': 270, 'right': 0}  # словарь для угла поворота змеи
START_POSITION = [(0, 0), (-20, 0), (-40, 0)]  # стартовая позиция первых 3 кубов змеи, начало игры


class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

# Функция создания змеи (3 куба)
    def create_snake(self):
        for position in START_POSITION:
            self.add_segment(position)

# Функция создания одного куска(куба) тела змеи (20х20)
    def add_segment(self, position):
        t = Turtle('square')
        t.color('white')
        t.penup()
        t.goto(position)
        self.snake_body.append(t)

# Функция увеличения змеи
    def extend(self):
        self.add_segment(self.snake_body[-1].position())

# Функция движения змеи вперёд
    def move(self):
        for i in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[i - 1].xcor()
            new_y = self.snake_body[i - 1].ycor()
            self.snake_body[i].goto(new_x, new_y)
        self.snake_body[0].forward(MOVE_DISTANCE)

# Функции поворота змеи с учётом того что она не может разворачиваться на 180 градусов
    def up(self):
        if self.head.heading() != ALFA['down']:
            self.head.setheading(ALFA['up'])

    def down(self):
        if self.head.heading() != ALFA['up']:
            self.head.setheading(ALFA['down'])

    def left(self):
        if self.head.heading() != ALFA['right']:
            self.head.setheading(ALFA['left'])

    def right(self):
        if self.head.heading() != ALFA['left']:
            self.head.setheading(ALFA['right'])
