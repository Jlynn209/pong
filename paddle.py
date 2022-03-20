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
        self.max_top = False
        self.max_bot = False

    def limit(self):
        if self.ycor() > 230:
            self.max_top = True
        else:
            self.max_top = False

        if self.ycor() < -230:
            self.max_bot = True
        else:
            self.max_bot = False

    def go_up(self):
        if not self.max_top:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def go_down(self):
        if not self.max_bot:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)


