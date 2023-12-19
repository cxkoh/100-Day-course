from tkinter import *
import pandas
import random
data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")
current_card = {}
def next():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card= random.choice(to_learn)
    current_card["French"]
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word,text= current_card["French"])
    canvas.itemconfig(card_background,image=card_front)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English")
    canvas.itemconfig(card_word, text=current_card["English"])
    canvas.itemconfig(card_background, image=card_back)

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next()

BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
window.title("Flash card project")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800,height=526)
card_back = PhotoImage(file="images/card_back.png")
card_front = PhotoImage(file="images/card_front.png")
right = PhotoImage(file="images/right.png")
wrong = PhotoImage(file="images/wrong.png")


card_background = canvas.create_image(400,263,image=card_front)
card_title = canvas.create_text(400,158,text="Title",font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400,263,text="word", font=("Ariel", 60, "bold"))
canvas.grid(row=0,column=0,columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

#canvas.create_image(400,263,image=card_back)
#canvas.create_image(50,50,image=right)
#canvas.create_image(50,50,image=wrong)
unknown_button= Button(image=wrong, highlightthickness=0,command=next)
unknown_button.grid(row=1,column=0)
known_button= Button(image=right, highlightthickness=0,command=is_known)
known_button.grid(row=1,column=1)

next()

window.mainloop()



