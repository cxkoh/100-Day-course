
from turtle import Turtle
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.x_coordinate = 0
        self.y_coordinate = 0
        self.setheading(15)
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)



    def move(self, is_done):
        while is_done == False:
            self.penup()
            self.forward(5)
            self.speed('fastest')

    def change_angle(self,angle,):
        self.setheading(angle)

    def bounce(self):
        if self.heading()<180:
            self.change_angle(360 - self.heading())
        elif self.heading()<270:
            angle = 360 - (self.heading() - 180)
            self.change_angle(angle)
        elif self.heading()<360:
            angle = 180 + (360 - self.heading())
            self.change_angle(angle)

    def reset(self):
        self.goto(0,0)
        self.setheading(15)



