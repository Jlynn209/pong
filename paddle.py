from turtle import Turtle

WIDTH = 1
HEIGHT = 5


class Paddle(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.start_x_pos = x
        self.start_y_pos = y
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(HEIGHT, WIDTH)
        self.goto(self.start_x_pos, self.start_y_pos)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
