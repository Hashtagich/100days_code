from turtle import Turtle

STARTING_POSITION = (0, -280)  # стартовая точка
STEP = 10  # шаг черепахи
FINISH_LINE = 260  # финишная черта


class Player(Turtle):

    def __init__(self):  # Создаём черепашку
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.color('green')
        self.go_home()
        self.setheading(90)

    def go_up(self):  # Движение черепашки вверх
        self.forward(STEP)

    def go_down(self):  # Движение черепашки вниз
        self.forward(-STEP)

    def go_left(self):  # Доп.опция движение влево
        new_x = self.xcor() - STEP
        self.goto(new_x, self.ycor())

    def go_right(self):  # Доп.опция движение вправо
        new_x = self.xcor() + STEP
        self.goto(new_x, self.ycor())

    def go_home(self):  # Возвращение черепашки на стартовую позицию
        self.goto(STARTING_POSITION)

    def finish(self):  # Выводим True если черепаха перешла дорогу
        return self.ycor() > FINISH_LINE
