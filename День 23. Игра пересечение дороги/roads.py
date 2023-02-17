from turtle import Turtle

X = 0
POSITION_B_LINE = [(X, 250), (X, 150), (X, 50), (X, -150), (X, -250), (X, -50)]
POSITION_W_LINE = [(X, 200), (X, 100), (X, 0), (X, -100), (X, -200)]


class Road(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('square')
        self.shapesize(stretch_len=30, stretch_wid=25)
        self.color('SlateGrey')
        self.goto(0, 0)

    def create_line(self):
        for i in POSITION_B_LINE:
            t = Turtle()
            t.shape('square')
            t.shapesize(stretch_len=30, stretch_wid=0.2)
            t.penup()
            t.speed('fastest')
            t.color('Black')
            t.goto(i)

    def create_l_line(self):
        for i in POSITION_W_LINE:
            t = Turtle()
            t.shape('square')
            t.shapesize(stretch_len=30, stretch_wid=0.1)
            t.penup()
            t.speed('fastest')
            t.color('White')
            t.goto(i)
