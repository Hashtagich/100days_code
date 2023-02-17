from turtle import Turtle

STEP = 10


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.goto(0, 0)
        self.penup()
        self.shape('circle')
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color('white')
        self.move_speed = 0.1
        self.x_move = STEP
        self.y_move = STEP

    def move_part_1(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def move_part_2(self):
        new_x = self.xcor() - self.x_move
        new_y = self.ycor() - self.y_move
        self.goto(new_x, new_y)

    def panch_y(self):
        self.y_move *= (-1)

    def panch_x(self):
        self.x_move *= (-1)
        self.move_speed *= 0.95

    def ball_home(self):
        self.move_speed = 0.1
        self.goto(0, 0)
        self.panch_x()
        self.panch_y()
