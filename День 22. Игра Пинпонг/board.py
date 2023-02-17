from turtle import Turtle
STEP = 20
THICK = 1
X = 0
Y = 600
Y_TABLO = 250
Y_1 = Y/(-2)
TURN = int(Y / (STEP*2))

ALIGNMENT = "center"  # Параметр расположения текста
FONT = ("Courier", 36, "normal")  # Картеж параметров стиля текста


class Tablo(Turtle):

    def __init__(self):
        super().__init__()
        self.gamer = 0
        self.com = 0
        self.penup()
        self.hideturtle()
        self.color('white')
        self.pensize(THICK)
        self.speed('fastest')

    def line(self):
        self.goto(X, Y_1)
        self.setheading(90)
        for _ in range(TURN):
            self.forward(STEP)
            self.pendown()
            self.forward(STEP)
            self.penup()

    def write_score(self):
        self.clear()
        self.line()
        self.goto(X, Y_TABLO)
        self.write(f'{self.gamer} {self.com}', align=ALIGNMENT, font=FONT)

    def gamer_win(self):
        self.gamer += 1
        self.write_score()

    def gamer_2_win(self):
        self.com += 1
        self.write_score()
