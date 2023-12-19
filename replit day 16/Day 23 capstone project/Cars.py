import random
from turtle import Turtle
import time

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.random_colour = (random.random(), random.random(), random.random())
        self.hideturtle()
        self.color(self.random_colour)
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.new_y = random.randint(-250,250)
        self.goto(320,self.new_y)
        self.showturtle()

    def move(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Car()
            self.cars.append(new_car)
    def move_car(self,speed):
        for car in self.cars:
            car.backward(speed)
