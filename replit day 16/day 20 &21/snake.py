from turtle import Turtle






class Snake:
    def __init__(self):
        self.x_cord = 0
        self.y_cord = 0
        self.all_tim = []
        self.create()
        self.head = self.all_tim[0]


    def right(self):
        self.all_tim[0].setheading(0)

    def left(self):
        self.all_tim[0].setheading(180)

    def up(self):
        self.all_tim[0].setheading(90)

    def down(self):
        self.all_tim[0].setheading(270)

    def create(self):
        for _ in range(3):
            tim = Turtle("square")
            tim.color("white")
            tim.penup()
            tim.goto(self.x_cord, self.y_cord)
            self.x_cord -= 20
            self.all_tim.append(tim)

    def move(self):
        for t in range(len(self.all_tim) - 1, 0, -1):
            new_x = self.all_tim[t - 1].xcor()
            new_y = self.all_tim[t - 1].ycor()
            self.all_tim[t].goto(new_x, new_y)
        self.all_tim[0].forward(20)

    def gameover(self):
        for tim in self.all_tim:
            tim.goto(1000,1000)
        self.all_tim.clear()
        self.create()
        self.head = self.all_tim



    def add(self):
        tim = Turtle("square")
        tim.color("white")
        tim.penup()
        tim.goto(self.all_tim[-1].position())
        self.all_tim.append(tim)
