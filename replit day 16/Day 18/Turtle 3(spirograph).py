from turtle import Turtle, Screen
import random
timmy = Turtle()

timmy.speed("fastest")
for _ in range(180):
    random_color = (random.random(), random.random(), random.random())
    timmy.color(random_color)
    timmy.right(10)
    timmy.circle(100)

screen = Screen()
screen.exitonclick()