from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(x, y)
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"{self.score}", align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()
