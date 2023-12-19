from turtle import Turtle
import random
timmy = Turtle()
directions = [0,90,180,270]
timmy.pensize(10)
timmy.speed("fastest")

for _ in range(200):
    random_colour = (random.random(), random.random(), random.random())
    timmy.color(random_colour)
    timmy.forward(30)
    timmy.setheading(random.choice(directions))
