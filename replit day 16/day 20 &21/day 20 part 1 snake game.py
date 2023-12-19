from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard





screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()
is_done = False
score = 0

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

while is_done == False:
    screen.update()
    time.sleep(0.1)
    snake.move()
    scoreboard.score(score)

    if food.distance(snake.all_tim[0]) < 15:
        food.refresh()
        print("nom nom nom")
        score += 1
        scoreboard.score(score)
        snake.add()
    if snake.all_tim[0].xcor()>300 or snake.all_tim[0].xcor()<-300:
        snake.gameover()
        scoreboard.gameover(score)
        score = 0

    if snake.all_tim[0].ycor()>300 or snake.all_tim[0].ycor()<-300:
        snake.gameover()
        scoreboard.gameover(score)
        score = 0

    for segment in snake.all_tim[1:]:
        if snake.all_tim[0].distance(segment) < 10:
            snake.gameover()
            scoreboard.gameover(score)
            score = 0









screen.exitonclick()













screen.exitonclick()
file.close()