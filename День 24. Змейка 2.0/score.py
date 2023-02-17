from turtle import Turtle

ALIGNMENT = "center"  # Параметр расположения текста
FONT = ("Courier", 14, "normal")  # Картеж параметров стиля текста
X, Y = 0, 280  # Координаты текста
TEXT = 'Результат :'
TEXT_1 = 'Лучший результат :'
NAME_FILE = 'data.txt'


class Scoreboard(Turtle):  # Функция создания текста "Результат"

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(X, Y)
        self.total = 0
        self.read_file()
        self.write_score()

    def reset_game(self): # Функция обнуления результата и обновления лучшего результата
        if self.total > self.high_score:
            self.high_score = self.total
        self.write_file()
        self.total = 0
        self.write_score()

    def up_total(self): # Функция увеличения результата на 1
        self.total += 1
        self.write_score()

    def write_score(self):  # Функция вывода текста с увеличением очков на один
        self.clear()
        self.write(f'{TEXT} {self.total} {TEXT_1} {self.high_score}', align=ALIGNMENT, font=FONT)

    def write_game_over(self):  # Функция вывода текста "GAME OVER"
        self.goto(0, 0)
        self.write(f'GAME OVER', align=ALIGNMENT, font=FONT)

    def read_file(self):  # Функция чтения данных из текстового файла
        with open(NAME_FILE, 'rt', encoding='utf-8') as file:
            num = file.read()
            self.high_score = int(num)

    def write_file(self):  # Функция перезаписи данных в текстовом файле для сохранения результата
        with open(NAME_FILE, 'w', encoding='utf-8') as file:
            score = str(self.high_score)
            file.write(score)
