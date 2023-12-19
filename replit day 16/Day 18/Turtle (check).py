#line (23, colour is from 1-255, why does random.random() work)
from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("arrow")
#for _ in range(15):
#    timmy.forward(10)
#    timmy.penup()
#    timmy.forward(10)
#    timmy.pendown()

#import turtle as t
#tim = t.Turtle()

#from turtle import * (everything)
#forward(100)

#from random import *
#choice([1, 2, 3])

import random
for _ in range(3,10):
    random_colour = (random.random(),random.random(),random.random())
    sides = _
    interior_angle = 180-(((sides-2)*180)/sides)
    print(interior_angle)
    for n in range(sides):
        timmy.color(random_colour)
        timmy.forward(100)
        timmy.right(interior_angle)







screen = Screen()
screen.exitonclick()
