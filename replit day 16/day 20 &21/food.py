import random
from turtle import Turtle
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.x_coordinate = random.randint(-280,280)
        self.y_coordinate = random.randint(-280,280)
        self.shape("circle")
        self.color("blue")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.refresh()

    def refresh(self):
        x_coordinate = random.randint(-280,280)
        y_coordinate = random.randint(-280,280)
        self.penup()
        self.goto(x_coordinate,y_coordinate)
