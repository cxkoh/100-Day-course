from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

    def score(self, xscore, yscore):
        self.clear()
        self.color("white")
        self.penup()
        self.goto(-30,270)
        self.write(f"{xscore}",move=False, align="center", font=("Arial",20,"normal"))
        self.hideturtle()
        self.goto(30,270)
        self.write(f"{yscore}",move=False, align="center", font=("Arial",20,"normal"))