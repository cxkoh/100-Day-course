from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(2)

def right():
    tim.right(2)

def left():
    tim.left(2)

screen.listen()
screen.onkey(key="Up", fun=move_forward)
screen.onkey(key="Right", fun=right)
screen.onkey(key="Left", fun=left)
screen.exitonclick()
