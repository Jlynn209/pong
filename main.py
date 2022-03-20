import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

left_paddle = Paddle(-350, 0)
right_paddle = Paddle(350, 0)
ball = Ball()
scoreboard_left = Scoreboard(-300, 260)
scoreboard_right = Scoreboard(300, 260)

screen.listen()
screen.onkeypress(right_paddle.go_up, "Up")
screen.onkeypress(right_paddle.go_down, "Down")
screen.onkeypress(left_paddle.go_up, "w")
screen.onkeypress(left_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    left_paddle.limit()
    right_paddle.limit()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.xcor() > 320 and ball.distance(right_paddle) < 50 or ball.xcor() < -320 and ball.distance(left_paddle) < 50:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard_left.increase_score()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard_right.increase_score()

screen.exitonclick()
