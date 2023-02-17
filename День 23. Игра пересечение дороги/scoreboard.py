from turtle import Turtle

FONT = ("Courier", 20, 'normal')
POSITION_LEVEL = (-290, 265)


class Score(Turtle):

    def __init__(self):  # Вывод первого уровня на экран
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(POSITION_LEVEL)
        self.level = 0
        self.w_level()

    def w_level(self):  # Повышение уровня на один с отображением
        self.clear()
        self.level += 1
        self.write(f'Level: {self.level}', align="left", font=FONT)

    def w_game_over(self):  # Отображение GAME OVER
        self.goto(0, 0)
        self.write('GAME OVER', align="center", font=FONT)
