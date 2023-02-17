from turtle import Turtle

ALIGNMENT = "center"  # Параметр расположения текста
FONT = ("Courier", 14, "normal")  # Картеж параметров стиля текста
X, Y = 0, 280  # Координаты текста
TEXT = 'Результат :'


class Scoreboard(Turtle):  # Функция создания текста "Результат"

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(X, Y)
        self.total = 0
        self.write_score()

    def write_score(self):  # Функция вывода текста с увеличением очков на один
        self.clear()
        self.write(f'{TEXT} {self.total}', align=ALIGNMENT, font=FONT)
        self.total += 1

    def write_game_over(self):  # Функция вывода текста "GAME OVER"
        self.goto(0, 0)
        self.write(f'GAME OVER', align=ALIGNMENT, font=FONT)
