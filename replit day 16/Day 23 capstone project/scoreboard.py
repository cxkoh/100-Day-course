from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

    def score(self, level):
        self.clear()
        self.color("black")
        self.penup()
        self.goto(-270,280)
        self.write(f"Level: {level}",move=False, align="center", font=("Arial",10,"normal"))
        self.hideturtle()

    def game_over(self, level):
        self.clear()
        self.color("black")
        self.penup()
        self.goto(0,0)
        self.write(f"GameOver! level: {level}",move=False, align="center", font=("Arial",50,"normal"))