import pandas
import turtle
screen = turtle.Screen()
screen.title("US states game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
correct = 0
guessed = []


data = pandas.read_csv("50_states.csv")
country_list = data.state.to_list()
while correct <50:
    user_guess = screen.textinput(title=f"{correct}/50 Guess the state", prompt="Guess a state").title()
    if user_guess == 'Exit':
        missing_state = [state for state in country_list if state not in guessed]
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("remaining.csv")
        break
    if user_guess in country_list:
        correct += 1
        state_data = data[data.state == user_guess]
        t = turtle.Turtle()
        t.hideturtle()
        t.color("black")
        t.penup()
        t.goto(int(state_data.x),int(state_data.y))
        t.write(user_guess)
        guessed.append(user_guess)





turtle.mainloop()