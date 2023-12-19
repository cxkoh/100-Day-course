from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour").lower()

x_cord = -200
y_cord = 120
color = ['purple', 'red', 'orange', 'green', 'blue', 'yellow']
all_turtle =[]

for index, n in enumerate(color):
    tim = Turtle(shape = "turtle")
    tim.color(color[int(index)])
    tim.penup()
    tim.goto(x_cord, y_cord)
    all_turtle.append(tim)
    y_cord -= 30


winner = " "


is_done = False
while is_done == False:
    for t in all_turtle:
        forwards = random.randint(0,10)
        t.forward(forwards)
        if t.xcor() > 200:
            winner = t
            position = all_turtle.index(winner)
            if user_bet == color[position]:
                print("You are correct, congratulations")
            else:
                print("You are wrong")
            is_done = True





screen.exitonclick()

