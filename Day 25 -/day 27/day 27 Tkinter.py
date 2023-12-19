from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

#Label, pack lays it out on the screen
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack()
# to change text got 2 ways
my_label["text"] = "New Text" #1
my_label.config(text = "New Text") #2

#Button
def button_clicked():
    my_label["text"] = input.get()
button = Button(text = "Click Me", command=button_clicked)
button.pack()

#Entry
input = Entry(width=10)
input.pack()










window.mainloop()