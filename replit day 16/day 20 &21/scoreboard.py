from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open("logs") as data:
            self.highscore = int(data.read())

    def score(self,score):
        self.clear()
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.write(f"Score = {score} high Score = {self.highscore}",move=False, align="center", font=("Arial",24,"normal"))
        self.hideturtle()


    def gameover(self,score):
        if score > self.highscore:
            self.highscore = score
        self.score(score)
        with open("logs", mode="w") as data:
            data.write(f"{self.highscore}")




