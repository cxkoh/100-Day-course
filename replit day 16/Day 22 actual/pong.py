from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

scoreboard = Scoreboard()
screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
x_score=0
y_score=0

game_is_on = True
while game_is_on:
    scoreboard.score(x_score, y_score)
    time.sleep(0.05)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.distance(r_paddle)<50 and ball.xcor() > 340:
        ball.bounce_x()

    if ball.distance(l_paddle)<50 and ball.xcor() < -340:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset()
        y_score += 1
        scoreboard.score(x_score,y_score)

    if ball.xcor() < -380:
        ball.reset()
        x_score += 1
        scoreboard.score(x_score,y_score)






screen.exitonclick()