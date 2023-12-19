from turtle import Screen
from ball import Ball
from bats import Bats
from scoreboard import Scoreboard


def convert_heading(angle):
    return (360 - angle) if angle <= 180 else (360 - angle - 360)

def calculate_reflection_angle(incident_angle, surface_angle):
    reflection_angle = 2 * surface_angle - incident_angle
    return reflection_angle

scoreboard = Scoreboard()
ball = Ball()
bats = Bats()
screen = Screen()
screen.setup(width=1000,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
x_score = 0
y_score = 0
bats.xbat()
bats.ybat()
is_done = False
scoreboard.score(x_score,y_score)

screen.listen()
screen.onkey(bats.yup, "Up")
screen.onkey(bats.ydown, "Down")
screen.onkey(bats.xup, "w")
screen.onkey(bats.xdown, "s")


while is_done == False:
    ball.move(is_done)
    scoreboard.score(x_score, y_score)
    if bats.tim.distance(ball) < 50 :
        print("made contact")
        ball.change_angle(180-ball.heading())
        ball.move(is_done)

    if bats.timy.distance(ball) < 50:
        print("made contact")
        angle = convert_heading(180-ball.heading())
        ball.change_angle(angle)
        ball.move(is_done)

    '''
    if ball.xcor()<-490:
        y_score += 1
        scoreboard.score(x_score,y_score)
        ball.reset()
        ball.move(is_done)
    if ball.xcor()>490:
        x_score += 1
        scoreboard.score(x_score,y_score)
        ball.reset()
        ball.move(is_done)
    if ball.ycor() > 300:
        ball.bounce()
        ball.move(is_done)
    if ball.ycor() < -300:
        ball.bounce()
        ball.move(is_done)
    '''


