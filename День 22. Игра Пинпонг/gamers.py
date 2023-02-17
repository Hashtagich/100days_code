from turtle import Turtle

STEP = 20
SPEED = 1


class Gamer(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.speed(SPEED)
        self.penup()
        self.goto(position)
        self.color('white')

    def move_up(self):
        new_y = self.ycor() + STEP
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - STEP
        self.goto(self.xcor(), new_y)
