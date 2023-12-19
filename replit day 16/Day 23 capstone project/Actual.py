from turtle import Turtle, Screen
import time
from Cars import Car
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("white")
screen.title("Crossyroad")
screen.tracer(0)
speed = 5
delay = 1
level = 1
cars = []

def up(tim):
    tim.setheading(90)
    tim.forward(20)
def left(tim):
    tim.setheading(180)
    tim.forward(20)
def right(tim):
    tim.setheading(0)
    tim.forward(20)

scoreboard = Scoreboard()
car = Car()
tim = Turtle('turtle')
tim.color("green")
tim.penup()
tim.goto(0,-280)
tim.setheading(90)
screen.listen()
screen.onkey(lambda: up(tim), "Up")
screen.onkey(lambda: left(tim), "Left")
screen.onkey(lambda: right(tim), "Right")

is_ongoing = True
while is_ongoing:
    scoreboard.score(level)
    time.sleep(0.1)
    screen.update()
    car.move()
    car.move_car(speed)

    for c in car.cars:
        if c.distance(tim) < 20:
            is_ongoing = False
            scoreboard.game_over(level)

    if tim.ycor() > 280:
        level += 1
        tim.goto(0,-280)
        speed *= 1.2







screen.exitonclick()
