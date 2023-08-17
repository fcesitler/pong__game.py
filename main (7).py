import time
from turtle import Turtle, Screen
from puddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up, key="Up")
screen.onkey(r_paddle.down, key="Down")
screen.onkey(l_paddle.up, key="w")
screen.onkey(l_paddle.down, key="s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #how to detect collision with paddle???
    if ball.xcor() > 320 and ball.distance(r_paddle) < 50:
        ball.bounce_x()
        ball.change_color_ball()
        r_paddle.change_color_paddle()

    if ball.xcor() < -320 and ball.distance(l_paddle) < 50:
        ball.bounce_x()
        ball.change_color_ball()
        l_paddle.change_color_paddle()
    if ball.xcor() > 410:
        score.increase_score_l_paddle()
        ball.refresh()

    if ball.xcor() < -410:
        score.increase_score_r_paddle()
        ball.refresh()







screen.exitonclick()
