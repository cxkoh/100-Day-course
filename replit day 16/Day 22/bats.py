from turtle import Turtle

class Bats:
    def __init__(self):
        self.xx_cord = -420
        self.xy_cord = 0
        self.yx_cord = 420
        self.yy_cord = 0
        self.tim = Turtle("square")
        self.timy = Turtle("square")

    def xbat(self):
        self.tim.color("white")
        self.tim.penup()
        self.tim.shapesize(stretch_wid = 5, stretch_len=1)
        self.tim.goto(self.xx_cord,self.xy_cord)


    def ybat(self):
        self.timy.color("white")
        self.timy.penup()
        self.timy.shapesize(stretch_wid = 5, stretch_len=1)
        self.timy.goto(self.yx_cord,self.yy_cord)




    def yup(self):
        new_x = self.timy.ycor()+20
        self.timy.goto(self.yx_cord,new_x)

    def ydown(self):
        new_x = self.timy.ycor()-20
        self.timy.goto(self.yx_cord,new_x)

    def xup(self):
        new_x = self.tim.ycor()+20
        self.tim.goto(self.xx_cord,new_x)

    def xdown(self):
        new_x = self.tim.ycor()-20
        self.tim.goto(self.xx_cord,new_x)


